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
    def isUsernameExist(userId):
        # true = 1, false = 2  [because of protobuf consider 0 as default]
        print(GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userId}, {"profile.username": 1,"_id": 0}))
        userNameExist = GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userId}, {"profile.username": 1, "_id": 0})
        if (userNameExist is None) or (len(userNameExist["profile"])) == 0:
            return 2
        return 1

    @staticmethod
    def insertNewUser(userId, name):
        print("inserting new User data")
        GuruMatchDatabase.DATABASE['user-db'].insert_one({"_id": userId, "profile":{"name": name}})

    @staticmethod
    def insertUserForm(userId, userFormData):
        print("inserting User Form data")
        # we dont need to check the userId, because we authenticate the use before using this 
        # function and userID is send by login where login extract the userId from database, so userID will always be valid
        GuruMatchDatabase.DATABASE["user-db"].update_one(
            {"_id":userId}, 
            {
                "$set":userFormData
            })
    
    @staticmethod
    def getUserProfile(userId):
        print("Getting user Profile")
        return (GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userId},{"profile":1, "_id":0})["profile"])
        
#GuruMatchDatabase.initialize()
#print(GuruMatchDatabase.isUsernameExist("633d25d5"))
#GuruMatchDatabase.insertNewUser({"_id": "1345234ee", "name": "David Beckham"})
#GuruMatchDatabase.insertUserForm("1345234ee", {"profile.username": "Kicker", "profile.userBio": "I am soccer player"})
#print(GuruMatchDatabase.getUserProfile("608888188def3a0ceded6f12"))
#608895309e12f61b99d44169

        







