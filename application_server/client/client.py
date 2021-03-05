import grpc
import sys

# importing the automated grpc interface stub
sys.path.append("./")
import guruMatch_pb2 as pb2
import guruMatch_pb2_grpc as pb2_grpc

# open grpc channel
channel = grpc.insecure_channel("localhost:50051")

# create client stub
stub = pb2_grpc.GuruMatchStub(channel)

# create a request
newMentee = pb2.Mentee(
    id=0,
    name="Tenzin Gyatso",
    email="dalai.lama@gmail.com",
    username="gyatso",
    school="SJSU",
    interest="Computer Science"
)
newMenteeRequest = pb2.CreateMenteeRequest(mentee=newMentee)

# make request
response = stub.CreateMentee(newMenteeRequest)

print("The respnse is " + str(response))

