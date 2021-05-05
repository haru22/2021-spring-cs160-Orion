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

app.post("/userForm/:id", function(req, res) {
  const {username, userBio, userDescription, userSkills, userIndustry, userTag} = req.body;
  console.log(username + " " + userBio+ " " +userDescription+ " " +userSkills+ " " +userIndustry+ " " +userTag)
  console.log("request: " + req.params.id)
  const userid = req.params.id
  grpcClient.storeUserForm(userid, username, userBio, userDescription, userSkills, userIndustry, userTag);
  res.redirect("/welcome/" + userid)
});

// get request for welcome route
app.get("/welcome/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const userProfile = await grpcClient.getUserProfile(userId)
  const json_userProfile = JSON.parse(userProfile)
  const username = json_userProfile.username
  console.log("username: " + username)
  res.render("welcome", {username: username, id: userId});
});

// get request for home route
app.get("/home/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const userProfile = await grpcClient.getUserProfile(userId)
  const json_userProfile = JSON.parse(userProfile)
  res.render("home", {userProfile: json_userProfile, id: userId})
});

// get request for profile route
app.get("/profile/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const userProfile = await grpcClient.getUserProfile(userId)
  const json_userProfile = JSON.parse(userProfile)
  console.log(json_userProfile)
  res.render("profile", {userProfile: json_userProfile, id: userId})
});

// post request for creating mentee route 
app.post("/createMentee/:id", AuthenticationSuccess, async function (req, res) {
  const {interest, menteeDescription} = req.body;
  const userId = req.params.id
  console.log(interest + " " + menteeDescription)
  grpcClient.createMentee(userId, interest, menteeDescription)
  console.log("I am creating mentee")
  res.redirect("/home/"+userId)
})

// post request for creating mentor route 
app.post("/createMentor/:id", AuthenticationSuccess, async function (req, res) {
  const userId = req.params.id
  const {interest, mentorDescription} = req.body;
  grpcClient.createMentor(userId, interest, mentorDescription)
  console.log("i am creating a mentor")
  res.redirect("/home/"+userId)
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
    let redirectURI = "/welcome";
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


