# -*- coding: utf-8 -*-
import shutil
import sys
import os
import subprocess
import datetime

sys.path.append('../dictdiffer')
sys.path.append('../pyjavaproperties-0.6')

sys.path.append('../shared/scripts/AnalyzerSimulator')
sys.path.append('../shared/scripts/Archives')
sys.path.append('../shared/scripts/BasicFunctionality')
sys.path.append('../shared/scripts/MainTabs/Configuration')
sys.path.append('../shared/scripts/MainTabs/InProcess')
sys.path.append('../shared/scripts/MainTabs/QC')
sys.path.append('../shared/scripts/MainTabs/Results')
sys.path.append('../shared/scripts/Review')

from src.dictdiffer import DictDiffer
from pyjavaproperties import Properties
from datetime import datetime, date, time, timedelta

def handleAnalyzerEvent(obj):
    test.log("The Analyzer JPanel has appeared")

def main():
    
    global ICONIFIED
    
    ICONIFIED = 1
    NORMAL = 0
    
    source(findFile("scripts", "AnalyzerSimulator/spritecanvas.py"))
    source(findFile("scripts", "AnalyzerSimulator/analyzereventsdialog.py"))
    source(findFile("scripts", "BasicFunctionality/users.py"))
    source(findFile("scripts", "BasicFunctionality/config.py"))
    source(findFile("scripts", "BasicFunctionality/images.py"))
    source(findFile("scripts", "BasicFunctionality/tables.py"))
    source(findFile("scripts", "MainTabs/InProcess/inprocess.py"))
    source(findFile("scripts", "MainTabs/QC/qctab.py"))
    source(findFile("scripts", "MainTabs/QC/qcoverview.py"))
    source(findFile("scripts", "MainTabs/QC/digicounttab.py"))
    source(findFile("scripts", "MainTabs/QC/populationtab.py"))
    source(findFile("scripts", "MainTabs/QC/reproducibilitytab.py"))
    source(findFile("scripts", "MainTabs/QC/wholebloodtab.py"))
    source(findFile("scripts", "MainTabs/Results/releaseactiondialog.py"))
    source(findFile("scripts", "MainTabs/Results/results.py"))
    source(findFile("scripts", "MainTabs/Archives/archives.py"))
    source(findFile("scripts", "MainTabs/Configuration/configurationtab.py"))
    source(findFile("scripts", "MainTabs/Configuration/generaltab.py"))
    source(findFile("scripts", "ReviewResults/plt.py"))
    source(findFile("scripts", "ReviewResults/rbc.py"))
    source(findFile("scripts", "ReviewResults/resultsoverview.py"))
    source(findFile("scripts", "ReviewResults/wbc.py"))
    
    config = Config()
    ##config.setProperty('data.source','SIMULATOR')
    config.setProperty('qc.server','2')
    
    qc_server = config.getProperty('qc.server')
    
    ##Load Object Map
    objectMap.load(config.workingdir + "/../objects.map");
    
    attachToApplication("ViewingStation")
    
    qcoverview = QCOverview()
    resultsoverview = ResultsOverview()
    digicounttab = DigiCountTab()
    populationtab = PopulationTab()
    reproducibilitytab = ReproducibilityTab()
    #Commenting this out for now.
    #wholebloodtab = WholeBloodTab()
    spritecanvas = SpriteCanvas()
    inprocess = InProcess()
    results = Results()
    wbc = WBC()
    releaseactiondialog = ReleaseActionDialog()
    analyzer_events_dialog = AnalyzerEventsDialog()
    archives = Archives()
    configurationtab = ConfigurationTab()
    configurationgeneraltab = ConfigurationGeneralTab()
    tables = Tables()
    
    test.log("Click on the Archives Tab")
    archives.clickTab()
    
    test.log("Start with 1/1/2012")
    start_date = date(2012, 1, 1)
    
    test.log("Go through all start dates in the year 2012")
    counter = 0
    test.log("Set the Start Month, Day and Year then click on the Search Archives Button")
    while(counter <= 365):
        #Start Day
        findObject(":Archives.Start:_JTextField").text = start_date.strftime("%m")
        #Start Month
        findObject(":Archives./_JTextField").text = start_date.strftime("%d")
        #Start Year
        findObject(":Archives./_JTextField_2").text = start_date.strftime("%Y")
        
        start_date = start_date + timedelta(days = 1)
        
        test.log("Click on the Search Archives Button")
        archives.clickSearchArchivesButton()
        counter += 1
    
    test.log("Start with 1/1/2012")
    start_date = date(2012, 1, 1)
    
    test.log("Next set the start date to 01/01/2012")
    #Start Day
    findObject(":Archives.Start:_JTextField").text = start_date.strftime("%m")
    #Start Month
    findObject(":Archives./_JTextField").text = start_date.strftime("%d")
    #Start Year
    findObject(":Archives./_JTextField_2").text = start_date.strftime("%Y")
    
    test.log("Then go through all end dates in the year 2012")
    counter = 0
    test.log("Set the Month, Day and Year then click on the Search Archives Button")
    while(counter <= 365):
        #End Day
        findObject(":Archives.End:_JTextField").text = start_date.strftime("%m")
        #End Month
        findObject(":Archives./_JTextField_3").text = start_date.strftime("%d")
        #End Year
        findObject(":Archives./_JTextField_4").text = start_date.strftime("%Y")
        
        start_date = start_date + timedelta(days = 1)
        
        archives.clickSearchArchivesButton()
        counter += 1
        
        