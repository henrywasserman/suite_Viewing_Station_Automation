# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():            
    try:
        step_counter = 98
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.reproducibilitytab.clickWholeBloodButton()
        
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.scanSample(957,20,224,374)
        shared.selectBloodhoundViewingStation()
        shared.reproducibilitytab.newreproducibilitytestdialog.clickNewButton()
        
        shared.spritecanvas.runSampleInOpenMode(224,374)
        accession_number = getattr(shared.spritecanvas,"accession_numbers")[0]
        shared.selectBloodhoundViewingStation()
        
        #Process Whole Blood sample - Rack mode
        test.log("#Process Whole Blood sample - Rack mode")
        
        #98. Put the sample on a rack and run it through the analyzer
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.moveEmptyRackToTheBelt()
        shared.spritecanvas.moveObject(254,374,329,177)
        shared.spritecanvas.runSampleRack()
        
        #99. Go to the In Process screen and review the progress of the sample until it completes processing            
        #Confirm the Whole Blood record is removed from the In Process screen
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickTab()        
        #Confirm the Whole Blood record is removed from the In Process screen
        shared.inprocess.waitForTableStatusReadyForRelease()        
    
        #100. Go to the QC > Whole Blood subtab, in the Analyzer Selector combobox select the appropriate Analyzer and in the Control Selector combobox select the control that was just run            
        #Confirm that it defaults to the Table subtab            
        #Confirm that the table contains a new column for the run and the column header is today's date            
        #Confirm that the column contains a sub-column with the Analyzer the run was processed on at the top            
        #Confirm that below the analyzer name is the time the run was completed            "(R) When it was completed, not when it started.
        #3/10/14 JJ - Updated."
        #Confirm that below the run time is mode used to process the sample, in this case the mode will be "Rack"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.qctab.clickTab()
        shared.wholebloodtab.clickTab()        
        #Confirm that it defaults to the Table subtab
        shared.wholebloodtab.confirmTableTabSelected()
        #Confirm that the table contains a new column for the run and the column header is today's date
        shared.wholebloodtab.confirmTableForNewRun()        
        # Confirm that the column contains a sub-column with the Analyzer the run was processed on at the top
        shared.wholebloodtab.confirmAnalyzerFirstSubColumn("Bloodhound 1")        
        #Confirm that below the analyzer name is the time the run was completed            "(R) When it was completed, not when it started.
        shared.wholebloodtab.confirmTimeInHeader()        
        # Confirm that below the run time is mode used to process the sample, in this case the mode will be "Rack"
        shared.wholebloodtab.confirmModeInHeader("Rack")        
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
