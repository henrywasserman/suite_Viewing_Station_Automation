# -*- coding: utf-8 -*-
import shutil
import sys
import os
import re
import exceptions
import traceback

def main():
    try:
        step_counter = 127
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.system.mountUSBDrive()
        #shared.setConfigLisReleaseDelay(6)
        
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
        
        #Get the original dilution numbers
        shared.results.clickTab()
        shared.results.clickOnFirstRowOfTable()
        shared.results.clickOpenForReviewButton()
        shared.results.overview.setCurrentDilutionNumbers()
        shared.results.clickCloseButton()
        original_dilution_numbers = getattr(shared.results.overview,"dilution_numbers")
    
        #127. Go to the In Process main tab.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickTab()
        
        #128. Under Filter by Analyzer combobox, select each one of the connected Analyzer options in the popup menu.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We are going to need an Accession number")
        shared.inprocess.populateTableData()
        accession_number = shared.inprocess.getTableData()[0]['Accession #']
        
        #129. Select option "All" in the Filter by Analyzer combo box to filter all Analyzers.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.selectFilterByAnalizerName("All")
        
        #"130. Click on the “'Create Work Order” button and review all the contents in the Create Work Order dialog:
        #-Accession Number field
        #-Recognize sample by location checkbox and its section (Analyzer combo box, Mode combo box, Rack and Position fields)
        #-Save custom slides checkbox and its section (Reviewable, Stained and Unstained fields)
        #-Normal, Retic, and Pair radio buttons under Stained and Unstained
        #-Isolate sample checkbox 
        #-Undo and Redo buttons
        #-Cancel, Edit and Save buttons"            "(N) 'Dilution' has been removed from this dialog (per spec). It is now only possible to set a dilution factor when running in open mode; the steps that follow will need to be re-worked.
        #[VM 02.27.14] - Altered steps to accommodate for the changes."
        #Confirm that all those components exist in each of the sections under the Create Work Order dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickCreateWorkOrderButton()
        shared.inprocess.createworkorderdialog.confirmAccessionNumberEditBox("enabled","")
        shared.inprocess.createworkorderdialog.confirmRecognizeSampleByLocationCheckbox("enabled","unchecked")
        shared.inprocess.createworkorderdialog.confirmAnalyzerComboBox("enabled","Bloodhound 1,Bloodhound 2")
        shared.inprocess.createworkorderdialog.confirmModeComboBox("disabled","Rack")
        shared.inprocess.createworkorderdialog.confirmRackField("not-editable","001")
        shared.inprocess.createworkorderdialog.confirmPositionField("not-editable","1")
        shared.inprocess.createworkorderdialog.confirmSaveCustomSlidesCheckbox("enabled","unchecked")
        #shared.inprocess.createworkorderdialog.confirmReviewableField("not-editable","1")
        #shared.inprocess.createworkorderdialog.confirmStainedField("not-editable","0")
        shared.inprocess.createworkorderdialog.confirmStainedNormalRadioButton("not-editable","selected")
        shared.inprocess.createworkorderdialog.confirmStainedReticRadioButton("not-editable","unselected")
        shared.inprocess.createworkorderdialog.confirmStainedPairedRadioButton("not-editable","unselected")
        shared.inprocess.createworkorderdialog.confirmUnStainedField("not-editable","0")
        shared.inprocess.createworkorderdialog.confirmUnStainedNormalRadioButton("not-editable","selected")
        shared.inprocess.createworkorderdialog.confirmUnStainedReticRadioButton("not-editable","unselected")
        shared.inprocess.createworkorderdialog.confirmUnStainedPairedRadioButton("not-editable","unselected")
        shared.inprocess.createworkorderdialog.confirmIsolateSampleCheckbox("disabled","unchecked")
        shared.inprocess.createworkorderdialog.confirmUndoButton("disabled")
        shared.inprocess.createworkorderdialog.confirmRedoButton("disabled")
        shared.inprocess.createworkorderdialog.confirmCancelButton("enabled")
        shared.inprocess.createworkorderdialog.confirmEditButton("disabled")
        shared.inprocess.createworkorderdialog.confirmSaveButton("disabled")
        shared.inprocess.createworkorderdialog.clickCancelButton()
    
        #131. Press Open Port button on the Analyzer and observe the 'Open Mode - <Analyzer_name>' dialog box appears. Confirm there is checkbox titled "Dilution: 1:".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.clickOpenPortButton()
        shared.spritecanvas.openmodedialog.confirmOpenModeDialogAppears("Bloodhound 1")
        shared.spritecanvas.openmodedialog.confirmDilution1CheckboxTitle()
        
        #132. 'Type in a barcode number that has already had its results filled in the Results Queue, check the "Dilution: 1:" checkbox, and type in "2" for the dilution text box.          
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.openmodedialog.setAccessionNumberEditBox(accession_number)
        shared.spritecanvas.openmodedialog.checkDilutionFactorCheckbox()
        shared.spritecanvas.openmodedialog.setDilutionField("2")
                
        #133. Press the Proceed button, and proceed running the sample in Open Port mode.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.openmodedialog.clickProceedButton()
        shared.spritecanvas.selectAnalyzerSimulator()
        sample_location = shared.spritecanvas.getSampleLocationByAccessionNumber(accession_number)
        shared.spritecanvas.proceedToRunSampleInOpenMode(sample_location)
    
        #134. Once the sample finished processing, open the sample up for review and observe that under the Current results column all the # results for (WBC, RBC, PLT, #nRBC, #RET, HGB, HCT) are doubled and that the dilution factor for this sample has been changed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.results.clickTab()
        shared.results.clickOnRowByAccessionNumber(accession_number)
        shared.results.clickOpenForReviewButton()
        shared.results.overview.setCurrentDilutionNumbers()
        shared.results.clickCloseButton()
        two_times_dilution_numbers = getattr(shared.results.overview,"dilution_numbers")
        test.log("TODO: Vadim and Vlad are going to decide what to do about #RET. Since it does not appear in the table, I am leaving it out for now.")
        #shared.results.confirmDilutionFactor(original_dilution_numbers,two_times_dilution_numbers,['WBC', 'RBC', 'PLT', '#nRBC', '#RET', 'HGB', 'HCT'],2)
        shared.results.confirmDilutionFactor(original_dilution_numbers,two_times_dilution_numbers,['WBC', 'RBC', 'PLT', '#nRBC', 'HGB', 'HCT'],2)
        
        #135. Now rerun the same sample again on the Analyzer.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.clickOpenPortButton()
        shared.spritecanvas.openmodedialog.setAccessionNumberEditBox(accession_number)
        shared.spritecanvas.openmodedialog.clickProceedButton()
        shared.spritecanvas.runSampleInOpenMode(252,374)
        
        #136. Observe that the third set of results in the Review page is not affected by the dilution factor '2' entered previously. Observe, the results are almost identical to original ones.
        #Confirm the Open Mode dialog box has a checkbox labeled 'Dilution: 1:'            
        #Confirm if this checkbox is checked, then the dilution factor for this sample will be changed when this sample is run on Analyzer.            
        #Confirm that dilution factor will affect all runs for which it was specified.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        shared.selectBloodhoundViewingStation()
        shared.results.clickTab()
        shared.results.clickOnRowByAccessionNumber(accession_number)
        shared.results.clickOpenForReviewButton()
        shared.results.overview.setCurrentDilutionNumbers()
        shared.results.clickCloseButton()
        third_set_of_dilution_numbers = getattr(shared.results.overview,"dilution_numbers")
        test.log("TODO: Vadim and Vlad are going to decide what to do about #RET. Since it does not appear in the table, I am leaving it out for now.")
        #shared.results.confirmDilutionFactor(original_dilution_numbers,third_set_dilution_numbers,['WBC', 'RBC', 'PLT', '#nRBC', '#RET', 'HGB', 'HCT'],2)
        shared.results.confirmDilutionFactor(original_dilution_numbers,third_set_of_dilution_numbers,['WBC', 'RBC', 'PLT', '#nRBC', 'HGB', 'HCT'],1)
    
        test.log("TODO: Sent Vlad an e-mail - checkbox is not labeled 'Dilution: 1: but rather Dilution factor: x")
        test.log("Waiting for documentation to update here, then I will make change to this doc.")    
        #Confirm the Open Mode dialog box has a checkbox labeled 'Dilution: 1:'
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.clickOpenPortButton()
        shared.spritecanvas.openmodedialog.confirmOpenModeDialogAppears("Bloodhound 1")
        shared.spritecanvas.openmodedialog.confirmDilution1CheckboxTitle()
        
        #Confirm if this checkbox is checked, then the dilution factor for this sample will be changed when this sample is run on Analyzer.
        #Confirm that dilution factor will affect all runs for which it was specified.
        shared.spritecanvas.openmodedialog.setAccessionNumberEditBox(accession_number)
        shared.spritecanvas.openmodedialog.checkDilutionFactorCheckbox()
        shared.spritecanvas.openmodedialog.setDilutionField("2")
        shared.spritecanvas.openmodedialog.clickProceedButton()
        shared.spritecanvas.selectAnalyzerSimulator()
        sample_location = shared.spritecanvas.getSampleLocationByAccessionNumber(accession_number)
        shared.spritecanvas.proceedToRunSampleInOpenMode(sample_location)
        
        shared.selectBloodhoundViewingStation()
        shared.results.clickTab()
        shared.results.clickOnRowByAccessionNumber(accession_number)
        shared.results.clickOpenForReviewButton()
        shared.results.overview.setCurrentDilutionNumbers()
        shared.results.clickCloseButton()
        fourth_set_of_dilution_numbers = getattr(shared.results.overview,"dilution_numbers")
        test.log("TODO: Vadim and Vlad are going to decide what to do about #RET. Since it does not appear in the table, I am leaving it out for now.")
        #shared.results.confirmDilutionFactor(original_dilution_numbers,third_set_dilution_numbers,['WBC', 'RBC', 'PLT', '#nRBC', '#RET', 'HGB', 'HCT'],2)
        shared.results.confirmDilutionFactor(fourth_set_of_dilution_numbers,two_times_dilution_numbers,['WBC', 'RBC', 'PLT', '#nRBC', 'HGB', 'HCT'],1)
    
        #137. Press the Create Work Order button in toolbar again and observe that in the "Save custom slides" section there is checkbox titled "Isolate sample".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickTab()
        shared.inprocess.clickCreateWorkOrderButton()
        shared.inprocess.createworkorderdialog.confirmIsolateSampleCheckbox("disabled","unchecked")
        
        #138. Note that the "Isolate sample" checkbox is unchecked when first start off.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.createworkorderdialog.confirmIsolateSampleCheckbox("disabled","unchecked")
        
        #139. Scan/type in a barcode in the barcode field and turn on the "Save custom slides"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.createworkorderdialog.setAccessionNumberEditBox(accession_number)
        shared.inprocess.createworkorderdialog.checkSaveCustonSlidesCheckbox()
        
        #140. Turn on the "Isolate sample" checkbox, set the reviewable text field to "2", and press the Save button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.createworkorderdialog.setReviewableField("2")
        shared.inprocess.createworkorderdialog.clickSaveButton()
        
        #141. Create another second similar work order as in step 136-139, place the first work order in position 1 of the rack and the second work order on position 2, and run the rack on the Analyzer.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        accession_number_2 = "4711"
        shared.inprocess.clickCreateWorkOrderButton()
        shared.inprocess.createworkorderdialog.setAccessionNumberEditBox(accession_number_2)
        shared.inprocess.createworkorderdialog.setReviewableField("2")
        shared.inprocess.createworkorderdialog.clickSaveButton()
        
        accession_location = shared.spritecanvas.getSampleLocationByAccessionNumber(accession_number)
        shared.spritecanvas.runSampleInOpenMode(accession_location[0],accession_location[1])
        
        accession_location = shared.spritecanvas.getSampleLocationByAccessionNumber(accession_number_2)
        shared.spritecanvas.runSampleInOpenModeOnSecondAnalyzer(accession_location[0],accession_location[1])
        
        #142. When the final run of the first work order reaches the low imager, block the imager so it triggers a imaging failure and then triggers an automatic rerun.    
        test.log("Step #" + str(step_counter)); step_counter += 1
    
        #143. Observe that if the "Isolate sample" checkbox is turned on, the failed sample tube will stay on the rocker until all the necessary auto reruns have started.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("TODO: Talked to Hugh about this. He seemed to think that blocking the imager was something that could")
        test.log("not be done on the simulator")
        test.log("He is going to open up an enhancement request")
        
        #144. Observe that once auto-rerun occurs the first work order sample is placed back into position 1 and the next work order will start running immediately; let the second work order pass with no rerun and see that the tube is placed back immediately to the rack.
        test.log("Step #" + str(step_counter)); step_counter += 1
     
        #145. Go back to the In Process main tab and create a work order with the same reviewable slides, but this time leave the "Isolate sample" unchecked.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #146. Place the work order in position 1 of the rack and another sample on position 2 and run the rack on the Analyzer.
        test.log("Step #" + str(step_counter)); step_counter += 1
    
        #147. When the final run of the work order reaches the low imager, block the imager so it triggers a imaging failure.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #148. Observe that this failure has no effect on the normal cadence of the Analyzer as it places the work order tube back into the rack and move onto the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #149. Observe if the "Isolated sample" checkbox is checked, then once a run of this sample begins, until there are known to be no more reruns of this sample possible, no other sample will run.            
        #Confirm under the fields a checkbox titled “Isolate sample” will appear.            
        #Confirm this checkbox will start off unchecked.            
        #Confirm if this checkbox is checked, then once a run of this sample begins, until there are known to be no more reruns of this sample possible, no other sample will run.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #150. Select a patient sample. Press the "Delete Sample" button. Press the "Cancel" button to close the Delete Sample dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.bringViewingStationToTheFront()
        shared.inprocess.clickTab()
        shared.inprocess.clickOnFirstRowOfTable()
        shared.inprocess.clickDeleteSampleButton()
        shared.inprocess.deletesampledialog.clickCancelButton()
    
        #151. Select another patient sample and press the "Edit Patient" button. Press the "Check" then "Cancel" buttons to close the Patient Information dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.populateTableData()
        shared.inprocess.clickOnTableRowIndex(1)
        shared.inprocess.clickEditPatientButton()
        shared.inprocess.patientinformationdialog.clickCheckButton()
        shared.inprocess.patientinformationdialog.clickCancelButton()
    
        #152. In the Search text field, enter the accession number of the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        accession_number = shared.inprocess.getAccessionNumberByIndex(1)
        shared.inprocess.enterSearchText(accession_number)
    
        #153. Click "Show All". To sort the samples by category, click on the Status, Name, Accession #, Medical Record #, Location, Date, Time, Turnaround time, Priority, Instrument and Mode column headers.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickShowAllButton()
        shared.inprocess.clickStatusColumnHeader()
        shared.inprocess.clickNameColumnHeader()
        shared.inprocess.clickAccessionNumberColumnHeader()
        shared.inprocess.clickMedicalRecordColumnHeader()
        shared.inprocess.clickLocationColumnHeader()
        shared.inprocess.clickDateColumnHeader()
        shared.inprocess.clickTimeColumnHeader()
        shared.inprocess.clickTurnaroundTimeColumnHeader()
        shared.inprocess.clickPriorityColumnHeader()
        shared.inprocess.clickAnalyzerColumnHeader()
        shared.inprocess.clickModeColumnHeader()
    
        #154. Go to the Results main tab.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
    
        #155. Deselect and reselect all the review levels: Initial review, Level 1, Level 2 and Level 3 for one sample.            
        #Confirm that the Results Queue Samples List displays the review level(s) accordingly to what is selected in the "Filter by review level" section.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.initialReviewCheckBox("uncheck")
        shared.results.populateTableData()
        test.verify(len(shared.results.getTableData()) == 0,"Confirm that there are zero rows in the results table")
        shared.results.initialReviewCheckBox("check")
        shared.results.populateTableData()        
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
        shared.results.level1ReviewCheckBox("uncheck")
        shared.results.populateTableData()
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
        shared.results.level1ReviewCheckBox("check")
        shared.results.populateTableData()
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
        shared.results.level2ReviewCheckBox("uncheck")
        shared.results.populateTableData()
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
        shared.results.level2ReviewCheckBox("check")
        shared.results.populateTableData()        
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
        shared.results.level3ReviewCheckBox("uncheck")
        shared.results.populateTableData()
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
        shared.results.level3ReviewCheckBox("check")
        shared.results.populateTableData()
        test.verify(len(shared.results.getTableData()) == 2,"Confirm that there are two rows in the results table")
    
        #156. Open the review page for a sample. In the Review combobox, select "Level 1 Review". Press the "Save" then "Close" buttons. A dark green flag with the value of 1 is displayed next to the Status icon for the selected sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickOpenForReviewButton()
        shared.results.selectReviewComboBox("Level 1 Review")
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        shared.results.confirmStatusIcon("greenflag_icon.png","Level 1 Review, Awaiting Review")
    
        #157. Open the review page for the selected sample. In the Review combobox, select "Level 2 Review". Press the "Save" then "Close" buttons. A light green flag with the value of 2 is displayed next to the Status icon for the selected sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickOpenForReviewButton()
        shared.results.selectReviewComboBox("Level 2 Review")
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        shared.results.confirmStatusIcon("light_greenflag_icon.png","Level 2 Review, Awaiting Review")
    
        #158. Open the review page for the selected sample. In the Review combobox, select "Level 3 Review". Press the "Save" then "Close" buttons. A orange flag with the value of 3 is displayed next to the Status icon for the selected sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickOpenForReviewButton()
        shared.results.selectReviewComboBox("Level 3 Review")
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        shared.results.confirmStatusIcon("orangeflag_icon.png","Level 3 Review, Awaiting Review")
    
        #159. Open the review page for the selected sample. In the Review combobox, select "Initial Review". Press the "Save" then "Close" buttons. No flags are displayed next to the Status icon for the selected sample. The Status is the original one.
        #Confirm that all the appropriate review levels are displayed accordingly.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickOpenForReviewButton()
        shared.results.selectReviewComboBox("Initial Review")
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        shared.results.confirmStatusIcon("no_green_flag_icon.png","Not sure what goes here")
        
        #160. Select a patient sample that is "Ready for Release". Click the "Release" button, note the that sample is marked as "Released" under the Status column and in the sidebar, and then press the "Cancel Release" button in the toolbar.            
        #Confirm that the sample is marked as "Released" in the Status column while in 'Oops' state.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("In order to select a patient sample, we need another run")
        test.log("Get total number of samples before starting")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.bringToFront()
        accession_number = shared.spritecanvas.getAccessionNumber(956,54)
        shared.spritecanvas.runSampleInOpenMode(956,54)
        
        shared.bringViewingStationToTheFront()
        shared.results.clickTab()
        test.log("Need to populate table data to select a row")
        shared.results.populateTableData()
        shared.results.clickOnTableRowByName("Accession #", accession_number)
        test.verify(str(shared.results.getSelectedStatus()) == "Ready for Release", "Confirm that the selected Row in the Results Table has a status of Ready for Release")
        shared.results.clickReleaseButton()
        test.verify(str(shared.results.getSelectedStatus()) == "Released", "Confirm that the selected Row in the Results Table has a status of Released")
        test.verify(("Released by" in shared.results.getSideBarTextByIndex(2,"")) == True, "Confirm that the side bar for the selected row contains the words Released by" + shared.results.getSideBarTextByIndex(2,""))
        shared.results.clickCancelReleaseButton()
        test.verify(("Awaiting approval for CBC" in shared.results.getSideBarTextByIndex(2,"")) == True, "Confirm that the side bar for the selected row contains the words Awaiting approval " + shared.results.getSideBarTextByIndex(2,""))
        test.verify(str(shared.results.getSelectedStatus()) == "Ready for Release", "Confirm that the selected Row in the Results Table has a status of Ready for Release")
    
        #161. Click the "Print" button then the "Cancel" button to cancel out of the dialog. Click the "Print" button again to open the Print Report dialog. Press the "Print" button in the Print Report dialog.            
        #Confirm that actual printing occurs and the printout matches what was displayed in the print preview section.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("TODO Actually compare PDF to png files using squish and java apache commons Base64")
        test.log("Before we get started delete any pdf files hanging around")
        shared.results.printdialog.deletePrinterFiles()            
        shared.results.clickPrintButton()
        shared.results.printdialog.clickCancelButton()
        shared.results.clickPrintButton()
        total_pages = shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel")
        shared.results.printdialog.selectAPrinterComboItem("PDFwriter")
        shared.results.printdialog.clickPrintButton()
        printerfiles = shared.results.printdialog.getPrintedFilesTotal(total_pages)
        test.verify(len(printerfiles) == total_pages,"Confirm that the total number of pages printed are equal to the total pages displayed in the preview")
    
        #162. Select another sample from the Results Queue list and click the "Mark for Rerun" button.            
        #Confirm the sample is marked with a manual rerun icon under the Status column.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We have to run another sample")
        test.log("Get total number of samples before starting")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.bringToFront()
        accession_number = shared.spritecanvas.getAccessionNumber(956,54)
        shared.spritecanvas.runSampleInOpenMode(956,54)
        shared.bringViewingStationToTheFront()
        shared.results.clickTab()
        test.log("Need to populate table data to select a row")
        shared.results.populateTableData()
        shared.results.clickOnTableRowByName("Accession #", accession_number)
        
        shared.results.clickMarkForRerunButton()
        test.log("TODO make sure that image compare fails when it cannot locate the expected file")
        shared.results.confirmStatusIcon("failed_manual_rerun_icon.png","Failed (manual rerun")
        
        #163. Select another sample from the Results Queue list. Click the "Open for Review" button then click the "Close" button.            
        #Confirm the Review page displays as expected and closes after the Close button is pressed (assuming there're no changes).
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We have to run another sample")
        test.log("Get total number of samples before starting")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.bringToFront()
        accession_number = shared.spritecanvas.getAccessionNumber(956,54)
        shared.spritecanvas.runSampleInOpenMode(956,54)
    
        shared.bringViewingStationToTheFront()
        shared.results.clickTab()
        test.log("Need to populate table data to select a row")
        shared.results.populateTableData()
        shared.results.clickOnTableRowByName("Accession #", accession_number)
        
        shared.results.clickOpenForReviewButton()
        shared.results.confirmReviewPage()
        shared.results.confirmReviewPage("not-displayed")
        
        #164. Select another sample from the Results Queue list. Click the "View Results" button, attempt to make edits, and close out of the Review page.            
        #Confirm in "View Only" mode the Review page cannot be edited.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We have to run another sample")
        test.log("Get total number of samples before starting")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.bringToFront()
        accession_number = shared.spritecanvas.getAccessionNumber(956,54)
        shared.spritecanvas.runSampleInOpenMode(956,54)
        shared.bringViewingStationToTheFront()
        shared.results.clickTab()
        test.log("Need to populate table data to select a row")
        shared.results.populateTableData()
        shared.results.clickOnTableRowByName("Accession #", accession_number)
    
        shared.results.clickViewResultsButton()
        shared.results.confirmSaveButton("not_enabled")
        shared.results.confirmRevertButton("not_enabled")
        shared.results.confirmUndoButton("not_enabled")
        shared.results.confirmRedoButton("not_enabled")
        shared.results.confirmInitialReviewButton("not_enabled")
        shared.results.confirmAutoDiffButton("not_enabled")
        shared.results.confirmReleaseButton("not_enabled")
        
        shared.resultsoverview.confirmCommentsAreNotEditable()
        shared.wbc.clickTab()
        shared.results.confirmSaveButton("not_enabled")
        shared.results.confirmRevertButton("not_enabled")
        shared.results.confirmUndoButton("not_enabled")
        shared.results.confirmRedoButton("not_enabled")
        shared.results.confirmInitialReviewButton("not_enabled")
        shared.results.confirmAutoDiffButton("not_enabled")
        shared.results.confirmReleaseButton("not_enabled")
        
        shared.wbc.doubleClickFirstBloodSampleImage()
        shared.wbc.confirmCellDialogComments("not_editable")
        shared.wbc.clickInspectCellCancelButton()
        shared.wbc.clickReportTab()
        shared.wbc.confirmGeneralTableIsEditable(False)
        shared.wbc.confirmReportTabCommentEditable("not_editable")
        
        shared.rbc.clickTab()
        shared.results.confirmSaveButton("not_enabled")
        shared.results.confirmRevertButton("not_enabled")
        shared.results.confirmUndoButton("not_enabled")
        shared.results.confirmRedoButton("not_enabled")
        shared.results.confirmInitialReviewButton("not_enabled")
        shared.results.confirmAutoDiffButton("not_enabled")
        shared.results.confirmReleaseButton("not_enabled")
        shared.rbc.doubleClickFirstBloodSampleImage()
        shared.rbc.confirmCellDialogComments("not_editable")
        shared.rbc.clickInspectCellCancelButton()
        shared.rbc.clickReportTab()
        shared.rbc.confirmOverviewTableIsEditable(False)
        shared.rbc.confirmRBCMorphologyTableIsEditable(False)
        shared.rbc.confirmInclusionsTableIsEditable(False)
        shared.rbc.confirmReportTabCommentEditable("not_editable")
        
        shared.plt.clickTab()
        shared.results.confirmSaveButton("not_enabled")
        shared.results.confirmRevertButton("not_enabled")
        shared.results.confirmUndoButton("not_enabled")
        shared.results.confirmRedoButton("not_enabled")
        shared.results.confirmInitialReviewButton("not_enabled")
        shared.results.confirmAutoDiffButton("not_enabled")
        shared.results.confirmReleaseButton("not_enabled")
    
        shared.plt.doubleClickFirstBloodSampleImage()
        shared.plt.confirmCellDialogComments("not_editable")
        shared.plt.clickInspectCellCancelButton()
        shared.plt.clickReportTab()
        shared.plt.confirmPlateletsTableIsEditable(False)
        shared.plt.confirmReportTabCommentEditable("not_editable")
        shared.results.clickCloseButton()
    
        #165. Double-click another sample from the Results Queue list to open for review and click the "Close" button.            
        #Confirm double-clicking another sample from the Results Queue Samples list is the same as pressing the Open for Review button. 
        test.log("Step #" + str(step_counter)); step_counter += 1            
        test.log("We have to run another sample")
        test.log("Get total number of samples before starting")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.bringToFront()
        accession_number = shared.spritecanvas.getAccessionNumber(956,54)
        shared.spritecanvas.runSampleInOpenMode(956,54)
        shared.bringViewingStationToTheFront()
        shared.results.clickTab()
        test.log("Need to populate table data to select a row")
        shared.results.populateTableData()
        shared.results.clickOnTableRowByName("Accession #", accession_number)
        
        test.log("Now that we have 'another' sample")
        shared.results.doubleClickOnTableRow(0)
        image1 = "double_click_results_tab.png"
        image2 = "open_for_review_results_tab.png"
        shared.images.saveImage(image1,":Results_JComponent")
        shared.results.clickCloseButton()
        shared.results.clickOpenForReviewButton()
        shared.images.saveImage(image2,":Results_JComponent")
        shared.results.clickCloseButton()
        image1 = Config().images_dir + "/" + image1
        image2 = Config().images_dir + "/" + image2
        shared.images.compareImages(image1, image2, "true")

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
