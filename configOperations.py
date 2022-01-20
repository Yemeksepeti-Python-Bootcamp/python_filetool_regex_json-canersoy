import configparser

class configOperations:
    #Init configOperations class with instance of config as ConfigParser object and configDict as dict
    def  __init__(self):
        self.config = configparser.ConfigParser()
        self.configDict = {}

    def readConfig(self):
        #Reads dbconfig.ini file
        self.config.read('config.ini')

        #Loops through each section in db.config file
        for sections in self.config:
            #Adds section name and section data into configDict (Ex: {'DEFAULT': {'db_file': '"dataregex.db"'}})
            self.configDict[sections] = {k:v for k, v in self.config[sections].items()}

        #Returns configDict
        return self.configDict

  