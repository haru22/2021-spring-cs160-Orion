/*
This is our web server written in express js
we will call the application server client to send request to 
application server grpc. 
*/

// express js
const express = require("express");
const path = require("path");
// frontend directory
const frontendDir = path.join(__dirname, "../frontend");
// application server client in grpc to interact with our application server
const grpcClientPath = path.join(__dirname, "../applicationServerClient");
const grpcClient = require(grpcClientPath + "/client.js");

const app = express();
// we use urlencoded for parsing the request body
app.use(express.urlencoded());
// server side rendering 
app.use(express.static(frontendDir));

// initializing the server 
app.listen(3000, function(){
    console.log("Server is running on port 3000.")
});

// get request for our homepage or root route
app.get("/", function(req, res){
    res.sendFile(frontendDir + "/index.html");
});

// post request for root route
app.post("/", function(req, res) {
    var email = req.body.email;
    var password = req.body.password;
    grpcClient.userLogin(email, password);
    res.send("Posting the respsonse: " + email)
});
