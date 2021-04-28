const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");
const caller = require("grpc-caller");
const { response } = require("express");
const protopath = __dirname + "/guruMatch.proto"
const client = caller("localhost:50051", protopath, "GuruMatch");
/*
const packageDef = protoLoader.loadSync(protopath, {});
const grpcObject = grpc.loadPackageDefinition(packageDef);
const guruMatchPackage = grpcObject.guruMatchPackage;

const client = new guruMatchPackage.GuruMatch("localhost:50051", grpc.credentials.createInsecure());
*/

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

    isUsernameExist: async (id) => {
        const grpcRequest = {
            "id": id
        }
        // if usernameExist is 2, that means user haven't set up the form
        // if 1, then show the homepage
        let usernameExist = 2;
        usernameExist = await client.IsUsernameExist(grpcRequest);//.then(res => {usernameExist = res});
        console.log("Hello " + usernameExist.success)
        return usernameExist.success;
    },

    storeUserForm: (id, username, user_bio, user_description, 
        user_skill, user_industry, user_tag) => {
            const grpcRequest = {
                "id": id,
                "username": username,
                "userBio": user_bio,
                "userDescription": user_description,
                "userSkill": user_skill,
                "userIndustry": user_industry,
                "userTag": user_tag
            }
            let res = false;
            client.StoreUserForm(grpcRequest, (err, response) => {
                console.log("recieved from server (StoreUserForm) " + JSON.stringify(response));
            })
            return res
    }
}








