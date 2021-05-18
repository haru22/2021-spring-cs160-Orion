import grpc
from concurrent import futures
import sys

from grpc_reflection.v1alpha import reflection

# help to convert protobuf to python dictionary
from google.protobuf.json_format import MessageToDict

# importing the automated grpc interface stub
import guruMatch_pb2 as pb2
import guruMatch_pb2_grpc as pb2_grpc
from database import GuruMatchDatabase


class GuruMatchServicer(pb2_grpc.GuruMatchServicer):
    # adding service to the server
    def CreateUser(self, request, context):
        GuruMatchDatabase.insertNewUser(request.id, request.name)
        response = pb2.SuccessResponse(success = True)
        return response
    
    def IsUsernameExist(self, request, context):
        userID = request.id
        print(userID)
        isUserThere = GuruMatchDatabase.isUsernameExist(userID)
        print("response from the databaes is " + str(isUserThere))
        response = pb2.SuccessResponse(success = isUserThere)
        return response
    
    def StoreUserForm(self, request, context):
        print("FORMFORMRFOMR")
        GuruMatchDatabase.insertUserForm(request.id,
            {
                "profile.username": request.username,
                "profile.userBio": request.userBio,
                "profile.userDescription": request.userDescription,
                "profile.userSkill": request.userSkill,
                "profile.userIndustry": request.userIndustry,
                "profile.userTag": request.userTag,
                "profile.profilePic": request.profilePic,
            })
        response = pb2.SuccessResponse(success = 1)
        return response
    
    def GetUserProfile(self, request, context):
        userProfile = GuruMatchDatabase.getUserProfile(request.id)
        print(userProfile)
        response = pb2.UserProfile(
            username = userProfile["username"],
            userBio = userProfile["userBio"],
            userDescription = userProfile["userDescription"],
            userSkill = userProfile["userSkill"],
            userIndustry = userProfile["userIndustry"],
            userTag = userProfile["userTag"],
            name = userProfile["name"],
            profilePic = userProfile["profilePic"],
        )
        return response
    
    def CreateMentee(self, request, context):
        print("inside the create mentee")
        print(request)
        interestList = request.interest.split(",")
        GuruMatchDatabase.createMenteeAndMentor(
            request.id,
            {
               "mentee.interest" : interestList,
               "mentee.mentee-description" : request.menteeDescription
            } )
        response = pb2.SuccessResponse(success = 1)
        return response

    def CreateMentor(self, request, context):
        print("CreateMentor inside the application server")
        print(request)
        interestList = request.interest.split(",")
        GuruMatchDatabase.createMenteeAndMentor(
            request.id,
            {
               "mentor.interest" : interestList,
               "mentor.mentor-description" : request.mentorDescription
            } )
        response = pb2.SuccessResponse(success = 1)
        return response

    def GetMatchMentors(self, request, context):
        print("GetMatchMentors, inside the application server")
        print(request)
        userID = request.id
        allMatchMentors = GuruMatchDatabase.getMatchMentors(userID)

        # since we have repeated in protofile message MatchMentorResponse
        # we have to run the for loop on reponse from the database and 
        # put the value in protobuf and append in MatchMentorResponse
        allMatchMentorToProto = pb2.MatchMentorResponse()
        for aMentor in allMatchMentors:
            responseMentorProto = pb2.MentorResponse()
            responseMentorProto.interest[:] = aMentor["mentor"]["interest"]
            responseMentorProto.mentorDescription = aMentor["mentor"]["mentor-description"]
            allMatchMentorToProto.allMatchMentors.append(pb2.Mentor(
                mentorID = aMentor["_id"],
                userProfile = pb2.UserProfile(
                    username = aMentor["profile"]["username"],
                    userBio = aMentor["profile"]["userBio"],
                    userDescription = aMentor["profile"]["userDescription"],
                    userSkill = aMentor["profile"]["userSkill"],
                    userIndustry = aMentor["profile"]["userIndustry"],
                    userTag = aMentor["profile"]["userTag"],
                    name = aMentor["profile"]["name"],
                    profilePic = aMentor["profile"]["profilePic"],
                ),
                mentor = responseMentorProto
            ))
        return allMatchMentorToProto

    def GetMatchMentees(self, request, context):
        print("GetMatchMentees, inside the application server")
        print(request)
        userID = request.id
        allMatchMentees = GuruMatchDatabase.getMatchMentees(userID)

        allMatchMenteeToProto = pb2.MatchMenteeResponse()
        for aMentee in allMatchMentees:
            responseMenteeProto = pb2.MenteeResponse()
            responseMenteeProto.interest[:] = aMentee["mentee"]["interest"]
            responseMenteeProto.menteeDescription = aMentee["mentee"]["mentee-description"]
            allMatchMenteeToProto.allMatchMentees.append(pb2.Mentee(
                menteeID = aMentee["_id"],
                userProfile = pb2.UserProfile(
                    username = aMentee["profile"]["username"],
                    userBio = aMentee["profile"]["userBio"],
                    userDescription = aMentee["profile"]["userDescription"],
                    userSkill = aMentee["profile"]["userSkill"],
                    userIndustry = aMentee["profile"]["userIndustry"],
                    userTag = aMentee["profile"]["userTag"],
                    name = aMentee["profile"]["name"],
                    profilePic = aMentee["profile"]["profilePic"],
                ),
                mentee = responseMenteeProto
            ))
        return allMatchMenteeToProto

    def InsertMentorSelectedMentee(self, request, context):
        """
        when mentor selected the mentee, we will store the 
        mentorId in mentee matchingDAtabase collection
        """
        menteeID = request.menteeID
        mentorID = request.mentorID
        GuruMatchDatabase.insertMentorSelectedMentee(menteeID, mentorID)
        return 1
    
    def InsertMenteeSelectedMentor(self, request, context):
        menteeID = request.menteeID
        mentorID = request.mentorID
        GuruMatchDatabase.insertMenteeSelectedMentor(mentorID, menteeID)
        return 1

    def GetAllMatchesRequest(self, request, context):
        userID = request.id
        responseFromDB = GuruMatchDatabase.getAllMatchRequest(userID)
        if (responseFromDB is None):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("this user have no matches currently")
            return pb2.AllMatches()
        allMatchesToProto = pb2.AllMatches()
        for allMenteeMatches in responseFromDB["mentee"]:
            allMatchesToProto.allMenteeRequest.append(allMenteeMatches)
        for allMentorMatches in responseFromDB["mentor"]:
            allMatchesToProto.allMentorRequest.append(allMentorMatches)
        return allMatchesToProto
        

    
def run_server():
    # start the database server
    GuruMatchDatabase.initialize()

    # start the application server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GuruMatchServicer_to_server(GuruMatchServicer(), server)
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['GuruMatch'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run_server()
