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
    def getMatchMentors(userId):
        """
        it will return all the mentors that match the mentee interest
        """
        menteeProfile = GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userId})
        # Check if the user have set up the mentee interest or not
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
                    if (currentCursor["_id"] == userId or len(currentCursor["mentor"]) == 0 or currentCursor["mentor"]["interest"] is not None):
                        continue
                    listOfReturnUser.append(currentCursor)
                    currentNumberOfUser += 1
            except StopIteration:
                pass
        else:
            menteeInterest = menteeProfile["mentee"]["interest"]
            try:
                while(currentNumberOfUser < totalUserReturn):
                    currentUserCursor = alluser.next()
                    if (currentUserCursor["_id"] != userId and len(currentUserCursor["mentor"]) > 0 and currentUserCursor["mentor"]["interest"] is not None):
                        if (any(item in currentUserCursor["mentor"]["interest"] for item in menteeInterest)):
                            listOfReturnUser.append(currentUserCursor)
                    else:
                        continue
            except StopIteration:
                if (len(listOfReturnUser) < totalUserReturn):
                    try:
                        alluser = GuruMatchDatabase.DATABASE["user-db"].find()
                        while( currentNumberOfUser < totalUserReturn):
                            # TODO make sure to add new user at end if there is less mentor matched
                            # have to start from the beginning with find()
                            currentUserCursor = alluser.next()
                            if (currentUserCursor["_id"] != userId and len(currentUserCursor["mentor"]) > 0 and currentUserCursor["mentor"]["interest"] is not None):
                                listOfReturnUser.append(currentUserCursor)
                                currentNumberOfUser += 1
                    except StopIteration:
                        pass
        return listOfReturnUser

    @staticmethod
    def getMatchMentees(userId):
        """
        we could have use the above method since both static method are same, but it highly 
        reduce the readibility and simplicity so I have decided to write method which is 
        similar to above method. 

        It will return all the mentees which match with the mentor
        """
        mentorProfile = GuruMatchDatabase.DATABASE["user-db"].find_one({"_id": userId})
        # Check if the user have set up the mentor interest or not and if not set up then
        # return random 10 users
        userMentorSetUp = True
        if (len(mentorProfile["mentor"]) == 0 or mentorProfile["mentor"]["interest"] == None):
            userMentorSetUp = False
        # find() will return the cursor to first document from our collection in database
        alluser = GuruMatchDatabase.DATABASE["user-db"].find()
        currentNumberOfUser = 0
        totalUserReturn = 10
        listOfReturnUser = list()
        # we will only return 10 users
        if (not userMentorSetUp):
            try:
                while( currentNumberOfUser < totalUserReturn):
                    currentCursor = alluser.next()
                    if (currentCursor["_id"] == userId or len(currentCursor["mentee"]) == 0 or currentCursor["mentee"]["interest"] is not None):
                        continue
                    listOfReturnUser.append(currentCursor)
                    currentNumberOfUser += 1
            except StopIteration:
                print("STop Iteration")
        else:
            mentorInterest = mentorProfile["mentor"]["interest"]
            try:
                while(currentNumberOfUser < totalUserReturn):
                    currentUserCursor = alluser.next()
                    if (currentUserCursor["_id"] != userId and len(currentUserCursor["mentee"]) > 0 and currentUserCursor["mentee"]["interest"] is not None):
                        if (any(item in currentUserCursor["mentee"]["interest"] for item in mentorInterest)):
                            listOfReturnUser.append(currentUserCursor)
                    else:
                        continue
            except StopIteration:
                print("asdfasdf")
                if (len(listOfReturnUser) < totalUserReturn):
                    try:
                        alluser = GuruMatchDatabase.DATABASE["user-db"].find()
                        while( currentNumberOfUser < totalUserReturn):
                            # TODO make sure to add new user at end if there is less mentee matched
                            # have to start from the beginning with find()
                            currentUserCursor = alluser.next()
                            if (currentUserCursor["_id"] != userId and len(currentUserCursor["mentee"]) > 0 and currentUserCursor["mentee"]["interest"] is not None):
                                listOfReturnUser.append(currentUserCursor)
                                currentNumberOfUser += 1
                    except StopIteration:
                        pass
        return listOfReturnUser

GuruMatchDatabase.initialize()
#print(GuruMatchDatabase.isUsernameExist("633d25d5"))
#GuruMatchDatabase.insertNewUser({"_id": "1345234ee", "name": "David Beckham"})
#GuruMatchDatabase.insertUserForm("1345234ee", {"profile.username": "Kicker", "profile.userBio": "I am soccer player"})
#print(GuruMatchDatabase.getUserProfile("608888188def3a0ceded6f12"))
#608895309e12f61b99d44169
#")))
print("final : ", GuruMatchDatabase.getMatchMentors("60944967595c0ef62c396663"))

        






