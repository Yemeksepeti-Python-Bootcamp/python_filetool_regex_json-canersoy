from dbOperations import dbOperations
from userOperations import userOperations
from initOperations import initOperations

#Init args object and get system args from command line
initOp = initOperations()
initOp.initArgsObjAndGetSysArgs()

"""
ASSIGN tableId, json_file and db_file
"""
#Generate a tableId str of current date and time (Ex: user_20012022_015633)
tableId = initOp.generateTableId()
#Get json and db file path from system args
json_file = initOp.getJsonFilePath()
db_file = initOp.getDbFilePath()

#Init dbOp object from dbOperations class and call connectDbAndCreateTable method
dbOp = dbOperations(db_file,tableId)
dbOp.connectDbAndCreateTable()

#Init userOp object from userOperations class and call readJsonAndInsertUserData method
userOp = userOperations(json_file,db_file,tableId)
userOp.readJsonAndInsertUserData()