import grpc from "grpc";
import protoLoader from "@grpc/proto-loader";

const packageDef = protoLoader.loadSync("./guruMatch.proto",{})
const grpcObject = grpc.loadPackageDefinition(packageDef);
const guruMatchPackage = grpcObject.guruMatchPackage;

const client = new guruMatchPackage.GuruMatch("localhost:50051", grpc.credentials.createInsecure());

const newMentee = {
    "id":0,
    "name":"Tenzin Wangpo",
    "email":"Tenzin.Wangpo@gmail.com",
    "username":"gyatso",
    "school":"SJSU",
    "interest":"Computer Science"
}

client.CreateMentee({"mentee": newMentee}, (err, response) => {
    console.log("recieved From server " + JSON.stringify(response))
})





