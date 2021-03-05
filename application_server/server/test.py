import sys

sys.path.append("./")
import guruMatch_pb2 as pb2
import guruMatch_pb2_grpc as pb2_grpc

from mongoDatabase.database import GuruMatchDatabase

GuruMatchDatabase.initialize()
GuruMatchDatabase.insertNewMentee({"name": "Tenzin Wangpo"})