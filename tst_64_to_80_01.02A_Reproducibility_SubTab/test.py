# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    try:
        test.log("Reproducibility SubTab")
    
        step_counter = 64
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup("SIMULATED_SLOW")
        
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.spritecanvas.selectAnalyzerSimulator()
        
        shared.spritecanvas.runSampleInOpenMode(957,20)
        accession_number1 = getattr(shared.spritecanvas,"accession_numbers")[0]
        
        shared.spritecanvas.runSampleInOpenMode(957,20)
        accession_number2 = getattr(shared.spritecanvas,"accession_numbers")[1]
        shared.spritecanvas.moveObject(254,374,224,374)
        
        shared.selectBloodhoundViewingStation()
    
        #QC > Reproducibility subtab
        
        #64. Go to the QC > Overview subtab and under the "New control on <analyzer>" header in the toolbar, click the "Reproducibility" button            
        #Confirm that the "New Reproducibility Test" dialog is displayed            
        #Confirm that the "Analyzer" field contains the analyzer that you are testing on            
        #Confirm that the "Barcode" field is empty
        #Confirm that the "Repeat Count" field with a default value of "20"
        #Confirm that the "Isolate sample" checkbox has a check in it
        #Confirm that the "Run Profile" combobox has a default value of "Default"
                    
        #Confirm that the "Include retic slide" checkbox does NOT have a check in it            "(R) There's also an “include retic slide” option now.
        #03/10/14 JJ - Confirm added."
        
        #Confirm that there are "Cancel" and "New" buttons
                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.reproducibilitytab.clickTab()
        shared.reproducibilitytab.clickReproducibilityButton()        
        #Confirm that the "New Reproducibility Test" dialog is displayed
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmDialogAppears()        
        #Confirm that the "Analyzer" field contains the analyzer that you are testing on
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmAnalyzerField()        
        #Confirm that the "Barcode" field is empty
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmBarcodeFieldIsEmpty()
        #Confirm that the "Repeat Count" field with a default value of "20"
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmRepeatCountField(20)
        #Confirm that the "Isolate sample" checkbox has a check in it
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmIsolateSampleCheckBox("selected")
        #Confirm that the "Run Profile" combobox has a default value of "Default"
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmRunProfileComboBox("Default")
        #Confirm that the "Include retic slide" checkbox does NOT have a check in it            "(R) There's also an “include retic slide” option now.
        #03/10/14 JJ - Confirm added."
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmIncludeReticSlideCheckbox("not-selected","Include retic slide")
        #Confirm that there are "Cancel" and "New" buttons
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmCancelAndNewButtonsExist()
        
        #65.  Scan the barcode of one of the blood samples that was run through the analyzer at the beginning of this test that was processed without any problems            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.scanSample(253,376, 253,376)
        accession_number1 = getattr(shared.spritecanvas,"accession_numbers")[0]
        
        #66. Change the value in the "Repeat Count" field to some value less than "20" but greater than "5", it can be any value but is should be something small, for the purposes of this test we'll use "5".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.reproducibilitytab.newreproducibilitytestdialog.setRepeatCountField("5")
        
        #67. Click the "New" button            
        #"Confirm that the ""Barcode Matches Active Control"" dialog is displayed with the following message:
        #Barcode ''<barcode>"" is an active sample in the In Process screen. Registering this barcode will cause any new runs of that sample to appear as a Reproducibility test. Are you sure you want to continue?"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.reproducibilitytab.newreproducibilitytestdialog.clickNewButton()
        #"Confirm that the ""Barcode Matches Active Control"" dialog is displayed with the following message:
        #Barcode ''<barcode>"" is an active sample in the In Process screen. Registering this barcode will cause any new runs of that sample to appear as a Reproducibility test. Are you sure you want to continue?"        
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmBarcodeMatchesActiveControlMessageBoxText(accession_number1)
    
        #68. Click the "OK" button            
        #Confirm that the "Barcode Matches Active Control" dialog closes            
        #Confirm that the "New Reproducibility Test" closes                
        #Confirm that you are now in the QC > Reproducibility subtab                
        #Confirm that the barcode specified in the dialog is now displayed in the Control Selector combobox
        #Confirm that the "Awaiting first run" message is displayed to the right of the Control Selector combobox
        #Confirm that the "Pending" message is displayed below the Control Selector combobox            
        #Confirm that the "0 Failures" message is displayed below the Control Selector combobox, under the "Pending" message
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.reproducibilitytab.newreproducibilitytestdialog.clickBarcodeMatchesActiveControlOKButton()
        test.log("Have to click the cancel button here because of Mantis bug 0013352 [Open Port] The Open Mode dialog doesn't close when it times out")
        shared.spritecanvas.openmodedialog.clickCancelButton()
    
        #Confirm that the "Barcode Matches Active Control" dialog closes
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmBarcodeMatchesActiveControlMessageBoxCloses()
        #Confirm that the "New Reproducibility Test" closes
        shared.reproducibilitytab.newreproducibilitytestdialog.confirmDialogCloses()
        #Confirm that you are now in the QC > Reproducibility subtab
        shared.qctab.confirmQCTabIsSelected()
        #Confirm that the barcode specified in the dialog is now displayed in the Control Selector combobox
        shared.qctab.confirmBarControlComboBoxItemSelected(accession_number1)
        #Confirm that the "Awaiting first run" message is displayed to the right of the Control Selector combobox
        shared.qctab.confirmAwaitingFirstRunLabel("Awaiting first run")        
        #Confirm that the "Pending" message is displayed below the Control Selector combobox
        shared.qctab.confirmPendingLabel("Pending")
        #Confirm that the "0 Failures" message is displayed below the Control Selector combobox, under the "Pending" message
        shared.qctab.confirmFailureLabel("0 failures")
    
        #69. Click on the Control Selector combobox            
        #Confirm the barcode is displayed in bold and has a checkmark to the left of the value            
        #"Process Reproducibility sample
        #For the next set of Reproducibility tests, read and understand ALL the steps below before starting. This is the part of the test that requires that the hood of the analyzer be up (see Pre-Requisite section) and using a piece of paper to produce failures"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickControlComboBox() 
        #Confirm the barcode is displayed in bold and has a checkmark to the left of the value
        test.vp("combobox")
        test.log("Process Reproducibility sample")
        #For the next set of Reproducibility tests, read and understand ALL the steps below before starting. This is the part of the test that requires that the hood of the analyzer be up (see Pre-Requisite section) and using a piece of paper to produce failures"
    
        #70. Take the blood tube with the Reproducibility barcode, put it on a rack and run it through the analyzer
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.moveEmptyRackToTheBelt()
        
    #    #1. Drag tube to the Pass generator
    #    shared.spritecanvas.moveObject(254,374,1297,159)
    #    #2. Drag tube to the missread generator
    #    shared.spritecanvas.moveObject(1297,159,1296,17)
    #    #3. Drag tube to the Pass generator
    #    shared.spritecanvas.moveObject(1296,17,1297,159)
    #    #4. Drag tube to the missread generator
    #    shared.spritecanvas.moveObject(1296,159,1296,17)
    #    #5.Drag tube to the Pass generator
    #    shared.spritecanvas.moveObject(1296,17,1296,159)    
        
        #Place tube on the rack.
        #shared.spritecanvas.moveObject(1296,159,329,177)
        shared.spritecanvas.moveObject(254,374,329,177)
        shared.spritecanvas.runSampleRack()
        
        #71. Go to the In Process screen, while running the next steps, watch the progress of each of the Reproducibility runs            
        #Confirm that the details of each run are listed in the sidebar to the right in the format; "Results 1 of 5", "Results 2 of 5", etc… up to "Results 5 of 5"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        shared.inprocess.waitToClickOnTableRowByName("Name", "(Reproducibility test)")
        shared.inprocess.waitForSidebarTextResults()
        test.log("Now wait for every row to contain Ready For Release")
        shared.inprocess.waitForTableStatusReadyForRelease()
        
        test.log("TODO: for now, due to simulator limitations all five runs are passing - verifying accordingly")
        
        #72. When run #2 reaches the Low Magnification station, hold a piece of paper between the sensor and the slide until it fails            
        #Confirm an error message is displayed on the cVS            
        #"Confirm after the failure, under the ""Individual run status"" in the sidebar, a new 2nd re-run entry is added for Results 2 of 5
        #NOTE: This second run may occur later"            "(R) We don't actually make any requirements about when the analyzer does the rerun, just that it should do it before moving on to the next sample. So, for example, it would be fine for it to start runs 3, 4, 5 before doing the rerun of 2.
        #03/10/14 JJ - Confirm note added."
        test.log("Step #" + str(step_counter)); step_counter += 1        
        #Confirm an error message is displayed on the cVS        
        #Confirm right after the failure, under the "Individual run status" in the sidebar, a new 2nd re-run entry is added for Results 2 of 5
                
        #73. Allow run #3 to be processed
        test.log("Step #" + str(step_counter)); step_counter += 1
    
        #74. When run #4 gets to the Low Magnification station, hold a piece of paper between the sensor and the slide until it fails            
        #Confirm an error message is displayed on the cVS            
        #"Confirm after the failure, under the ""Individual run status"" in the sidebar, a new 2nd re-run entry is added for Results 4 of 5
        #NOTE: This second run may occur later"            "(R) See above.
        #03/10/14 JJ - Confirm note added."
        test.log("Step #" + str(step_counter)); step_counter += 1        
        #Confirm an error message is displayed on the cVS        
        #Confirm right after the failure, under the "Individual run status" in the sidebar, a new 2nd re-run entry is added for Results 4 of 5        
    
        #75. When the re-run of run #2 reaches the Low Magnification station, don't block it, allow it to complete processing        
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #76. When run #4 reaches the Low Magnification station, hold a piece of paper between the sensor and the slide until it fails            
        #Confirm an error message is displayed on the cVS            
        #"Confirm under the ""Individual run status"" in the sidebar, no new entry is added for Results 4 of 5
        #Note: in case of a failure, the analyzer automatically re-runs the sample. If the same run fails twice, the analyzer should not start another re-run"
        test.log("Step #" + str(step_counter)); step_counter += 1        
        #Confirm an error message is displayed on the cVS        
        #"Confirm under the ""Individual run status"" in the sidebar, no new entry is added for Results 4 of 5
        #Note: in case of a failure, the analyzer automatically re-runs the sample. If the same run fails twice, the analyzer should not start another re-run"        
        
        #77. Allow run #5 to be processed
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #78. As the runs are being processed, go to QC > Reproducibility and view the table for the test that was just run            
        #Confirm that, when each run is complete, a column is added to the table, to the right of the Target column. Each run is sorted by date, run time and mode. All runs are merged under the date header            
        #"Confirm the columns for runs #2 and #4 are blank since the  re-runs have not yet been completed
        #Note: The blank column for run #4 is only added when run #5 is complete and the column for that run is added"            
        #Confirm the values for one of the runs, look approximately correct (no or few cells with a red or yellow background)            "(R) This isn't really a “confirm”, since it's not a bug if the results are bad – it just means that something's wrong with your sample.
        #03/10/14 JJ - Removing this confirm"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.reproducibilitytab.clickTab()        
        #Confirm that, when each run is complete, a column is added to the table, to the right of the Target column. Each run is sorted by date, run time and mode. All runs are merged under the date header        
        #"Confirm the columns for runs #2 and #4 are blank since the  re-runs have not yet been completed
        #Note: The blank column for run #4 is only added when run #5 is complete and the column for that run is added"        
        #Confirm the values for one of the runs, look approximately correct (no or few cells with a red or yellow background)
        test.log("Note: all runs are passing here by default")
        table_data = shared.reproducibilitytab.populateTableData()
        test.verify("Rack 1" in table_data[0], "Confirm that the first pass was recorded in the Reproducibility Table")
        test.verify("Rack 2" in table_data[0], "Confirm that the second pass was recorded in the Reproducibility Table")
        test.verify("Rack 3" in table_data[0], "Confirm that the third pass was recorded in the Reproducibility Table")
        test.verify("Rack 4" in table_data[0], "Confirm that the fourth pass was recorded in the Reproducibility Table")
        test.verify("Rack 5" in table_data[0], "Confirm that the fifth pass was recorded in the Reproducibility Table")
        
        #79. Go back to the In Process screen and wait for all runs to complete            
        #"Confirm the Reproducibility tube is returned to the rack
        #Note: until all Reproducibility runs have been completed AND the reruns have started, the Analyzer should not put the tube back in the rack"            "(R) Not true. The tube is returned once all the first runs have completed, and all the reruns have started. So, reruns of 2 and 4 might still be in processing when the tube is returned.
        #03/10/14 JJ - Confirm updated."
        #Confirm the Reproducibility record is removed from the In Process screen            
        test.log("Step #" + str(step_counter)); step_counter += 1
        #"Confirm the Reproducibility tube is returned to the rack
        #Note: until all Reproducibility runs have been completed AND the reruns have started, the Analyzer should not put the tube back in the rack"            "(R) Not true. The tube is returned once all the first runs have completed, and all the reruns have started. So, reruns of 2 and 4 might still be in processing when the tube is returned.        
        #Confirm the Reproducibility record is removed from the In Process screen
        test.log("I have already tested that every status in this table is Ready For Release")
        test.log("With this code above shared.inprocess.waitForTableStatusReadyForRelease() step 74")
        shared.inprocess.clickTab()
    
        #80. Go to QC > Reproducibility            
        #"Confirm columns for runs #1, #2, #3 and #5 contain values
        #Note: the columns for each run are created following the numerical run order (run#1 to #5). Check the run time to tag each run"            "(R) No, the columns should be in numerical run order; if they aren't then it's a bug. What will be out of order is the completion times: run 2 will have a later completion time because it was rerun.
        #03/10/14 JJ - Confirm updated."
        #Confirm the 4th column from the right (since the 4th run failed 2 times) is blank            "(R) The time on this column should match the time the run failed (the time displayed in the error message), not when it would have completed.
        #03/10/14 JJ - Confirm updated."
        #One-Off: Immortal Reproducibility            
        test.log("Step #" + str(step_counter)); step_counter += 1
        #"Confirm columns for runs #1, #2, #3 and #5 contain values
        #Note: the columns for each run are created following the numerical run order (run#1 to #5). Check the run time to tag each run"            "(R) No, the columns should be in numerical run order; if they aren't then it's a bug. What will be out of order is the completion times: run 2 will have a later completion time because it was rerun.        
        #Confirm the column that matches the run time of run #4 (most likely the 4th column from the right) is blank        
        #QC > Whole Blood subtab
        test.log("Only checking here that there are numbers in every column.  The simulator is fast and all times are the same.")
        test.log("Fourth column is not blank due to simulator issues noted above")
        test.log("%RET #RET and HGBr are blank - Hugh has verified that this is expected behavior.")
        shared.qctab.clickTab()
        shared.reproducibilitytab.clickTab()
        shared.reproducibilitytab.confirmTableNumbers()
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()

