from pymongo import MongoClient

class GuruMatchDatabase(object):
    URI = "mongodb+srv://guruMatch:orion123@gurumatch-db.j176d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DATABASE = None

    @staticmethod
    def initialize():
        print("initializing the MongoDB")
        client = MongoClient(GuruMatchDatabase.URI)
        GuruMatchDatabase.DATABASE = client.get_database("guruMatchDatabase")
        print(GuruMatchDatabase.DATABASE["user-db"].count_documents({}))
    
    @staticmethod
    def idExist(userID):
        if GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userID}) is None:
            return False
        return True

    @staticmethod
    def isUsernameExist(userID):
        # true = 1, false = 2  [because of protobuf consider 0 as default]
        if len(GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userID}, {"username": 1, "_id": 0})) == 0:
            return 2
        return 1

    @staticmethod
    def insertNewUser(userInfo):
        print("inserting new User data")
        GuruMatchDatabase.DATABASE['user-db'].insert_one(userInfo)

    @staticmethod
    def insertUserForm(userFormData):
        print("inserting User Form data")
        # we dont need to check the userId, because we authenticate the use before using this 
        # function and userID is send by login where login extract the userId from database, so userID will always be valid
        GuruMatchDatabase.DATABASE["user-db"].update_one(
            {"_id":userFormData["_id"]}, 
            {
                "$set":userFormData
            })
        

GuruMatchDatabase.initialize()
print(GuruMatchDatabase.isUsernameExist("60891c85759b8d8fc26dffe0"))
#608895309e12f61b99d44169

        







