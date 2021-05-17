const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");
const caller = require("grpc-caller");
const { response } = require("express");
const protopath = __dirname + "/guruMatch.proto"
const client = caller("localhost:50051", protopath, "GuruMatch");

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
        return usernameExist.success;
    },

    storeUserForm: (id, username, user_bio, user_description, 
        user_skill, user_industry, user_tag, profile_pic) => {
            const grpcRequest = {
                "id": id,
                "username": username,
                "userBio": user_bio,
                "userDescription": user_description,
                "userSkill": user_skill,
                "userIndustry": user_industry,
                "userTag": user_tag,
                "profilePic": profile_pic,
            }
            let res = 2;
            client.StoreUserForm(grpcRequest, (err, response) => {
                console.log("recieved from server (StoreUserForm) " + JSON.stringify(response));
            })
            return res
    },

    getUserProfile: async (id) => {
        const grpcRequest = {
            "id": id
        };
        let res = ""
        res =  await client.GetUserProfile(grpcRequest);
        return JSON.stringify(res)
    }, 

    createMentee: async (id, interests, description) => {
        const grpcRequest = {
            "id" : id,
            "interest" : interests,
            "menteeDescription" : description
        };
        let res = 2
        res = await client.CreateMentee(grpcRequest);
        return res;
    },

    createMentor: async (id, interests, description) => {
        const grpcRequest = {
            "id" : id,
            "interest" : interests,
            "mentorDescription" : description
        };
        let res = 2
        res = await client.CreateMentor(grpcRequest);
        return res;
    },

    getMatchMentors: async (id) => {
        const grpcRequest = {
            "id" : id
        };
        let res = await client.GetMatchMentors(grpcRequest);
        return JSON.stringify(res);
    },

    getMatchMentees: async (id) => {
        const grpcRequest = {
            "id" : id
        };
        let res = await client.GetMatchMentees(grpcRequest);
        //console.log(JSON.stringify(res))
        return JSON.stringify(res);
    },

    insertMentorSelectedMentee: async (menteeID, mentorID) => {
        console.log("menteeID : " + menteeID  + "mentorID : " + mentorID)
        const grpcRequest = {
            "menteeID" : menteeID,
            "mentorID" : mentorID
        };
        let res = await client.InsertMentorSelectedMentee(grpcRequest);
        return JSON.stringify(res);
    },

    insertMenteeSelectedMentor: async (menteeID, mentorID) => {
        console.log("menteeID : " + menteeID  + "mentorID : " + mentorID)
        const grpcRequest = {
            "menteeID" : menteeID,
            "mentorID" : mentorID
        };
        let res = await client.InsertMenteeSelectedMentor(grpcRequest);
        return JSON.stringify(res);
    },

    getAllMatches: async (userID) => {
        const grpcRequest = {
            "id" : userID
        };
        let res = await client.GetAllMatchesRequest(grpcRequest);
        return JSON.stringify(res);
    }
}

/*
async function test(userID) {
    const grpcRequest = {
        "id" : userID
    };
    let res = await client.GetAllMatchesRequest(grpcRequest).then(result => {return result});
    return JSON.stringify(res);
}*/








