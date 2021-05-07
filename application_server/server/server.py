import grpc
from concurrent import futures
import sys

from grpc_reflection.v1alpha import reflection

# help to convert protobuf to python dictionary
from google.protobuf.json_format import MessageToDict

# importing the automated grpc interface stub
import guruMatch_pb2 as pb2
import guruMatch_pb2_grpc as pb2_grpc
sys.path.append("../")
from mongoDatabase.database import GuruMatchDatabase


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
