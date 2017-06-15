# -*- coding: utf-8 -*-
import shutil
import sys
import os
import exceptions
import traceback

def main():
    try:
        step_counter = 14
            
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup("SIMULATED_SLOW")
        version = shared.version
        shared.setConfigLisReleaseDelay(6)
        
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
    
        test.log("Before we get started record the total number of samples on the In Process Page")
        shared.vadim.selectBloodhoundViewingStation()
        total_samples = shared.inprocess.getTotalNumberOfSamples()
    
        #14. Run a sample in rack mode and observe the In Process Samples list.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        
        test.log("Select The Analyzer Simulator")
        shared.spritecanvas.bringToFront()
        shared.spritecanvas.selectAnalyzerSimulator()
        
        test.log("Move An Empty Rack into the belt")
        shared.spritecanvas.moveEmptyRackToTheBelt()
        test.log("Move a sample into the Rack")
        accession_number = shared.spritecanvas.moveObjectAndSetAccessionNumber(957,20,329,178)
        test.log("Run the sample")
        shared.spritecanvas.runSampleRack()
        shared.selectBloodhoundViewingStation()
        shared.inprocess.waitForTableStatusReadyForRelease()
        
        #Confirm the sample displays on the In Process Samples list with its status and runs list on the sidebar.
        shared.inprocess.confirmARunOnTheSideBar()            
        #Confirm that the sample is listed as "Rack" under the "Mode" column.
        shared.inprocess.confirmRackUnderModeColumn(total_samples + 1)            
        #Confirm that the sample's patient identity is populated in the patient data section in the toolbar.
        shared.inprocess.confirmSamplePatientIdentityInfoExists()
        
        #15. Once the all the runs are finished, click to the Results main tab and observe the sample appears under the queue.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
        shared.results.confirmAccessionNumberAppearsInTable(accession_number)
    
        #16. Double-click the sample for review and view the results in the Overview, WBC, RBC and PLT subtab; observe that the cell images are loaded properly.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("TODO: Will have to revisit how to observe that cell images are loaded properly")
        shared.results.doubleClickOnTableRow(0)
        
        #17. Click to the WBC subtab, highlight ten Neutrophils cell type, and press the spacebar key to invoke the Cell Inspector dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wbc.clickTab()
        shared.wbc.hightlightNeutrophilsCells(10)
        
        #18. Observe that a dialog displays with the title "Inspect 10 Cells", reclassify the cells into Blast cell type by selecting "Blast" option in the Reclassify combobox, and press the OK button to close the dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wbc.inspectcellsdialog.confirmTitle("Inspect 10 Cells")
        shared.wbc.inspectcellsdialog.selectComboboxItem("Blast (Any Type)")
        shared.wbc.inspectcellsdialog.clickOKButton()
        
        #19. Observe once the dialog is closed a new line in the WBC gallery is created for the cell type "Blast" and a new row is created in the differential table in the sidebar with an absolute count and percentage.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wbc.confirmNewLine("Blast (Any Type)")
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        shared.results.confirmCellTypeTableData('Blast (Any Type)')
        
        #20. Click on the Report tab in the sidebar, check a few reportables on (note which ones you update).
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickOpenForReviewButton()
        shared.wbc.clickTab()
        shared.wbc.clickReportTab()
        shared.wbc.checkAndUncheckOptions()
            
        #21. Click Save and Close buttons on the toolbar.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        
        test.log("TODO: going to revisit the testing of this performance issue.")
        #Confirm that the cell images are loaded properly in a reasonable time in Review page.
        #Confirm Cell Inspector dialog reclassify the cells once the dialog is closed and a new line is created in the WBC cell gallery.
        shared.results.clickOpenForReviewButton()
        shared.wbc.clickTab()            
        shared.wbc.confirmNewLine("Blast (Any Type)")
        #Confirm a new row is created in the differential table in the sidebar with an absolute count and percentage.
        shared.results.clickCloseButton()            
        shared.results.confirmCellTypeTableData('Blast')
        #Confirm the sample has been reflagged in the Results Queue list.
        shared.results.confirmStatusByAccessionNumber("Awaiting Review",accession_number)             
        #Confirm the sample has been reflagged in the Results Queue list.            "(N) I'm not aware of any such dialog; the Viewing Station doesn't ""save files"" except during export.
        test.verify(str(shared.results.getSelectedStatus()) == "Awaiting Review", "Confirm that the selected Status is now 'Awaiting Review'")
        #[VM 02.27.14] - This must be an older version of the TC. Because I do not have this line in the TC I have. Instead, there is a different line here."
        #"Confirm the provisional release (white checkmark) is no longer displayed for this sample, and the Release button on the toolbar is disabled.
        shared.results.confirmTheWhiteCheckmarkIsNoLongerDisplayed()
        #"            "(Re) Doesn't this imply that you should try logging in? How are steps 22-27 related to this requirement?
        #[VM 02.27.14] - This must be an older version of the TC. Because I do not have this line in the TC I have. Instead, there is a different line here. "
    
        #22. Reopen the sample for review. Press the "Action" button. The Release Action dialog opens. Press the "Release" button to release the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickOpenForReviewButton()
        shared.results.clickActionButton()
        shared.releaseactiondialog.clickReleaseButton()
        
        #23. Go to the Archives tab. In the Search field, type the Accession # of the sample you just released. Open the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickTab()
        shared.archives.setSearchText(accession_number)
        shared.archives.clickSearchArchivesButton()
        shared.archives.confirmArchiveRecordsDisplayed()
        shared.archives.populateTableData()
        shared.archives.clickOnArchiveRow()
        shared.archives.clickViewResultsButton()
    
        #Under WBC > Report, confirm the corresponding changes are displayed.
        shared.wbc.clickTab(":Archives.WBC_TabProxy")
        shared.wbc.clickReportTab(":WBC.Report_TabProxy_2")
        shared.wbc.confirmCorrespondingReportChanges()
        shared.archives.clickCloseButton()
        
        #24. Select another sample from the Results Queue list. Press the "Release" button. Double-click this sample while it is in the "Oops" delay.            
        #Confirm the sample can be viewed momentarily. The released sample eventually closes out after being archived.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
        shared.results.clickCloseButton()    
        shared.results.populateTableData()
        shared.results.clickOnTableRow("Ready for Release")
        shared.results.setAccessionNumber()
        shared.results.clickReleaseButton()
           
        shared.results.doubleClickReleasedSampleRow()
        test.log("Confirm that the Release Dialog Appears and is removed within 5 minutes")
        shared.results.confirmResultsReleaseDialogAppearsOnlyForAShortTime(shared.results.getAccessionNumber())
    
        shared.results.populateTableDataWithAllRowsEqualToReadyforRelease()
    
        #25. Open any "Ready for Release" sample for review. Press the "Action" button, and partially release some of the test orders. For example, uncheck Diff orders. It will only release CBC order.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This First Time through we are going to deselct Diff.")
        test.log("Open any 'Ready for Release' sample")
        test.log("Just in case get the Table Data")
        shared.results.populateTableData()
        test.log("Click on the first row in the results table that has the status of Ready for Release")
        shared.results.clickOnTableRow("Ready for Release")
        
        test.log("Click on the Open for Review Button")
        shared.results.clickOpenForReviewButton() 
        
        test.log("Click on the Action Button")
        shared.results.clickActionButton()
        
        test.log("Partially release some of the test orders.")
        shared.releaseactiondialog.uncheckDiff()
                
        #26. Once the "Release" button is pressed in the Release Action dialog, press the "Action" button to reopen the Release Action dialog.            
        #Confirm that only the selected orders are released. Confirm the grayed out results (in our example, CBC order) in the Release Action dialog. Click Cancel on Release Action dialog box. Click Close in Results main tab.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.releaseactiondialog.clickReleaseButton2()
        shared.results.clickActionButton()
        
        test.log("Setup Expected Results for CBC deselected")
        shared.releaseactiondialog.setupDiffDeselectedExpectedResults()
        
        #Confirm that only the select orders are released.
        
        test.log("Confirm the grayed out results.")
        shared.releaseactiondialog.populateTableData()
        shared.releaseactiondialog.confirmReleaseResultsCheckedAndDisabled()
        
        test.log("Click on the Release Action Cancel Button")
        shared.releaseactiondialog.clickCancelButton()
        
        test.log("Click on the Results Close Button")
        shared.results.clickCloseButton()
    
        #27. Open a different sample for review. Press the "Action" button. Perform the same partial release for Diff orders only; then open the Release Action dialog again to view the released parameters.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("In order to open a different sample I need to run one more sample")
        
        test.log("Select The Analyzer Simulator")
        shared.spritecanvas.bringToFront()
        shared.spritecanvas.selectAnalyzerSimulator()
        
        test.log("Move An Empty Rack into the belt")
        shared.spritecanvas.moveEmptyRackToTheBelt()
        test.log("Move a sample into the Rack")
        accession_number = shared.spritecanvas.moveObjectAndSetAccessionNumber(957,20,329,178)
        test.log("Run the sample")
        shared.spritecanvas.runSampleRack()
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        shared.inprocess.waitForTableStatusReadyForRelease()
        
        shared.results.clickTab()
        
        test.log("Just in case get the Table Data")
        shared.results.populateTableData()
        shared.results.clickOnTableRowIndex(0)
            
        shared.results.clickOpenForReviewButton() 
        
        test.log("Click on the Action Button")
        shared.results.clickActionButton()
        
        test.log("Click on the CBC CheckBox")
        
        test.log("Partially release some of the test orders, this time CBC")
        shared.releaseactiondialog.uncheckCBC()
        
        test.log("Click on the Release Button")
        shared.releaseactiondialog.clickReleaseButton2()
        
        test.log("Click on the Action Button")
        shared.results.clickActionButton()    
        
        #28. Observe the released results are grayed out and then continue to release the CBC orders.
        #Confirm that only those samples that are selected are released. Confirm the grayed out results. Continue to release unchecked cell types (if any).
        test.log("Step #" + str(step_counter)); step_counter += 1            
        test.log("Setup Expected Results for CBC deselected")
        shared.releaseactiondialog.setupCBCDeselectedExpectedResults()
        
        test.log("Confirm the grayed out results.")
        shared.releaseactiondialog.populateTableData()
        shared.releaseactiondialog.confirmReleaseResultsCheckedAndDisabled()

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()    