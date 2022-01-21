from dbOperations import dbOperations
from userOperations import userOperations
from datetime import datetime
import argparse

#Init args object
parser = argparse.ArgumentParser() 
parser.add_argument("--json_file", "--file", type=str, required=True)
parser.add_argument("--db_file", "--db", type=str, required=True)
args = parser.parse_args()

#Assign json_file and db_file path taken from command line as system args
json_file = args.json_file
db_file = args.db_file

#Generates a tableId str of current date and time (Ex: user_20012022_015633)
tableId = datetime.now().strftime("%d%m%Y_%H%M%S")

#Init dbOp object from dbOperations class and call connectDbAndCreateTable method
dbOp = dbOperations(db_file,tableId)
dbOp.connectDbAndCreateTable()

#Init userOp object from userOperations class and call readJsonAndInsertUserData method
userOp = userOperations(json_file,db_file,tableId)
userOp.readJsonAndInsertUserData()