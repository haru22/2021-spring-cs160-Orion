import grpc
import sys

# importing the automated grpc interface stub
sys.path.append("../server")
import guruMatch_pb2 as pb2
import guruMatch_pb2_grpc as pb2_grpc

# open grpc channel
channel = grpc.insecure_channel("localhost:50051")

# create client stub
stub = pb2_grpc.GuruMatchStub(channel)

# create a request
newUser = pb2.CreateUserRequest(
    id="1233e334",
    name="Tenzin Gyatso",
)

# make request
response = stub.CreateUser(newUser)

print("The respnse is " + str(response))

