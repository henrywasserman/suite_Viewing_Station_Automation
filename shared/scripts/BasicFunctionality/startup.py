# -*- coding: utf-8 -*-
import datetime
import shutil
import sys
import os
import glob
import psutil

sys.path.append('../dictdiffer')
sys.path.append('../pyjavaproperties-0.6')

sys.path.append('../shared/scripts/AnalyzerSimulator')
sys.path.append('../shared/scripts/Archives')
sys.path.append('../shared/scripts/BasicFunctionality')
sys.path.append('../shared/scripts/MainTabs/Analyzers')
sys.path.append('../shared/scripts/MainTabs/Configuration')
sys.path.append('../shared/scripts/MainTabs/Configuration/QC')
sys.path.append("../shared/scripts/MainTabs/Configuration/Rules")
sys.path.append('../shared/scripts/MainTabs/InProcess')
sys.path.append('../shared/scripts/MainTabs/Maintenance')
sys.path.append('../shared/scripts/MainTabs/QC')
sys.path.append('../shared/scripts/MainTabs/Results')
sys.path.append('../shared/scripts/ReviewResults')

from src.dictdiffer import DictDiffer
from pyjavaproperties import Properties
from subprocess import Popen, PIPE
from config import Config

class Startup():
    
    def __init__(self,start_parameter=''):
        
        global ICONIFIED
        
        self.version = Config().version
        
        ICONIFIED = 1
        NORMAL = 0
        
        source(findFile("scripts", "AnalyzerSimulator/spritecanvas.py"))
        source(findFile("scripts", "AnalyzerSimulator/openmodedialog.py"))
        source(findFile("scripts", "BasicFunctionality/users.py"))
        source(findFile("scripts", "BasicFunctionality/config.py"))
        source(findFile("scripts", "BasicFunctionality/controls.py"))
        source(findFile("scripts", "BasicFunctionality/images.py"))
        source(findFile("scripts", "BasicFunctionality/spreadsheets.py"))
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        source(findFile("scripts", "BasicFunctionality/system.py"))
        source(findFile("scripts", "BasicFunctionality/tables.py"))
        source(findFile("scripts", "MainTabs/Analyzers/analyzereventsdialog.py"))
        source(findFile("scripts", "MainTabs/Analyzers/analyzers.py"))
        source(findFile("scripts", "MainTabs/Analyzers/cleaningsolutiondialog.py"))
        source(findFile("scripts", "MainTabs/Analyzers/consumablewastemanagementdialog.py"))
        source(findFile("scripts", "MainTabs/InProcess/createworkorderdialog.py"))
        source(findFile("scripts", "MainTabs/InProcess/inprocess.py"))
        source(findFile("scripts", "MainTabs/QC/activateeditdigicountcontroldialog.py"))
        source(findFile("scripts", "MainTabs/QC/qctab.py"))
        source(findFile("scripts", "MainTabs/QC/digicounttab.py"))
        source(findFile("scripts", "MainTabs/QC/excludedialog.py"))
        source(findFile("scripts", "MainTabs/QC/newdigicountcontroldialog.py"))
        source(findFile("scripts", "MainTabs/QC/newreproducibilitytestdialog.py"))
        source(findFile("scripts", "MainTabs/QC/newwholebloodcontroldialog.py"))
        source(findFile("scripts", "MainTabs/QC/populationtab.py"))
        source(findFile("scripts", "MainTabs/QC/qcoverview.py"))
        source(findFile("scripts", "MainTabs/QC/reproducibilitytab.py"))
        source(findFile("scripts", "MainTabs/QC/wholebloodtab.py"))
        source(findFile("scripts", "MainTabs/Results/archivesampledialog.py"))
        source(findFile("scripts", "MainTabs/Results/exportallfiledialog.py"))
        source(findFile("scripts", "MainTabs/Results/inspectcellsdialog.py"))
        source(findFile("scripts", "MainTabs/Results/printdialog.py"))
        source(findFile("scripts", "MainTabs/Results/releaseactiondialog.py"))
        source(findFile("scripts", "MainTabs/Results/results.py"))
        source(findFile("scripts", "MainTabs/Archives/archives.py"))
        source(findFile("scripts", "MainTabs/Configuration/analyzerstab.py"))
        source(findFile("scripts", "MainTabs/Configuration/configurationtab.py"))
        source(findFile("scripts", "MainTabs/Configuration/listab.py"))
        source(findFile("scripts", "MainTabs/Configuration/parameterstab.py"))
        source(findFile("scripts", "MainTabs/Configuration/QC/configurationdigicounttab.py"))
        source(findFile("scripts", "MainTabs/Configuration/QC/configurationgeneraltab.py"))
        source(findFile("scripts", "MainTabs/Configuration/QC/configurationpopulationmeanstab.py"))
        source(findFile("scripts", "MainTabs/Configuration/QC/configurationqctab.py"))
        source(findFile("scripts", "MainTabs/Configuration/QC/configurationreproducibilitytab.py"))
        source(findFile("scripts", "MainTabs/Configuration/QC/configurationwholebloodtab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationactionstab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationdeltastab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationflagstab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationlimitstab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationmessagestab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationmorphologytab.py"))
        source(findFile("scripts", "MainTabs/Configuration/Rules/configurationrulestab.py"))
        source(findFile("scripts", "MainTabs/Configuration/rulestab.py"))
        source(findFile("scripts", "MainTabs/Configuration/userstab.py"))
        source(findFile("scripts", "MainTabs/Maintenance/bootstrappopulationmeansdialog.py"))
        source(findFile("scripts", "MainTabs/Maintenance/calibrationrunstab.py"))
        source(findFile("scripts", "MainTabs/Maintenance/calibrationtab.py"))
        source(findFile("scripts", "MainTabs/Maintenance/consumablehistorytab.py"))
        source(findFile("scripts", "MainTabs/Maintenance/consumablehistoryprintdialog.py"))
        source(findFile("scripts", "MainTabs/Maintenance/closespecialsampledialog.py"))
        source(findFile("scripts", "MainTabs/Maintenance/eventlogstab.py"))
        source(findFile("scripts", "MainTabs/Maintenance/runmaintenanceactiondialog.py"))
        source(findFile("scripts", "MainTabs/Maintenance/maintenance.py"))
        source(findFile("scripts", "MainTabs/Maintenance/newspecialsampledialog.py"))
        source(findFile("scripts", "MainTabs/Maintenance/usagehistorytab.py"))
        source(findFile("scripts", "ReviewResults/plt.py"))
        source(findFile("scripts", "ReviewResults/rbc.py"))
        source(findFile("scripts", "ReviewResults/resultsoverview.py"))
        source(findFile("scripts", "ReviewResults/wbc.py"))

        #Clean out the Print Que
        
        self.user = os.environ['USER']
        self.viewing_station_symbol = ":Bloodhound™ Viewing Station " + self.version + "_JPanel"
        self.viewing_station_qc_symbol = ":QC_JComponent"
        self.impropershutdown_symbol = ":Bloodhound™ Viewing Station " + self.version + ".OK_JButton"
        self.hide_button_symbol = ":Bloodhound™ Viewing Station " + self.version + ".Hide_JButton"
        self.viewing_station_jtabbed = ":Bloodhound™ Viewing Station " + self.version + "_JTabbedPane"
        
        printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + self.user + '/*.pdf')
        for f in printerfiles:
            os.remove(f)
        
        self.config = Config()
        #config.setProperty('data.source','SIMULATOR')
        self.config.setProperty('qc.server','2')
        
        self.qc_server = self.config.getProperty('qc.server')
        
        #Load Object Map
        objectMap.load(self.config.workingdir + "/../objects.map")
        self.system = System()
                    
        if (start_parameter == 'QC'):
            startApplication("startQC.sh")
        elif(start_parameter == 'QC_SMALL_DATA_SET'):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("QC_SMALL_DATA_SET")
        elif(start_parameter == 'QC_MEDIUM_DATA_SET'):
            startApplication("startQC_medium_data_set.sh")
        elif(start_parameter == 'QC_MEDIUM_LARGE_DATA_SET'):
            startApplication("startQC_medium_large_data_set.sh")
        elif (start_parameter == "with_errors"):
            startApplication("start_with_errors.sh")
        elif (start_parameter == "start_slow"):
            startApplication("start_slow.sh")
        elif (start_parameter == "start_medium"):
            startApplication("start_medium.sh")
        elif (start_parameter == "start_display_control_debug_true"):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("START_DISPLAY_CONTROL_DEBUG_TRUE")        
        elif (start_parameter == "QC_MEDIUM_DATA_SET_ATTACH"):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("QC_MEDIUM_DATA_SET")
        elif (start_parameter == "QC_LARGE_DATA_SET_ATTACH"):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("QC_LARGE_DATA_SET")
        elif(start_parameter == "ATTACH_TO_RUNNING_STATION"):
            self.system.attachToViewingStation()
        elif(start_parameter == "SIMULATED_MEDIUM"):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("SIMULATED_MEDIUM")
        elif(start_parameter == "SIMULATED_SLOW"):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("SIMULATED_SLOW")
        elif(start_parameter == "VANILLA"):
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation("VANILLA")            
        else:
            if (self.isViewingStationRunning()):
                self.system.terminateViewingStation()
            self.system.startViewingStation()
    
        self.dismissMessageBoxes()
        
        #Create our Objects 
        self.vadim = Users('Vadim', 'and1lead')
        self.qctab = QCTab()
        
        #Login as Vadim
        self.vadim.login()
        
        #Click QC Tab
        self.qctab.clickTab()
        self.qcoverview = QCOverview()
        self.newdigicountcontroldialog = NewDigiCountControlDialog()
        self.resultsoverview = ResultsOverview()
        self.digicounttab = DigiCountTab()
        self.populationtab = PopulationTab()
        self.reproducibilitytab = ReproducibilityTab()
        #TODO Need to refactor wholebloodtab constructor
        #Should not be calling actions in constructor
        self.wholebloodtab = WholeBloodTab()
        self.spritecanvas = SpriteCanvas()
        self.inprocess = InProcess()
        self.results = Results()
        self.analyzers = Analyzers()
        self.wbc = WBC()
        self.rbc = RBC()
        self.plt = PLT()
        self.images = Images()
        self.releaseactiondialog = ReleaseActionDialog()
        #Simulator only
        self.analyzer_events_dialog = AnalyzerEventsDialog()
        self.archives = Archives()
        self.configurationtab = ConfigurationTab()
        self.analyzerstab = AnalyzersTab()
        self.listab = LisTab()
        self.configurationqctab = ConfigurationQCTab()
        self.configurationgeneraltab = ConfigurationGeneralTab()
        self.configurationdigicounttab = ConfigurationDigicountTab()
        self.configurationpopulationmeanstab = ConfigurationPopulationMeansTab()
        self.configurationreproducibilitytab = ConfigurationReproducibilityTab()
        self.configurationwholebloodtab = ConfigurationWholeBloodTab()
        self.configurationactionstab = ConfigurationActionsTab()
        self.configurationdeltastab = ConfigurationDeltasTab()
        self.configurationflagstab = ConfigurationFlagsTab()
        self.configurationlimitstab = ConfigurationLimitsTab()
        self.configurationmessagestab = ConfigurationMessagesTab()
        self.configurationmorphologytab = ConfigurationMorphologyTab()
        self.configurationrulestab = ConfigurationRulesTab()
        self.parameterstab = ParamtersTab()
        self.maintenance = Maintenance()
        self.tables = Tables()
        self.spreadsheets = SpreadSheets()
        self.factory_defaults = []
        
        #If we are in QC mode - We have to wait for data to finish loading
        if 'QC' in start_parameter:
            self.waitForQCDataToFinish()
        
    def waitForQCDataToFinish(self):
        counter = 0
        while(True):
            now = datetime.now()
            date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)[2:]
            #Wait 10 Seconds
            snooze(10.0)
            self.digicounttab.clickTab()
                
            if date in findObject(":QC.Last Run on AM_JLabel").text:
                break
            #Wait a maximum of 20 minutes
            if counter == 1200:
                break
            self.qcoverview.clickTab()
        self.qcoverview.clickTab()
                                        
    def selectBloodhoundViewingStation(self):
        waitForObject(self.viewing_station_jtabbed).getTopLevelAncestor().toFront()
        
    def setConfigLisReleaseDelay(self,seconds):
        test.log("Set the Configuration Lis-Release Delay in seconds")
        self.configurationtab.clickTab()
        self.configurationgeneraltab.clickTab()
        self.configurationgeneraltab.setLISReleaseDelay(seconds)
        
    def populateFactoryDefaultTable(self):
        self.configurationtab.clickTab()
        self.parameterstab.clickTab()
        self.parameterstab.doubleClickRow(0)
        self.factory_defaults = self.parameterstab.populateTableData()
        self.parameterstab.clickCancelButton()
        
    def isViewingStationRunning(self):
        self.viewer_running = False
        for p in psutil.process_iter():
            try:
                cmdline = str(p.cmdline)
                #test.log(cmdline)
                if "dist/mac/ViewingStation.app" in cmdline:
                    self.viewer_running = True
                    test.log(cmdline)
                    break
            except psutil.AccessDenied:
                pass        
        return self.viewer_running
    
    def bringViewingStationToTheFront(self):
        if object.exists(self.viewing_station_symbol):
            findObject(self.viewing_station_symbol).getTopLevelAncestor().toFront()
        elif object.exists(self.viewing_station_qc_symbol):
            findObject(self.viewing_station_qc_symbol).getTopLevelAncestor().toFront()

    def dismissMessageBoxes(self): 
        #Minimize LIZ Simulator
        if object.exists(":LIS Simulator_JPanel"):
            waitForObject(":LIS Simulator_JPanel").getTopLevelAncestor().setExtendedState(ICONIFIED)
        # Bring Viewing Station To The Front - Simulator Only
        if (object.exists(self.viewing_station_symbol)):
            try:
                findObject(self.viewing_station_symbol).getTopLevelAncestor().toFront()
            except:
                test.log("getTopLevelAncestor did not exist")
        
        #Remove the console by clicking on the hide button if it is there.
        if object.exists(self.hide_button_symbol):
            clickButton(findObject(self.hide_button_symbol))
        
        #If improper shutdown notice appears dismiss it
        try:
            impropershutdown = findObject(self.impropershutdown_symbol)
            if not "invalid" in impropershutdown.toString():
                clickButton(self.impropershutdown_symbol)                 
        except:
            test.log("For an unrecorded reason we could not click on the impropershutdown button, you may want to check to see if it exists or existed")
