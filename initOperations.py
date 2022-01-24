from datetime import datetime
import argparse

class initOperations():
    #Init initOperations class with instance of:
    #tableId, json_file and db_file as empty str
    #argparse args object as None
    def __init__(self):
        self.tableId = ""
        self.args = None
        self.json_file = ""
        self.db_file = ""
    
    #Init args object and get sys args via command line input
    def initArgsObjAndGetSysArgs(self):
        parser = argparse.ArgumentParser() 
        parser.add_argument("--json_file", "--file", type=str, required=True)
        parser.add_argument("--db_file", "--db", type=str, required=True)
        self.args = parser.parse_args()
    
    #Assign json file path from sys args
    def getJsonFilePath(self):
        self.json_file = self.args.json_file
        return self.json_file

    #Assign db file path from sys args
    def getDbFilePath(self):
        self.db_file = self.args.db_file
        return self.db_file

    #Generate a tableId str of current date and time (Ex: user_20012022_015633)
    def generateTableId(self):
        self.tableId = datetime.now().strftime("%d%m%Y_%H%M%S")
        return self.tableId
