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
const { response } = require("express");
const protopath = __dirname + "/guruMatch.proto"
const packageDef = protoLoader.loadSync(protopath, {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const guruMatchPackage = grpcObject.guruMatchPackage;

const client = new guruMatchPackage.GuruMatch("localhost:50051", grpc.credentials.createInsecure());
/*
exports.userLogin = function(email, password) {
    console.log(email + " password: " + password);
    const newMentee = {
        "id": 1,
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
}*/

module.exports = {
    createUser: (id, name) => {
        const userRequest = {
            "id": id,
            "name": name,
        }
        client.CreateUser(userRequest, (err, response) => {
            console.log("recieved From Server " + JSON.stringify(response))
        });
    },
    createInterests: (id, interest1) => {
        const interestRequest = {
            "id": id,
            "interest": interest1
        }
        client.CreateInterests(interestRequest, (err, response) => {
            console.log("recieved From Server " + JSON.stringify(response))
        });
    }
}
function createInterests (id, interest1) {
    const interestRequest = {
        "id": id,
        "interest": interest1
    }
    client.CreateInterests(interestRequest, (err, response) => {
        console.log("recieved From Server (CreateInterest) : " + response.success)
    });
}

createInterests("123swe4", "python, Java");






