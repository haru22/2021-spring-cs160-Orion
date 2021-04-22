require('dotenv').config(); 
const LocalStrategy = require("passport-local").Strategy;
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const FacebookStrategy = require('passport-facebook').Strategy;
const findOrCreate = require('mongoose-findorcreate');

// User model  (mongoDB)
const User = require("../database/user");

module.exports = function(passport) {
    passport.use(
        new LocalStrategy({usernameField: "email"}, (email, password, done) => {
            // see if there email in our database
            User.findOne({email: email})
                .then(user => {
                    // if email not exist or email not match
                    if (!user) {
                        return done(null, false, {message: "Email is not register"});
                    }
                    // if user exist in our database
                    // let match the password given and the 
                    //password from our database which is hashed
                    bcrypt.compare(password, user.password, (err, match) => {
                        if (err) throw err;
                        // if match is true
                        if (match) {
                            return done(null, user);
                        } else {
                            return done(null, false, {message: "Password incorrect"});
                        }
                    });
                })
                .catch(err => console.log(err))
        })
    );

    // let create the session or cookies for log in
    passport.serializeUser((user, done) => {
        done(null, user.id);
      });
    
    passport.deserializeUser((id, done) => {
        User.findById(id, (err, user) => {
          done(err, user);
        });
    });

    // google OAuth
    passport.use(new GoogleStrategy({
        clientID: process.env.CLIENT_ID,
        clientSecret: process.env.CLIENT_SECRET,
        callbackURL: "http://localhost:3000/auth/google/home",
        userProfileURL: "https://www.googleapis.com/oauth2/v3/userinfo"
      },
      function(accessToken, refreshToken, profile, cb) {
        console.log(profile);
        User.findOrCreate({ username: profile.displayName, googleId: profile.id }, function (err, user) {
          return cb(err, user);
        });
      }
    ));

    // facebook OAuth
    passport.use(new FacebookStrategy({
        clientID: process.env.FACEBOOK_APP_ID,
        clientSecret: process.env.FACEBOOK_APP_SECRET,
        callbackURL: "http://localhost:3000/auth/facebook/home"
      },
      function(accessToken, refreshToken, profile, cb) {
        console.log(profile);
        User.findOrCreate({ facebookId: profile.id }, function (err, user) {
          return cb(err, user);
        });
      }
    ));
}
