from pymongo import MongoClient

class GuruMatchDatabase(object):
    URI = "mongodb+srv://guruMatch:orion123@gurumatch-db.j176d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        print("initializing the MongoDB")
        client = MongoClient(GuruMatchDatabase.URI)
        GuruMatchDatabase.DATABASE = client.get_database("guruMatchDatabase")
        print(GuruMatchDatabase.DATABASE["mentee-db"].count_documents({}))

    @staticmethod
    def insertNewMentee(menteeInfo):
        print("inserting")
        GuruMatchDatabase.DATABASE['mentee-db'].insert_one(menteeInfo)


# if __name__ == "__main__":
#     GuruMatchDatabase.initialize()
#     GuruMatchDatabase.insertNewMentee({"name": "Tenzin Wangpo"})


        
        







