/*
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");

const packageDef = protoLoader.loadSync("./guruMatch.proto", {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const guruMatchPackage = grpcObject.guruMatchPackage;

const client = new guruMatchPackage.GuruMatch("localhost:50051", grpc.credentials.createInsecure());

const newMentee = {
    "id":1,
    "name":"John Wick",
    "email":"JohnWick@gmail.com",
    "username":"JohnTheKiller",
    "school":"Avenger-B",
    "interest":"Martial Arts"
}

client.CreateMentee({"mentee": newMentee}, (err, response) => {
    console.log("recieved From server " + JSON.stringify(response))
})
*/

const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");
const protopath = __dirname + "/guruMatch.proto"
const packageDef = protoLoader.loadSync(protopath, {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const guruMatchPackage = grpcObject.guruMatchPackage;

const client = new guruMatchPackage.GuruMatch("localhost:50051", grpc.credentials.createInsecure());

exports.userLogin = function(email, password) {
    console.log(email + " password: " + password);
    const newMentee = {
        "id":1,
        "name":"John Wick",
        "email":"JohnWick@gmail.com",
        "username":"JohnTheKiller",
        "school":"Avenger-B",
        "interest":"Martial Arts"
    }
    
    
    client.CreateMentee({"mentee": newMentee}, (err, response) => {
        console.log("recieved From server " + JSON.stringify(response))
    })
    return;
}





