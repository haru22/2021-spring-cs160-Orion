import grpc from "grpc";
import protoLoader from "@grpc/proto-loader";

const packageDef = protoLoader.loadSync("./guruMatch.proto",{
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
   })
   
const grpcObject = grpc.loadPackageDefinition(packageDef);
const guruMatchPackage = grpcObject.guruMatchPackage;

const server = new grpc.Server();
server.bind("0.0.0.0:50051", grpc.ServerCredentials.createInsecure());

server.addService(guruMatchPackage.GuruMatch.service, {
    "CreateMentee": createMentee
})

server.start();
console.log("server starting on port 4000");

function createMentee (call, callback) {
    console.log(call.request)
    const resp = {
        "persisted": true
    }
    callback(null, resp);
}
