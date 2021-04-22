const mongoose = require("mongoose");
const passport = require("passport");

const findOrCreate = require('mongoose-findorcreate');

const UserSchema = new mongoose.Schema({
    email: {
        type: String,
        // required: true
    },
    password: {
        type: String,
        // required: true
    },
    username: {
        type: String,
    },
    googleId: {
        type: String
    }

});

UserSchema.plugin(findOrCreate);

const User = mongoose.model("User", UserSchema);

module.exports = User;