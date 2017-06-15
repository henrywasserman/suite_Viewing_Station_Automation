# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish
import __builtin__

from tables import Tables
from inprocess import InProcess
from consumablewastemanagementdialog import ConsumableWasteManagementDialog
from openmodedialog import OpenModeDialog
from config import Config

class SpriteCanvas(Tables):
    
    def __init__(self):
        version = Config().version
        self.accession_numbers = []
        self.inprocess = InProcess()
        self.sprite_object_symbol = ":Analyzer Simulator_SpriteCanvas"
        self.accession_number_symbol = ":Bloodhound™ Viewing Station " + version + ".Accession #:_JTextField"
        self.viewing_station_symbol = ":Bloodhound™ Viewing Station " + version + "_JTabbedPane"
        self.openmodedialog = OpenModeDialog()
        
        self.emptyrack_position_1 = [330,177]
        self.emptyrack_position_2 = [330,202]
        self.emptyrack_position_3 = [330,228]
        
        self.finishedrack_position_1 = [851,179]
        self.finishedrack_position_2 = [851,205]
        self.finishedrack_position_3 = [850,230]
        
        self.sample_2 = [958,55]
    
    def clickTab(self):
        inprocess = InProcess()
        inprocess.clickTab()
        
    def resetAccessionNumbers(self):
        self.accession_numbers = []
    
    def selectAnalyzerSimulator(self):
        squish.waitForObject(self.sprite_object_symbol).getTopLevelAncestor().toFront()
    
    def moveObject(self,from_x,from_y,to_x,to_y):
        squish.mouseClick(self.sprite_object_symbol,from_x,from_y, 0, squish.Button.Button1 )
        self.dragObject(from_x, from_y, to_x, to_y)
        
    def moveObjectAndSetAccessionNumber(self,from_x,from_y,to_x,to_y):
        squish.mouseClick(self.sprite_object_symbol,from_x,from_y, 0, squish.Button.Button1 )
        accession_number = self.setAccessionNumber(from_x, from_y)
        self.dragObject(from_x, from_y, to_x, to_y)
        return accession_number
        
    def dragObject(self,from_x,from_y,to_x,to_y):
        squish.mousePress(self.sprite_object_symbol,from_x,from_y,squish.Button.Button1)
        squish.mouseMove(self.sprite_object_symbol,to_x,to_y)
        squish.mouseRelease(self.sprite_object_symbol,to_x,to_y,squish.Button.Button1)
        squish.mouseClick(self.sprite_object_symbol,to_x,to_y,0,squish.Button.Button1)

    def runSampleRack(self):
        squish.mouseClick(self.sprite_object_symbol,18,325,0,squish.Button.Button1)
        squish.mousePress(self.sprite_object_symbol,18,325,squish.Button.Button1)
        squish.mouseRelease(self.sprite_object_symbol,18,325,squish.Button.Button1)
        squish.mouseClick(self.sprite_object_symbol,18,325,0,squish.Button.Button1)
        
    def runSampleRackOnSecondAnalyzer(self):
        squish.mouseClick(self.sprite_object_symbol,18,722,0,squish.Button.Button1)
        squish.mousePress(self.sprite_object_symbol,18,722,squish.Button.Button1)
        squish.mouseRelease(self.sprite_object_symbol,18,722,squish.Button.Button1)
        squish.mouseClick(self.sprite_object_symbol,18,722,0,squish.Button.Button1)
        
    def clickOnSTATDrawer(self):
        squish.mouseClick(self.sprite_object_symbol,370,344,0,squish.Button.Button1)
        squish.mousePress(self.sprite_object_symbol,370,344,squish.Button.Button1)
        squish.mouseRelease(self.sprite_object_symbol,370,344,squish.Button.Button1)
        squish.mouseClick(self.sprite_object_symbol,370,344,0,squish.Button.Button1)
        
    def clickOnObject(self, x,y):
        squish.mouseClick(self.sprite_object_symbol,x,y,0,squish.Button.Button1)
                
    def addMisreadToASample(self,x,y):
        self.moveObjectAndSetAccessionNumber(x,y,1282,19)
        self.moveObject(1282,19,x,y)
        
    def addFailFailToASample(self,x,y):
        self.moveObjectAndSetAccessionNumber(x,y,1282,194)
        self.moveObject(1282,194,x,y)
        
    def clickOpenPortButton(self):
        #We have to 'click' this twice only with squish 
        #for the Open Mode Dialog to appear
        self.clickOnObject(568,347)
        self.clickOnObject(568,347)
        
    def proceedToRunSampleInOpenMode(self,location):
        (x,y) = location
        #Move the sample onto the Open Port Tube
        self.moveObject(x,y,554,374)
        
        #Finally Move the sample off of the Open Port Tube
        accession_number = self.moveObjectAndSetAccessionNumber(554,374,254,374)
        
        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        self.openmodedialog.clickCancelButton()

        return accession_number
    
    def runSampleInOpenModeAndSimulateBarcode(self,barcode_number,x_list,y=0):
        self.selectAnalyzerSimulator()
        
        #This allows us to send in a list for x-y if we want to.
        if isinstance(x_list,list):
            x = x_list[0]
            y = x_list[1]
        else:
            x = x_list
        
        #Click on the Open Port Tube
        #Until the Open Mode Dialog Appears
        counter = 0
        while (True):
            self.clickOnObject(568,347)
            counter += 1
            squish.snooze(1.0)
            if object.exists(self.accession_number_symbol):
                break
            if counter == 500:
                break
        
        #This extra little click on the Open Port Tube
        #Brings back the disappearing Tube - only needed for automation
        self.clickOnObject(568,347)
        
        #Type accession_number into Open Mode dialog box.
        self.openmodedialog.setAccessionNumberEditBox(barcode_number)
        
        #Click on the Proceed Button
        self.openmodedialog.clickProceedButton()

        #Move the sample onto the Open Port Tube
        self.moveObject(x,y,554,374)
        
        #Finally Move the sample off of the Open Port Tube
        self.moveObject(554,374,254,374)
        
        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        self.openmodedialog.clickCancelButton()    
                
    def runSampleInOpenMode(self,x,y):
        self.selectAnalyzerSimulator()
        #Click on the Open Port Tube
        #Until the Open Mode Dialog Appears
        counter = 0
        while (True):
            self.clickOnObject(568,347)
            counter += 1
            squish.snooze(1.0)
            if object.exists(self.accession_number_symbol):
                break
            if counter == 500:
                break
        
        #Move a sample onto the Bar Code Reader X
        #This extra little click on the Open Port Tube
        #Brings back the disappearing Tube - only needed for automation
        self.clickOnObject(568,347)
        
        #Now move a sample onto the barcode reader X
        self.moveObject(x,y,666,376)

        #Move the sample onto the Open Port Tube
        self.moveObject(666,376,554,374)
        
        #Finally Move the sample off of the Open Port Tube
        accession_number = self.moveObjectAndSetAccessionNumber(554,374,254,374)
        
        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        self.openmodedialog.clickCancelButton()
        
        return accession_number
    
    def scanCleaningSolution(self):
        self.moveObject(1238,344,666,376)
        self.moveObject(666,376,957,428)
        
    def runSampleInOpenModeAfterClickingOnMaintenanceTab(self,x,y):
        self.selectAnalyzerSimulator()
        #Click on the Open Port Tube
        #Until the Open Mode Dialog Appears
        #counter = 0
        #while (True):
        self.clickOnObject(568,347)
            #counter += 1
        squish.snooze(1.0)
            #if object.exists(self.accession_number_symbol):
            #    break
            #if counter == 500:
            #    break
        
        #Move a sample onto the Bar Code Reader X
        #This extra little click on the Open Port Tube
        #Brings back the disappearing Tube - only needed for automation
        self.clickOnObject(568,347)
        
        #Now move a sample onto the barcode reader X
        self.moveObject(x,y,666,376)

        #Move the sample onto the Open Port Tube
        self.moveObject(666,376,554,374)
        
        #Finally Move the sample off of the Open Port Tube
        self.moveObject(554,374,254,374)

        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        self.openmodedialog.clickCancelButton()
        
    def runSampleInOpenModeOnSecondAnalyzer(self,x,y):
        self.selectAnalyzerSimulator()
        #Click on the Open Port Tube
        #Until the Open Mode Dialog Appears
        counter = 0
        while (True):
            self.clickOnObject(568,747)
            counter += 1
            squish.snooze(1.0)
            if object.exists(self.accession_number_symbol):
                break
            if counter == 500:
                break
        
        #Move a sample onto the Bar Code Reader X
        #This extra little click on the Open Port Tube
        #Brings back the disappearing Tube - only needed for automation
        self.clickOnObject(568,747)
        
        #Now move a sample onto the barcode reader X
        self.moveObject(x,y,666,776)

        #Move the sample onto the Open Port Tube
        self.moveObject(666,776,554,774)
        
        #Finally Move the sample off of the Open Port Tube
        self.moveObjectAndSetAccessionNumber(554,774,254,774)
        
        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        self.openmodedialog.clickCancelButton()
    
    def reRunSampleInOpenMode(self,x,y):
        self.selectAnalyzerSimulator()
        #Click on the Open Port Tube
        #Until the Open Mode Dialog Appears
        counter = 0
        while (True):
            self.clickOnObject(568,747)
            counter += 1
            squish.snooze(1.0)
            if object.exists(self.accession_number_symbol):
                break
            if counter == 500:
                break
        
        #Move a sample onto the Bar Code Reader X
        #This extra little click on the Open Port Tube
        #Brings back the disappearing Tube - only needed for automation
        self.clickOnObject(568,747)
        
        #Now move a sample onto the barcode reader X
        self.moveObject(x,y,665,775)

        #Move the sample onto the Open Port Tube
        self.moveObject(666,776,554,775)
        
        #Finally Move the sample off of the Open Port Tube
        self.moveObjectAndSetAccessionNumber(554,775,233,775)
        
        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        self.openmodedialog.clickCancelButton()


    def runOneSampleInStatDrawer(self, x,y):
        self.selectAnalyzerSimulator()
        self.clickOnStatDrawerDropDown()
        
        #Move the sample into the Stat drawer
        
        self.moveObject(x,y,427,377)
        
        #Click on the Stat Drawer Drop Down
        self.clickOnSTATDrawer()
        
    def runSamplesInStatDrawer(self, locations = ''):
        self.selectAnalyzerSimulator()
        self.clickOnStatDrawerDropDown()
        
        #Move Three samples into the Stat drawer
        
        if locations == '':
            self.moveObject(956,54,427,377)
            self.moveObject(956,54,468,377)
            self.moveObject(956,54,507,377)
        else:
            self.moveObject(locations[0],locations[1],427,377)
            self.moveObject(locations[2],locations[3],468,377)
            self.moveObject(locations[4],locations[5],507,377)

        
        #Click on the Stat Drawer Drop Down
        self.clickOnSTATDrawer()
        
        #If you can see the dragEpisode the STAT tray has dropped.
        self.waitForSTATTrayToDrop()
        
        #Go Back to Analyzer simulator
        self.selectAnalyzerSimulator()
        
        #Move the Three Samples off of the Stat drawer
        self.moveObjectAndSetAccessionNumber(427,377,25,377)
        self.moveObjectAndSetAccessionNumber(468,377,50,377)
        self.moveObjectAndSetAccessionNumber(507,377,75,377)
        
        #Click on the Stat Drawer Drop Down to
        #Return tray to its original position
        self.clickOnSTATDrawer()
        
    def bringToFront(self):
        squish.waitForObject(self.sprite_object_symbol).getTopLevelAncestor().toFront()
        
    def waitForSTATTrayToDrop(self):
        self.waitForAccessionNumber(427,377)
        
    def waitForSecondAnalyzerRackToFinish(self):
        self.waitForAccessionNumber(883,566)
        
    def waitForFirstAnalyzerRackToFinish(self):
        self.waitForAccessionNumber(850,178)
        
    def setAccessionNumber(self,from_x,from_y):
        accession_number = self.getAccessionNumber(from_x,from_y)
        self.accession_numbers.append(accession_number)
        return accession_number
        
    def getSampleLocationByAccessionNumber(self,accession_number):
        #Right now just checking for the samples in the first finished rack of 10
        #we will enhance this functionality later when we need to
        
        found_location = []
        
        finished_rack_of_ten = [
            [907,178],
            [907,205],
            [907,230],
            [907,257],
            [907,283],
            [882,164],
            [882,190],
            [883,217],
            [882,241],
            [883,268]
        ]
        
        for sample_location in finished_rack_of_ten:
            if accession_number == self.getAccessionNumber(sample_location[0],sample_location[1]):
                found_location = sample_location
                break
        return found_location

    def getAccessionNumberFromAFinishedRack(self):
        mouse_position = []
        
        while(True):
            mouse_position = [829,164]
            accession_number = self.getAccessionNumber(mouse_position[0],mouse_position[1])
            if not accession_number.isdecimal():
                break
        
            mouse_position = [852,178] 
            accession_number = self.getAccessionNumber(mouse_position[0],mouse_position[1])
            if not accession_number.isdecimal():
                break

            mouse_position = [829,191]                
            accession_number = self.getAccessionNumber(mouse_position[0],mouse_position[1])
            if not accession_number.isdecimal():
                break
            
            mouse_position = [850,204]                
            accession_number = self.getAccessionNumber(mouse_position[0],mouse_position[1])
            if not accession_number.isdecimal():
                break

            mouse_position = [828,218]                
            accession_number = self.getAccessionNumber(mouse_position[0],mouse_position[1])
            if not accession_number.isdecimal():
                break

            mouse_position = [851,231]                
            accession_number = self.getAccessionNumber(mouse_position[0],mouse_position[1])
            if not accession_number.isdecimal():
                break            
            
            break

        return mouse_position
        
    def getAccessionNumber(self,from_x,from_y):
        counter = 0
        
        while(True):
            self.selectAnalyzerSimulator()
            sprite = squish.findObject(self.sprite_object_symbol)
            squish.mouseClick(self.sprite_object_symbol,from_x,from_y, 0, squish.Button.Button1)
            field = sprite.getClass().getDeclaredField("dragEpisode")
            field.setAccessible(True)
            grab_drag_episode = field.get(sprite)
            counter += 1
            if counter == 300:
                break
        
            if str(grab_drag_episode) == '<null>':
                squish.snooze(1.0)
                continue
            else:
                break
        
        field2 = grab_drag_episode.getClass().getDeclaredField("dragging")
        field2.setAccessible(True)
        dragging = field2.get(grab_drag_episode)
        accession_number = dragging.toString().split(" ")[0]
        return accession_number        
        
    def clickOnStatDrawerDropDown(self):
        #Click on the Stat Drawer Drop Down
        self.clickOnObject(368,344)
    
    def waitForAccessionNumber(self,x,y):
        #We can tell the STAT tray has dropped when the mouse pointer
        #returns an accession number
        self.selectAnalyzerSimulator()
        sprite = squish.findObject(self.sprite_object_symbol)
        counter = 0
        while (True):
            counter += 1
            if counter == 300:
                test.fail("Tray did not drop after 5 minutes")
                break

            squish.mouseClick(self.sprite_object_symbol,x,y, 0, squish.Button.Button1 )
            field = sprite.getClass().getDeclaredField("dragEpisode")
            field.setAccessible(True)
            grab_drag_episode = field.get(sprite)
            if str(grab_drag_episode) == '<null>':
                counter += 1
                squish.snooze(1.0)
                continue
            else:
                break
            
    def runARackOfTen(self):
        inprocess = InProcess()
        
        self.selectBloodhoundViewingStation()
        total_samples = inprocess.getTotalNumberOfSamples()
    
        test.log("Select The Analyzer Simulator")
        self.bringToFront()
        self.selectAnalyzerSimulator()
    
        test.log("Move the Rack into the belt")
        self.moveObject(1235,26,324,161)
        test.log("Run the sample")
        self.runSampleRack()
        
        test.log("Wait for one rack of 10 samples to finish also acknowledge or hide any of the Analyzer Event Dialog Boxes that appear.")
        inprocess.waitForRackToFinish(total_samples)
        Tables.waitForTableStatusReadyForReleaseOrAwaitingReview(self, inprocess.table_symbol)
        
    def moveEmptyRackToTheBelt(self):
        test.log("Move the Empty Rack into the belt")
        self.moveObject(1174,28,323,162)
        
        
    def moveEmptyRackToSecondAnalyzer(self):
        test.log("Move the Empty Rack into the belt of second analyzer")
        self.moveObject(1174,27,323,562)
        
    #x and y is the mouse position of where original sample lives
    def takeSampleFromAFinishedRackAndRunInSecondAnalyzer(self,x,y):
        self.reRunSampleInOpenMode(x, y)
        
    def clickFluidicEjectButton(self):
        squish.mouseClick(self.sprite_object_symbol,917,88,0,squish.Button.Button1)
        squish.mousePress(self.sprite_object_symbol,917,88,squish.Button.Button1)
        squish.mouseRelease(self.sprite_object_symbol,917,88,squish.Button.Button1)
        squish.mouseClick(self.sprite_object_symbol,917,88,0,squish.Button.Button1)        
                
    def removeReagentPack(self):
        self.moveObject(691,107,1228,648)
        
    def removeSystemWash(self):
        self.moveObject(755,97,1229,725)
                
    def scanAndReplaceReagentPack(self):
        self.moveObject(1234,386,668,379)
        self.moveObject(668,379,679,105)
        return self.getLotNumberFromConsumableWasteManagementDialog(0)
        
    def scanAndReplaceSystemWash(self):
        self.moveObject(1157,385,666,376)
        self.moveObject(666,376,755,97)
        return self.getLotNumberFromConsumableWasteManagementDialog(1)
                
    def closeTheFluidicsDrawer(self):
        squish.mouseClick(self.sprite_object_symbol,917,88,0,squish.Button.Button1)
        squish.mousePress(self.sprite_object_symbol,917,88,squish.Button.Button1)
        squish.mouseRelease(self.sprite_object_symbol,917,88,squish.Button.Button1)
        squish.mouseClick(self.sprite_object_symbol,917,88,0,squish.Button.Button1)        
        self.clickOnObject(917,89)
        
    def getLotNumberFromConsumableWasteManagementDialog(self,row):
        table_symbol = getattr(ConsumableWasteManagementDialog(),"table_symbol")
        Tables.populateTableData(self,table_symbol)
        table_data = Tables.getTableData(self)
        lot_number = table_data[row]["Lot Number"]
        return lot_number
            
    def scanSampleAndSetAccessionNumber(self,from_x,from_y, to_x, to_y):
        #Move a sample to the barcode reader
        self.moveObjectAndSetAccessionNumber(from_x,from_y,665,375)
        #Move sample off the barcode reader
        self.moveObject(665,375, to_x, to_y)

    def scanSample(self,from_x,from_y, to_x, to_y):
        #Move a sample to the barcode reader
        self.moveObject(from_x,from_y,665,375)
        #Move sample off the barcode reader
        self.moveObject(665,375, to_x, to_y)
        
    def selectBloodhoundViewingStation(self):
        squish.waitForObject(self.viewing_station_symbol).getTopLevelAncestor().toFront()

    def getMousePosition(self):
        sprite = findObject(self.sprite_object_symbol)
        return sprite.getMousePosition()
    
