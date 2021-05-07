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
        GuruMatchDatabase.DATABASE['user-db'].insert_one({"_id": userId, "profile":{"name": name}, "mentee": {}, "mentor":{}})

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

    # can use this for both creating mentor and mentee even though it say create
    @staticmethod
    def createMenteeAndMentor(userId, userInput):
        print("inserting the the mentee or mentor input")
        print(userInput)
        GuruMatchDatabase.DATABASE["user-db"].update_one(
            {"_id": userId},
            {
                "$set": userInput
            }
        )
    
    @staticmethod
    def getMatchMentor(userId):
        menteeProfile = GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userId})
        # Check if the user have set up the interest or not
        userMenteeSetUp = True
        if (len(menteeProfile["mentee"]) == 0 or menteeProfile["mentee"]["interest"] == None):
            userMenteeSetUp = False
        # find() will return the cursor to first document from our collection in database
        alluser = GuruMatchDatabase.DATABASE["user-db"].find()
        currentNumberOfUser = 0
        totalUserReturn = 10
        listOfReturnUser = list()
        # we will only return 10 users
        if (not userMenteeSetUp):
            try:
                while( currentNumberOfUser < totalUserReturn):
                    currentCursor = alluser.next()
                    if (len(currentCursor["mentee"]) == 0 or currentCursor["mentee"]["interest"] == None):
                        continue
                    listOfReturnUser.append(currentCursor)
                    currentNumberOfUser += 1
            except StopIteration:
                print("STop Iteration")
        else:
            menteeInterest = menteeProfile["mentee"]["interest"]
            try:
                while(currentNumberOfUser < totalUserReturn):
                    currentUserCursor = alluser.next()
                    if (any(item in currentUserCursor["mentor"]["interest"] for item in menteeInterest)):
                        listOfReturnUser.append(currentUserCursor)
            except StopIteration:
                if (len(listOfReturnUser) < totalUserReturn):
                    try:
                        while( currentNumberOfUser < totalUserReturn):
                            listOfReturnUser.append(alluser.next())
                            currentNumberOfUser += 1
                    except StopIteration:
                        print("STop Iteration")
        return listOfReturnUser

        """
        try:
            alluser = GuruMatchDatabase.DATABASE["user-db"].find()
            while(alluser):
                print(alluser.next())
        except StopIteration:
            print("STop Iteration")"""

#GuruMatchDatabase.initialize()
#print(GuruMatchDatabase.isUsernameExist("633d25d5"))
#GuruMatchDatabase.insertNewUser({"_id": "1345234ee", "name": "David Beckham"})
#GuruMatchDatabase.insertUserForm("1345234ee", {"profile.username": "Kicker", "profile.userBio": "I am soccer player"})
#print(GuruMatchDatabase.getUserProfile("608888188def3a0ceded6f12"))
#608895309e12f61b99d44169
#GuruMatchDatabase.getMatchMentor("609371cf438a5923aa91b196")

        







