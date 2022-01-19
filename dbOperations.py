import sqlite3
from datetime import datetime

class dbOperations():
    #Init dbOperations class with instance of config from input dict config, 
    #con as Connection object, cur as Cursor object, 
    #tableId as str of current date and time (Ex: user_20012022_015633)
    #createTableQuery as empty str
    def __init__(self,config):
        self.config = config
        self.con = sqlite3.Connection
        self.cur = sqlite3.Cursor
        self.tableId = datetime.now().strftime("%d%m%Y_%H%M%S")
        self.createTableQuery = ""

    #Gets the .db file from config dict and connects to it via sqlite3 module
    def __connectToDB(self):
        db_file = self.config["DEFAULT"]["db_file"]
        self.con = sqlite3.connect(db_file)

    #Init the necessary query to create user table with table id
    def __initCreateTableQuery(self):
        self.createTableQuery = f"""
            CREATE TABLE user_{self.tableId} (
                user_id INTEGER PRIMARY KEY,
                email TEXT NOT NULL UNIQUE,
                name_surname TEXT NOT NULL,
                emailuserlk INTEGER NOT NULL DEFAULT 1,
                usernamelk INTEGER NOT NULL DEFAULT 1,
                birth_year INTEGER,
                birth_month INTEGER,
                birth_day INTEGER,
                country TEXT NOT NULL,
                isActive INTEGER NOT NULL DEFAULT 1
            );
        """

    #Execute the createTableQuery
    def __executeCreateTableQuery(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.createTableQuery)
        self.con.close()

    #The main method to be called including all child modules of dbOperations
    def connectDbAndCreateTable(self):
        self.__connectToDB()
        self.__initCreateTableQuery()
        self.__executeCreateTableQuery()
        



