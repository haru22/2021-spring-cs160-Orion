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

// session middleware
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
const User = require("../database/user");

// frontend directory
const frontendDir = path.join(__dirname, "../frontend");

// application server client in grpc to interact with our application server
const grpcClientPath = path.join(__dirname, "../applicationServerClient");
const grpcClient = require(grpcClientPath + "/client.js");

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
  passport.authenticate("local", {
    successRedirect: "/home",
    failureRedirect: "/login",
    failureFlash: true
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
            username: firstName + " " + lastName,
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

// get request for home route
app.get("/home", AuthenticationSuccess, function (req, res) {
  res.render("home");
});
// app.get("/home", function(req, res) {
//   res.render("home");
// })

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
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect("/home");
  });

// get request for facebook auth
app.get("/auth/facebook",
  passport.authenticate("facebook"));

app.get("/auth/facebook/home",
  passport.authenticate("facebook", { failureRedirect: "/login" }),
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect('/home');
  });