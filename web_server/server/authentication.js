module.exports = {
    AuthenticationSuccess: (req, res, next) => {
        if (req.isAuthenticated()) {
            return next();
        }
        req.flash("error_message", "You need to log in view this page");
        res.redirect("login");
    }
}