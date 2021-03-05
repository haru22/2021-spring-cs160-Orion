from pymongo import MongoClient

class GuruMatchDatabase(object):
    URI = "mongodb://localhost:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        print("initializing the MongoDB")
        client = MongoClient(GuruMatchDatabase.URI)
        GuruMatchDatabase.DATABASE = client["guruMatchDatabase"]

    @staticmethod
    def insertNewMentee(menteeInfo):
        GuruMatchDatabase.DATABASE['mentee-db'].insert_one(menteeInfo)


# if __name__ == "__main__":
#     GuruMatchDatabase.initialize()
#     GuruMatchDatabase.insertNewMentee({"name": "Tenzin Wangpo"})


        
        







