const mongoose = require("mongoose");
const passport = require("passport");

const findOrCreate = require('mongoose-findorcreate');

const UserSchema = new mongoose.Schema({
    email: {
        type: String,
    },
    password: {
        type: String,
    },
    googleId: {
        type: String
    }

});

const guruMatchDBSchema = new mongoose.Schema({
    name: String,
    profile: {
        file: String,
        intro: String,
        short_description: String,
        skills: [String],
        industry: String,
        work_experience: String,
        long_description: String,
    },
    mentee: {
        short_description: String,
        long_description: String,
        tag: [String]
    },
    mentor: {
        short_description: String,
        long_description: String,
        tag: [String]
    }
});

UserSchema.plugin(findOrCreate);

const User = mongoose.model("User", UserSchema);
const GuruMatchDBSchema = mongoose.model("GuruMatchDBSchema", guruMatchDBSchema);

module.exports.User = User;
module.exports.GuruMatchDBSchema = GuruMatchDBSchema;