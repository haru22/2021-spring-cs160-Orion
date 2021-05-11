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

"""
# create a request
newUser = pb2.UserFormData(
    id = "608895309e12f61b99d44169",
    username = "10zin",
    userBio = "I am Tenzin Wangpo",
    userDescription = "I love computer science",
    userSkill = "Python, Golang",
    userIndustry = "SJSU",
    userTag = "Testing, RestAPI",
)
"""

#create request
#requests = pb2.IDonlymessage(id = "608888188def3a0ceded6f12")
"""
requests = pb2.CreateMentorRequest(
    id = "60920a94f652b4c0b9479c02",
    interest = "python, Java, Golang",
    mentorDescription = "I love to learn about the python, JAva, and Golang"
)"""
"""
users = pb2.UserFormRequest(
    id = "608895309e12f61b99d44169",
    username = "10zin",
    userBio = "I am Tenzin Wangpo",
    userDescription = "I love computer science",
    userSkill = "Python, Golang",
    userIndustry = "SJSU",
    userTag = "Testing, RestAPI",
)

print("asdfasdf")
"""
# make request
#response = stub.CreateUser(newUser)
#print(stub.IsUsernameExist(requests))
#print(stub.CreateMentor(requests))
#print("The response is " + str(response))

req = pb2.IDonlymessage(id = "6095ab14b3e334370b1cf9cb")
print(stub.GetMatchMentors(req))




