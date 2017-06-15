import os
import commands

from pyjavaproperties import Properties

class Config:
    
    def __init__(self):
        #Get the working directory and version text file
        self.workingdir = os.getcwd()
        versiontxt = self.workingdir + "/../../../PCTR/src/version.txt"
        self.bloodhoundprops = self.workingdir + "/../../../PCTR/dist/mac/ViewingStation.app/Contents/Resources/Java/bloodhound.properties"
        self.reproducibility_dir = self.workingdir + "/../data/reproducibility"
        self.testdata_dir = self.workingdir + "/../shared/testdata"
        self.results_dir = self.workingdir + "/../data/results"
        self.expected_spreadsheet_results_dir = self.results_dir + "/expected/spreadsheets"
        self.expected_csv_result_dir = self.results_dir + "/expected/csv"
        self.wholeblood_dir = self.workingdir + "/../data/wholeblood"
        self.images_dir = self.workingdir + "/../data/images"
        self.scripts_dir = self.workingdir + "/../scripts"
        self.aut_dir = self.workingdir + "/../../../PCTR"
        self.properties = Properties()
        self.properties.load(open(self.bloodhoundprops))
           
        #Open the version text file and get the version
        with open(versiontxt,'rt') as f:
            self.version = "v" + f.read()
            self.version = self.version.rstrip()
            f.close()
       
    def getVersion(self):
        return self.version
       
    def getWorkingDir(self):
        return self.workingdir
                  
    def setProperty(self,name,value):
        #Change the data.source property to SIMULATOR
        self.properties[name] = value
        self.properties.store(open(self.bloodhoundprops,'w'))
         
    def getProperty(self,name):
        return self.properties[name]
    
    def getSystemUserName(self):
        return os.getenv('USER')