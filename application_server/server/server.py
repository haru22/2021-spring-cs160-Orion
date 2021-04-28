import grpc
from concurrent import futures
import sys

# help to convert protobuf to python dictionary
from google.protobuf.json_format import MessageToDict

# importing the automated grpc interface stub
import guruMatch_pb2 as pb2
import guruMatch_pb2_grpc as pb2_grpc
sys.path.append("../")
from mongoDatabase.database import GuruMatchDatabase


class GuruMatchService(pb2_grpc.GuruMatchServicer):
    # adding service to the server

    """
    def CreateMentee(self, request, context):
        # CreateMentee service will create the new mentee and persist the new mentee data in mongoDatabase
        print("asdfasdf")
        print(request)
        # here we are converting the protobuf response to the python dictionary because pymongo
        # only take dictionary data structure
        menteeDict = list(MessageToDict(request).values())[0]
        # then insert into the mongodb
        GuruMatchDatabase.insertNewMentee(menteeDict)
        # send the response back to client
        response = pb2.CreateMenteeResponse(persisted=True)
        return response

    def GetUserName(self, request, context):
        # CreateMentee service will create the new mentee and persist the new mentee data in mongoDatabase
        print("get user name")
        print(request)
        # here we are converting the protobuf response to the python dictionary because pymongo
        # only take dictionary data structure
        menteeDict = list(MessageToDict(request).values())[0]
        # then insert into the mongodb
        user = GuruMatchDatabase.GetUserName()
        print(user)
        # send the response back to client
        response = pb2.GetUserNameResponse({"userName": user.username})
        return response
    """
    
    def CreateUser(self, request, context):
        GuruMatchDatabase.insertNewMentee({"_id": request.id, "name": request.name})
        response = pb2.SuccessResponse(success = True)
        return response
    



def run_server():
    # start the database server
    GuruMatchDatabase.initialize()

    # start the application server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GuruMatchServicer_to_server(GuruMatchService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    run_server()
