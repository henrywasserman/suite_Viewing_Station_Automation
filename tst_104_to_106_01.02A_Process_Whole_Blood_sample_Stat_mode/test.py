# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():            
    try:
        step_counter = 104
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup("SIMULATED_SLOW")
        #shared = Startup()
        
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.reproducibilitytab.clickWholeBloodButton()
        
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.scanSample(957,20,224,374)
        shared.selectBloodhoundViewingStation()
        shared.reproducibilitytab.newreproducibilitytestdialog.clickNewButton()
        
        shared.spritecanvas.runSampleInOpenMode(224,374)
        accession_number = getattr(shared.spritecanvas,"accession_numbers")[0]
        
        shared.spritecanvas.moveEmptyRackToTheBelt()
        shared.spritecanvas.moveObject(254,374,329,177)
        shared.spritecanvas.runSampleRack()
        shared.spritecanvas.waitForFirstAnalyzerRackToFinish()
        
        test.log("Move Empty Rack into the second Analyzer")
        shared.spritecanvas.moveEmptyRackToSecondAnalyzer()
        test.log("Move sample into rack")
        shared.spritecanvas.moveObject(850,179,330,578)
        test.log("Run the sample on the second analyzer")
        shared.spritecanvas.runSampleRackOnSecondAnalyzer()
        shared.spritecanvas.waitForSecondAnalyzerRackToFinish()

        test.log("Process Whole Blood sample - STAT mode")        
        
        #104. Go back to the 1st analyzer and run the same Whole Blood control in the STAT rack
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.runOneSampleInStatDrawer(907,579)
        
        #105. Go to the In Process screen and review the progress of the control            
        #Confirm that the sample is treated as a Whole Blood control, not a normal blood sample            
        #Confirm that when the sample completes processing, the Whole Blood record is removed from the In Process screen    
        test.log("Step #" + str(step_counter)); step_counter += 1        
        #Confirm that the sample is treated as a Whole Blood control, not a normal blood sample        
        #Confirm that when the sample completes processing, the Whole Blood record is removed from the In Process screen
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        row = shared.inprocess.waitToClickOnTableRowByName("Name", "(Whole Blood Control)")
        test.verify("(Whole Blood Control)" == row["Name"], "Confirm that the row selected contains the name: 'Whole Blood Control'")
        shared.inprocess.waitForTableStatusReadyForRelease()
        
        #106. Go to the QC > Whole Blood > Table subtab, in the Analyzer Selector combobox select the appropriate Analyzer and in the Control Selector combobox select the control that was just run            
        #Confirm that the table contains, under the same date column header, a new column for the run                    
        #Confirm that the new column is to the left of the other runs
        #Confirm that at the top of the new column is the Analyzer that the run was processed on            
        #Confirm that below the analyzer name is the time the run was processed            
        #Confirm that below the run time is mode used to process the sample; Rack, Open Port or STAT, in this case the mode will be "STAT"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.wholebloodtab.clickTab()
        shared.wholebloodtab.selectAnalyzer("Bloodhound 1")
        shared.wholebloodtab.selectControlItem(accession_number)
        #Confirm that the table contains, under the same date column header, a new column for the run
        shared.wholebloodtab.confirmNewColumn(3)        
        #Confirm that the new column is to the left of the other runs
        shared.wholebloodtab.confirmAnalyzerNames(["Bloodhound 1","Bloodhound 2","Bloodhound 1","Bloodhound 1"])
        # Confirm that at the top of the new column is the Analyzer that the run was processed on
        shared.wholebloodtab.confirmAnalyzerFirstSubColumn("Bloodhound 1")        
        # Confirm that below the analyzer name is the time the run was processed
        shared.wholebloodtab.confirmTimeInHeader()        
        # Confirm that below the run time is mode used to process the sample; Rack, Open Port or STAT, in this case the mode will be "STAT"
        shared.wholebloodtab.confirmModeInHeader("STAT")
                
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
