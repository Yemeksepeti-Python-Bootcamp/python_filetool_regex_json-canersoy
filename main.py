from configOperations import configOperations
from dbOperations import dbOperations
from userOperations import userOperations
from datetime import datetime

#Init configOp object from configOperations class and call readConfig method
configOp = configOperations()
config = configOp.readConfig()

#Generates a tableId str of current date and time (Ex: user_20012022_015633)
tableId = datetime.now().strftime("%d%m%Y_%H%M%S")

#Init dbOp object from dbOperations class and call connectDbAndCreateTable method
dbOp = dbOperations(config,tableId)
dbOp.connectDbAndCreateTable()

#Init userOp object from userOperations class and call readJsonAndInsertUserData method
userOp = userOperations(config,tableId)
userOp.readJsonAndInsertUserData()