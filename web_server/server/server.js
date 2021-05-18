/*
This is our web server written in express js
we will call the application server client to send request to 
application server grpc. 
*/
// environmental variable
require('dotenv').config(); 
// Express js
const express = require("express");
const bodyParser = require('body-parser');
// session to store the message when redirect the route
const flash = require("connect-flash");
const session = require("express-session");
// mongoose for MongoDB
const mongoose = require("mongoose");
// bcrypt for password
const bcrypt = require("bcryptjs");
//passport 
const passport = require("passport");
// google auth
const GoogleStrategy = require('passport-google-oauth20').Strategy;
// facebook auth
const FacebookStrategy = require('passport-facebook').Strategy;
const findOrCreate = require('mongoose-findorcreate');
// for upload image
const multer = require('multer')


// define storage for the image
const Storage = multer.diskStorage({
  destination: "./frontend/uploads",
  filename:(req,file,callback) => {
    callback(null, file.fieldname+"_"+Date.now()+path.extname(file.originalname));
  }
});

// upload params for multer
const upload = multer({
  storage: Storage
}).single('file');


const app = express();
const path = require("path");

// export passport.js
require("./passport")(passport);

const {AuthenticationSuccess} = require("./authentication");

// session middleware which use the MemoryStorage 
app.use(session({
    secret: 'guruMatch secret',
    resave: false,
    saveUninitialized: false
}));

// passport middleware
app.use(passport.initialize());
app.use(passport.session());


// middleware for connect flash
app.use(flash());

// middleware for global Variables
app.use((req, res, next) => {
    res.locals.success_message = req.flash("success_message");
    res.locals.error_message = req.flash("error_message");
    next();
});

// connect to MongoDB
const dbURI =
  "mongodb+srv://guruMatch:orion123@gurumatch-db.j176d.mongodb.net/guruMatchDatabase";
mongoose.connect(dbURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("MongoDB connected..."))
  .catch((err) => console.log(err));

mongoose.set("useCreateIndex", true);

// User model
const {User, GuruMatchDBSchema} = require("../database/user");
const { SSL_OP_EPHEMERAL_RSA } = require('constants');

// frontend directory
const frontendDir = path.join(__dirname, "../frontend");

// application server client in grpc to interact with our application server
const grpcClientPath = path.join(__dirname, "../applicationServerClient");
const grpcClient = require(grpcClientPath + "/client");

// we use urlencoded for parsing the request body
app.use(express.urlencoded({ extended: false }));

// server side rendering
app.use(express.static(frontendDir));

// EJS
app.set("views", frontendDir);
app.set("view engine", "ejs");
// bodyParser
app.use(bodyParser.urlencoded({extended:true}));
// initializing the server
app.listen(3000, function () {
  console.log("Server is running on port 3000.");
});

// get request for login route
app.get("/login", function (req, res) {
  res.render("login");
});

// post request for login route
app.post("/login", function (req, res, next) {
  passport.authenticate('local', function(err, user, info) {
    if (err) { return next(err); }
    if (!user) { return res.redirect('/login'); }
    req.logIn(user, async function(err) {
      if (err) { return next(err); }
      // here we will check if the user already fill up the form, 
      // if not, then redirect to userForm page, else, redirect to welcome page
      // if usernameExist is 2, then false, if 1 then true
      const userID = user._id.toString();
      let redirectURI = "/welcome/" + userID;
      const usernameExist = await grpcClient.isUsernameExist(userID).catch((err) => console.log("ERROR: ", err))
      console.log("asdfasdf " + usernameExist)
      if (usernameExist == 2) {
        redirectURI = "/userForm/" + userID;
      }
      return res.redirect(redirectURI);
    });
  })(req, res, next);
});

// get request for register route
app.get("/register", function (req, res) {
  res.render("register");
});

// post request for register route
app.post("/register", function (req, res) {
  // extracting the data from req body
  const { firstName, lastName, email, password, passwordConfirm } = req.body;
  let errors = [];

  // let check if all the field are filled
  if (!firstName || !lastName || !email || !password || !passwordConfirm) {
    errors.push({ msg: "Please fill in all fields" });
  }

  // check if the both password are match
  if (password !== passwordConfirm) {
    errors.push({ msg: "Passwords do not match" });
  }

  // check the password length
  if (password.length < 6) {
    errors.push({ msg: "Password should be atleast 6 characters" });
  }

  if (errors.length > 0) {
    res.render("register", {
      errors,
      firstName,
      lastName,
      email,
      password,
      passwordConfirm,
    });
  } else {
    // validation passed
    User.findOne({ email: email })
      .then((user) => {
        if (user) {
          // user already exists
          errors.push({ msg: "Email is already registered" });
          res.render("register", {
            errors,
            firstName,
            lastName,
            email,
            password,
            passwordConfirm,
          });
        } else {
          const newUser = new User({
            email: email,
            password: password,
          });

          // let hash the password
          bcrypt.genSalt(10, (err, salt) =>
            bcrypt.hash(newUser.password, salt, (err, hash) => {
                if (err) throw err;
                // set the hash password to user password
                newUser.password = hash;
                // let save the newUser to database
                newUser.save()
                    .then(user => {
                        // Let send the request to application server through grpc and with data
                        grpcClient.createUser(user._id.toString(), firstName + lastName);
                        req.flash("success_message", "You are now register and can log in");
                        res.redirect("login");
                    })
                    .catch(err => console.log(err));
            })
          );
        }
      })
      .catch();
  }
});



// get request for user-form 
app.get("/userForm/:id", AuthenticationSuccess, function(req, res) {
  res.render("userdataForm", {id: req.params.id})
});

app.post("/userForm/:id", upload, function(req, res) {
  const {username, userBio, userDescription, userSkills, userIndustry, userTag} = req.body;
  const file = req.file.filename;
  console.log(username + " " + userBio+ " " +userDescription+ " " +userSkills+ " " +userIndustry+ " " +userTag + " " + file)
  console.log("request: " + req.params.id)
  const userid = req.params.id
  grpcClient.storeUserForm(userid, username, userBio, userDescription, userSkills, userIndustry, userTag, file);
  res.redirect("/welcome/" + userid)
});

// get request for welcome route
app.get("/welcome/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const userProfile = await grpcClient.getUserProfile(userId)
  console.log("I am in welcome Page")
  const json_userProfile = JSON.parse(userProfile)
  const username = json_userProfile.username
  console.log("username: " + username)

  // use below code for notification, which send the number of new match request 
  // there may be error when user dont have match (in case when user is new and haven't)
  // choose any mentor or mentee then return for allMatches will be None and get 
  // NotFound Error from the server, so we have to use try and catch
  // when catch the error, it will do nothing since numberOfMatches is already 0
  let numberOfMatches = 0;
  try {
    const userAllMatches = await grpcClient.getAllMatches(userId)
    console.log(userAllMatches)
    const matches = JSON.parse(userAllMatches)
    numberOfMatches = matches.allMentorRequest.length + matches.allMenteeRequest.length
  }
  catch (error) {
  }
  res.render("welcome", {username: username, id: userId, numOfMatch: numberOfMatches});
});

// get request for home route
app.get("/home/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const userProfile = await grpcClient.getUserProfile(userId)
  const userMatchMentors = await grpcClient.getMatchMentors(userId)
  const userMatchMentees = await grpcClient.getMatchMentees(userId)
  const json_userProfile = JSON.parse(userProfile)
  const json_userMatchMentors = JSON.parse(userMatchMentors)
  const json_userMatchMentees = JSON.parse(userMatchMentees)

  let numberOfMatches = 0;
  try {
    const userAllMatches = await grpcClient.getAllMatches(userId)
    console.log(userAllMatches)
    const matches = JSON.parse(userAllMatches)
    numberOfMatches = matches.allMentorRequest.length + matches.allMenteeRequest.length
  }
  catch (error) {
  }

  res.render("home", {
    id: userId, 
    userProfile: json_userProfile, 
    mentorsMatch: json_userMatchMentors.allMatchMentors, 
    menteesMatch: json_userMatchMentees.allMatchMentees,
    numOfMatch: numberOfMatches
  })
});

// get request for profile route
app.get("/profile/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const userProfile = await grpcClient.getUserProfile(userId)
  const json_userProfile = JSON.parse(userProfile)

  let numberOfMatches = 0;
  try {
    const userAllMatches = await grpcClient.getAllMatches(userId)
    console.log(userAllMatches)
    const matches = JSON.parse(userAllMatches)
    numberOfMatches = matches.allMentorRequest.length + matches.allMenteeRequest.length
  }
  catch (error) {
  }

  res.render("profile", {
    userProfile: json_userProfile, 
    id: userId,
    numOfMatch: numberOfMatches
  })
});

app.get("/faq/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id

  let numberOfMatches = 0;
  try {
    const userAllMatches = await grpcClient.getAllMatches(userId)
    console.log(userAllMatches)
    const matches = JSON.parse(userAllMatches)
    numberOfMatches = matches.allMentorRequest.length + matches.allMenteeRequest.length
  }
  catch (error) {
  }
  res.render("faq", {id: userId, numOfMatch: numberOfMatches})
});

// post request for creating mentee route 
app.post("/createMentee/:id", AuthenticationSuccess, async function (req, res) {
  const {interest, menteeDescription} = req.body;
  const userId = req.params.id
  grpcClient.createMentee(userId, interest, menteeDescription)
  console.log("I am creating mentee")
  res.redirect("/home/"+userId)
})

// post request for creating mentor route 
app.post("/createMentor/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const {interest, mentorDescription} = req.body;
  grpcClient.createMentor(userId, interest, mentorDescription)
  res.redirect("/home/"+userId)
})

// post request, when user mentor selected the mentee from the home page
app.post("/createMenteeMatch/:mentorID/:menteeID", AuthenticationSuccess, async function (req, res) {
  const menteeId = req.params.menteeID
  const mentorId = req.params.mentorID
  grpcClient.insertMentorSelectedMentee(menteeId, mentorId)
  res.redirect("/home/"+mentorId)
})

// post request, when user mentee selected the mentor from home page, 
app.post("/createMentorMatch/:menteeID/:mentorID", AuthenticationSuccess, async function (req, res) {
  const menteeId = req.params.menteeID
  const mentorId = req.params.mentorID
  grpcClient.insertMenteeSelectedMentor(menteeId, mentorId)
  res.redirect("/home/"+menteeId)
})

// get request for notification 
app.get("/notification/:id", async function (req, res) {
  const userID = req.params.id
  const userProfile = await grpcClient.getUserProfile(userID)
  const json_userProfile = JSON.parse(userProfile)
  
  // use below code for notification, which send the number of new match request 
  var allMentorProfile = new Array();
  var allMenteeProfile = new Array();
  let numberOfMatches = 0;
  try {
    const userAllMatches = await grpcClient.getAllMatches(userID)
    const matches = JSON.parse(userAllMatches)
    numberOfMatches = matches.allMentorRequest.length + matches.allMenteeRequest.length

    matches.allMentorRequest.forEach(async matchMentorID => {
      console.log(matchMentorID)
      const userProfile = await grpcClient.getUserProfile(matchMentorID)
      const json_userProfile = JSON.parse(userProfile)
      allMentorProfile.push(json_userProfile)
    });

    matches.allMenteeRequest.forEach(async matchMenteeID => {
      console.log(matchMenteeID)
      const userProfile = await grpcClient.getUserProfile(matchMenteeID)
      const json_userProfile = JSON.parse(userProfile)
      allMenteeProfile.push(json_userProfile)
    });
    await sleep(100)
  } catch (error) {}
  res.render("notification", {
    id: userID,
    userProfile: json_userProfile, 
    allMatchMentor: allMentorProfile,
    allMatchMentee: allMenteeProfile,
    numOfMatch: numberOfMatches
  })
})

// Logout handler
app.get("/logout", function(req, res) {
  req.logOut();
  req.flash("success_message", "Successfuly Logout");
  res.redirect("login");
})

// get request for google auth
app.get("/auth/google",
  passport.authenticate("google", { scope: ["profile"] }));

// redirect to home
app.get("/auth/google/home", 
  passport.authenticate("google", { failureRedirect: "/login" }),
  async function(req, res) {
    //console.log(req.authInfo._json)
    const userID = req.user._id.toString();
    await grpcClient.createUser(userID, req.authInfo._json.name);
    // here we will check if the user already fill up the form, 
    //if not, then redirect to userForm page, else, redirect to home page
    // if usernameExist is 2, then false, if 1 then true
    let redirectURI = "/welcome/" + userID;
    const usernameExist = await grpcClient.isUsernameExist(userID)
    console.log("asdfasdf " + usernameExist)
    if (usernameExist == 2) {
      redirectURI = "/userForm/" + userID;
    }
    res.redirect(redirectURI);
  });

// get request for facebook auth
app.get("/auth/facebook",
  passport.authenticate("facebook"));

app.get("/auth/facebook/home",
  passport.authenticate("facebook", { failureRedirect: "/login" }),
  function(req, res) {
    // Successful authentication, redirect welcome.
    res.redirect('/welcome');
  });

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
  

