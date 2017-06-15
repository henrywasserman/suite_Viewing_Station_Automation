# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try:
    
        test.log("Activate DigiCount™ Normal Control")
        step_counter = 42
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.qcoverview.clickDigiCountButton()
        
        shared.newdigicountcontroldialog.simulateDigiCountScan("Normal")
        shared.spritecanvas.selectAnalyzerSimulator()
    
        sample_2 = shared.spritecanvas.sample_2
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode("S1401001N", sample_2)
        
        test.log("Run it two more times so we have 3 runs on this accession number")
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode("S1401001N", sample_2)            
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode("S1401001N", sample_2)
        
        #Activate DigiCount™ Normal Control
        
        #42. Click the Control  combobox. Select the Normal control that you just created            
        test.log("Step #" + str(step_counter)); step_counter += 1
        accession_number = shared.digicounttab.getAccessionNumberByLevel("Normal")
        test.log("What for a second for the third run to get picked up")
        snooze(1.0)
    
        #43. Click the "Activate/Edit" button            
        #Confirm that the "Activate/Edit DigiCount™ Controls" dialog opens            
        #Confirm that in the "Activate/Edit DigiCount™ Controls" dialog under the "Expires" line is the new "Usage" line with the number of runs, in this case, "3 runs"            
        #Confirm that in the "Activate/Edit DigiCount™ Controls" dialog under the "Usage" line is the new "Start" line and that it is blank            03/10/14 JJ - Updated.
        #Confirm that in the "Activate/Edit DigiCount™ Controls" dialog under the "Start" line is the new "End" line which should be blank
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.clickActivateEditButton()            
        #Confirm that the "Activate/Edit DigiCount™ Controls" dialog opens
        shared.digicounttab.activateeditdigicountcontroldialog.confirmDialogOpens()        
        #Confirm that in the "Activate/Edit DigiCount™ Controls" dialog under the "Expires" line is the new "Usage" line with the number of runs, in this case, "3 runs"
        shared.digicounttab.activateeditdigicountcontroldialog.confirmUsageText("3 runs")        
        #Confirm that in the "Activate/Edit DigiCount™ Controls" dialog under the "Usage" line is the new "Start" line and that it is blank            03/10/14 JJ - Updated.
        test.log("TODO Not sure if this is a bug or a feature.  Right now Start Date is blank until you click the Active check box")
        shared.digicounttab.activateeditdigicountcontroldialog.confirmStartDateExists()                
        #Confirm that in the "Activate/Edit DigiCount™ Controls" dialog under the "Start" line is the new "End" line which should be blank
        shared.digicounttab.activateeditdigicountcontroldialog.confirmEndDateDoesNotExist()        
    
        #44. Click on the "Active" checkbox            
        #Confirm a check mark is displayed in the "Active" checkbox            
        #"Confirm the following message is displayed:
        #<Lot#L> will be inactive and this lot will be activated
        #Where <Lot#> is the barcode of the other control
        #
        #NOTE: If there is no active Control, the message displayed is:
        #This lot will be activated"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.activateeditdigicountcontroldialog.checkActiveCheckBox()
        #Confirm a check mark is displayed in the "Active" checkbox
        shared.digicounttab.activateeditdigicountcontroldialog.confirmActiveCheckBox("checked")        
        #"Confirm the following message is displayed:
        #<Lot#L> will be inactive and this lot will be activated
        #Where <Lot#> is the barcode of the other control
        shared.digicounttab.activateeditdigicountcontroldialog.confirmWillBeActivatedMessage()
        
        #45. Click the "Save" button            
        #Confirm the Activate/Edit DigiCount™ Controls dialog closes            
        #Confirm the Normal DigiCount™ sample is now active as indicated in the message below the Control combobox            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.activateeditdigicountcontroldialog.clickSaveButton()
        #Confirm the Activate/Edit DigiCount™ Controls dialog closes
        shared.digicounttab.activateeditdigicountcontroldialog.confirmDialogClosed()
        #Confirm the Normal DigiCount™ sample is now active as indicated in the message below the Control combobox
        shared.digicounttab.confirmActiveNormalLabelExists()
        #<Lot#L> will be inactive and this lot will be activated
        #Where <Lot#> is the barcode of the other control
        shared.digicounttab.activateeditdigicountcontroldialog.confirmWillBeActivatedMessage()
    
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()

    