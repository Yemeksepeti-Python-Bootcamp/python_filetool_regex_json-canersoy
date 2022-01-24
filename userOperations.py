import json
from dbOperations import dbOperations
from collections import Counter

class userOperations:
    def __init__(self,json_file,db_file,tableId):
        self.json_file = json_file
        self.db_file = db_file
        self.jsonData = {}
        self.insertIntoQuery = ""
        self.tableId = tableId
        self.dbOp = dbOperations(db_file,tableId)

    #Read JSON file
    def __parseJsonFile(self):
        json_file = open(self.json_file)
        self.jsonData = json.load(json_file)
    
    #Dynamically create a new Insert Into query for each user in the JSON file
    #and exectute it
    def __insertUserData(self):
        for user in self.jsonData:
            self.insertIntoQuery = f"""
                INSERT INTO user_{self.tableId}
                    ("email",
                    "name_surname",
                    "emailuserlk",
                    "usernamelk",
                    "birth_year",
                    "birth_month",
                    "birth_day",
                    "country",
                    "isActive")
                VALUES
                    ("{user["email"]}",
                    "{user["profile"]["name"]}",
                    {1 if sum((Counter(user["email"])&Counter(user["username"])).values()) >= 3 else 0},
                    {1 if any(word in user["username"].lower() for word in user["profile"]["name"].lower().split()) else 0},
                    {int(user["profile"]["dob"].split("-")[0])},
                    {int(user["profile"]["dob"].split("-")[1].strip("0"))},
                    {int(user["profile"]["dob"].split("-")[2].strip("0"))},
                    "{user["profile"]["address"].split(", ")[2]}",
                    1);
                """
            self.dbOp.executeInsertIntoTableQuery(self.insertIntoQuery)
        self.dbOp.closeDB()
    
    #The main method to be called including all child modules of userOperations
    def readJsonAndInsertUserData(self):
        self.__parseJsonFile()
        self.__insertUserData()