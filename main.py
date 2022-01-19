from configOperations import configOperations
from dbOperations import dbOperations

#Init configOp object from configOperations class and call readConfig method
configOp = configOperations()
config = configOp.readConfig()

#Init dbOp object from dbOperations class and call connectDbAndCreateTable method
dbOp = dbOperations(config)
dbOp.connectDbAndCreateTable()