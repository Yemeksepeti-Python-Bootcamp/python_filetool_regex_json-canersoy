import sqlite3

class dbOperations():
    def __init__(self,db_file,tableId):
        self.db_file = db_file
        self.con = sqlite3.Connection
        self.cur = sqlite3.Cursor
        self.tableId = tableId
        self.createTableQuery = ""

    #Gets the .db file from config dict and connects to it via sqlite3 module
    def __connectToDB(self):
        db_file = self.db_file
        self.con = sqlite3.connect(db_file)

    #Closes the database connection    
    def closeDB (self):
        self.con.close()

    #Init the necessary query to create user table with table id
    def __initCreateTableQuery(self):
        self.createTableQuery = f"""
            CREATE TABLE user_{self.tableId} (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        self.con.commit()

    #The main method to be called including all child modules of dbOperations
    def connectDbAndCreateTable(self):
        self.__connectToDB()
        self.__initCreateTableQuery()
        self.__executeCreateTableQuery()
        self.closeDB()
    
    #Execute the insertIntoTableQuery
    def executeInsertIntoTableQuery(self,insertIntoTableQuery):
        self.__connectToDB()
        self.cur = self.con.cursor()
        self.cur.execute(insertIntoTableQuery)
        self.con.commit()
        