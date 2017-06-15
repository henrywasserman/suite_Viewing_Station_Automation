# -*- coding: utf-8 -*-
import shutil
import sys
import os
import re
import exceptions
import traceback

def main():

    try:    
        step_counter = 103
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.system.mountUSBDrive()
        shared.setConfigLisReleaseDelay(6)
        
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
    
        #103. Click on the Archives main tab. Check the state of the buttons in the toolbar, and then press the "Search Archives" button with the current default date range filled.            
        #Confirm archived records are displayed.            
        #Confirm that until a row is selected, the "Export", "Print", "Export Raw", "Export Current", and "View Results" buttons are disabled.        [VM 02.27.14]
        
        #Confirm archived records are displayed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("In order to have something to archive, we run a rack of ten")
        shared.spritecanvas.runARackOfTen()
        
        test.log("Now we need to take one from the rack and run it in the other analyzer")
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.takeSampleFromAFinishedRackAndRunInSecondAnalyzer(828,165)
    
        shared.vadim.selectBloodhoundViewingStation()
        
        shared.archives.clickTab()
        shared.archives.confirmExportButton("disabled")
        shared.archives.confirmPrintButton("disabled")
        shared.archives.confirmExportCurrentButton("disabled")
        shared.archives.confirmExportRawButton("disabled")
        shared.archives.confirmViewResultsButton("disabled")
        
        shared.results.clickTab()
        shared.results.clickOnTableRow("Ready for Release")    
        shared.results.clickOpenForReviewButton()
        shared.resultsoverview.enterComments("Automation Result Overview Comment")
        test.log("Click on the WBC Tab")
        shared.wbc.clickTab()
        test.log("Click on the Report subtab Tab")
        shared.wbc.clickReportTab(":WBC.Report_TabProxy")
         
        shared.wbc.setAuerRods(["true","false","false","false","false"])
        shared.wbc.setDohleBodies(["false","true","false","false","false"])
        shared.wbc.setHypoAgranular(["false","false","true","false","false"])
        shared.wbc.setToxicGranulation(["false","false","false","true","false"])
        shared.wbc.setHyposegmentation(["false","false","false","false","true"])
        shared.wbc.setHypersegmentation(["true","false","false","false","false"])
        shared.wbc.setToxicVacuolation(["false","true","false","false","false"])
        shared.wbc.setSmudgeCells(["false","false","true","false","false"])
    
        test.log("Press the save button")
        shared.results.clickSaveButton()
        shared.results.clickReleaseButton2()
        shared.results.clickCloseButton()
    
        shared.archives.clickTab()
        shared.archives.confirmArchiveRecordsDisplayed()
        
        #Confirm that until a row is selected, the "Export", "Print", "Export Raw", "Export Current" buttons are grayed out.
        shared.archives.confirmExportButton("disabled")
        shared.archives.confirmPrintButton("disabled")
        shared.archives.confirmExportRawButton("disabled")
        shared.archives.confirmExportCurrentButton("disabled")
        test.log("TODO - check if View Results should also be disabled - Adding View Results Button for good measure")
        shared.archives.confirmViewResultsButton("disabled")
        
        test.log("Now select the archived row")
        shared.archives.clickOnTableRow("Released")
        
        shared.archives.confirmExportButton("enabled")
        shared.archives.confirmPrintButton("enabled")
        shared.archives.confirmExportRawButton("enabled")
        shared.archives.confirmExportCurrentButton("enabled")
        test.log("TODO - check if View Results should also be enabled - Adding View Results Button for good measure")
        shared.archives.confirmViewResultsButton("enabled")
        snooze(1.0)
            
        #104. Click on Results tab. Select a sample with multiple runs. Type a comment and update the morphology by turning on a reportable in its the Review page.        [VM 12.16.13] - I think there is a missed step here.We should navigate to the Results main tab before Step 102.    "(Re) The comment here is correct; there should be an additional step: ""Click on the Results tab.""
        #[VM 02.27.14] - Added"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
        row = shared.results.clickOnTableRow("Awaiting Review")
        shared.results.setAccessionNumberByRow(row)
        
        shared.results.clickOpenForReviewButton()
        shared.resultsoverview.enterComments("Automation Result Overview Comment")
        test.log("Click on the WBC Tab")
        shared.wbc.clickTab()
        test.log("Click on the Report subtab Tab")
        shared.wbc.clickReportTab(":WBC.Report_TabProxy")
        
        #TODO: Instead of just resetting here.  We should initialize with the current configuration.
        shared.wbc.resetReportArray()
        
        shared.wbc.setAuerRods(["true","false","false","false","false"])
        shared.wbc.setDohleBodies(["false","true","false","false","false"])
        shared.wbc.setHypoAgranular(["false","false","true","false","false"])
        shared.wbc.setToxicGranulation(["false","false","false","true","false"])
        shared.wbc.setHyposegmentation(["false","false","false","false","true"])
        shared.wbc.setHypersegmentation(["true","false","false","false","false"])
        shared.wbc.setToxicVacuolation(["false","true","false","false","false"])
        shared.wbc.setSmudgeCells(["false","false","true","false","false"])
        
        #105. In the Review page, press the "Release" button to release and archive the sample.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickReleaseButton2()
        shared.results.clickCloseButton()
        
        #106. Go to Archives main tab, search for the archived sample by entering the accession number, and then press the "Export" button.            
        #"Confirm the following: 
        #-""Export Data to File"" dialog displays with ""Save As"" field filled in with default ""export.txt"" 
        #-""Where"" combobox says “<No devices found>” if no writable, removable drives are connected (in kiosk mode), otherwise, ""Where"" combobox should have a local drive selected (e.g. Macintosh HD)
        #-“↑” and “↓” buttons
        #- ""+"" button
        #- File View table with Name and Date column headers
        #- ""Files of Type"" combobox is set to ""All files"" as default
        #-""Cancel"" and ""Export"" buttons
        #-The text ""Safely remove [device_name] after export"" and checkbox are grayed out"        [VM 12.16.13] - "Where" combobox does not say "<No devices found>" because there will be at least "Macintoch HD" device that will show up in there.    "(N) In Kiosk mode, the dialog will show ""<No devices found>"", but in normal mode you can see ""Macintosh HD""
        #[VM 02.27.14] - Clarification added."
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickTab()
        shared.archives.setSearchText(shared.results.getAccessionNumber())
        shared.archives.confirmArchiveRecordsDisplayed()
        
    
        test.log("When this bug is fixed not shared.archives.populateTableData() will be True")    
        if (not shared.archives.populateTableData()):
            test.warning("Mantis Bug 0013439 was found on 3/12/2014")
            test.log("Here is the work around")
            
            shared.results.clickTab()
            shared.results.doubleClickReleasedSampleRow()
            
            shared.archives.clickTab()
            shared.archives.setSearchText(shared.results.getAccessionNumber())
            shared.archives.confirmArchiveRecordsDisplayed()
        
        shared.system.unmountUSBDrive()
        test.log("TODO Create a method that waits for the USBDrive to finishes unmounting - because snoozes are not reliable.")
        snooze(5.0)
        shared.archives.clickOnTableRow("Released")
        shared.archives.clickExportButton()
        
        #"Confirm the following: 
        #-""Export Data to File"" dialog displays with ""Save As"" field filled in with default ""export.txt""
        title = shared.results.getFileExportDialogTitle()
        test.verify(title == "Export Data to File","Confirm that the dialog is named Export Data ")
        #-""Where"" combobox says “<No devices found>” if no writable, removable drives are connected
        shared.results.exportallfiledialog.confirmWhereComboSelection("<null>")
        #-“↑” and “↓” buttons
        shared.results.exportallfiledialog.confirmUpArrowButton("disabled")
        shared.results.exportallfiledialog.confirmDownArrowButton("disabled")
        #- ""+"" button
        shared.results.exportallfiledialog.confirmPlusButton("disabled")
        #- File View table with Name and Date column headers
        shared.results.exportallfiledialog.confirmColumnName(0,"Name")
        shared.results.exportallfiledialog.confirmColumnName(1,"Date")
        #- ""Files of Type"" combobox is set to ""All files"" as default
        shared.results.exportallfiledialog.confirmFilterSelectorComboBoxSelection("All files")
        #-""Cancel"" and ""Export"" buttons
        shared.results.exportallfiledialog.confirmCancelButton("enabled")
        shared.results.exportallfiledialog.confirmExportButton("disabled")
        #-The text ""Safely remove device after export"" and checkbox are grayed out"
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("disabled","device")
    
        #107. Insert flash drive into the iMac computer.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        drive_name = shared.system.mountUSBDrive()
        snooze(5.0)
    
        #108. Change the text under "Save As" to a different name.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.setFilename("a_different_name")
    
        #109. Under the "Where" combobox, select the USB flash drive as the location to export the file.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/" + drive_name)
    
        #110. Make sure that the "Safely remove "[flash drive]" after export" checkbox is checked. Press the "Export" button, and wait until the "Device Ejected" dialog opens.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Wait a second before checking")
        snooze(1.0)
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("checked") 
        #Press the "Export" button, and wait until the "Device Ejected" dialog opens.
        shared.system.deleteFile("/Volumes/" + drive_name + "/a_different_name.txt")
        shared.results.exportallfiledialog.clickExportButton()
        test.log("The Device Ejected dialog does not open here. This is Mantis Bug 10304")
    
        #111. Press the "OK" button. Take the flash drive to another station.
        #Confirm a file has been saved on the flash drive.            
        #Confirm the file opens in Excel with the exported data matching the results from the Archives table.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("No OK button currently appears due to Mantis Bug 10304")
        
        #Confirm a file has been saved on the flash drive.
        test.verify(shared.system.confirmFileExists("/Volumes/" + drive_name + "/a_different_name.txt") == True,"Confirm that the following file: /Volumes/" + drive_name  + "/a_different_name.txt exists")
        
        #Confirm the file opens in Excel with the exported data matching the results from the Archives table.
        test.log("TODO: Open Bug - Needs to be entered in mantis - we are missing the following columns")
        test.log("Status, Name, Accession #, Medical Record #, Dept., Analyzer, Archived By User, Completion Time, Release Time")
        test.log("For now I am using an expected spreadsheet that does not contain these columns")
        test.log("This new spreadsheet should fail when the 'defect is fixed'")
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/a_different_name")
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/a_different_name.xls"
        medical_record = shared.archives.populateTableData()[0]['Medical\nRecord #']
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Volumes/" + drive_name + "/a_different_name.xls",medical_record)
    
        #112. Repeat previous exporting step without inserting a USB flash drive. The "Safely remove "[flash drive] after export" is grayed out with the checkbox unchecked. Under "Where", the flash drive location is not an option
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Wait a few seconds to make sure that the USB drive gets unmounted")
        shared.system.unmountUSBDrive()
        snooze(5.0)
        shared.results.exportallfiledialog.clickExportButton()
        #The "Safely remove "[flash drive] after export" is grayed out with the checkbox unchecked.
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("disabled","device")
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("unchecked")
        #Under "Where", the flash drive location is not an option
        shared.results.exportallfiledialog.confirmWhereComboSelection("<null>")
        shared.results.exportallfiledialog.clickCancelButton()
    
        #113. Select the same sample with multiple runs, press on the "Export Current" button, and export it to the USB drive, if in Kiosk mode, otherwise export it to Users > … > Desktop.        [VM 03.13.14]    
        #Confirm the file opens in Excel with the exported data matching the results from the Archives table        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Step #" + str(step_counter)); step_counter += 1
        drive_name = shared.system.mountUSBDrive()
        test.log("Wait a few seconds for the drive to be mounted")
        snooze(3.0)
        shared.results.exportallfiledialog.clickExportCurrentButton()
        
        shared.system.deleteFile("/Volumes/" + drive_name + "/test_step_113.txt")
        shared.results.exportallfiledialog.setFilename("test_step_113.txt")
        shared.results.exportallfiledialog.clickExportButton()
        
        #Confirm the file opens in Excel with the exported data matching the results from the Archives table
        testdata_dir = Config().testdata_dir
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/test_step_113")
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/test_step_113.xls"
        medical_record = shared.archives.populateTableData()[0]['Medical\nRecord #']
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet, "/Volumes/" + drive_name + "/test_step_113.xls",medical_record)
    
        
        #114. Select the sample with multiple runs and click on the "Print" button.            
        #"Confirm that the Print Report dialog displays and the multiple results (unless Chartable is selected) reflected in the preview section are accurate.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickPrintButton()
        test.log("Wait a couple of seconds for the preview to appear")
        snooze(5.0)
        
        #"Confirm that the Print Report dialog displays and the multiple results 
        #(unless Chartable is selected) reflected in the preview section are accurate."
        test.log("TODO Find out what Chartable selected means and how to test it")
        test.vp("Test_112")
    
        #115. Preview the results by clicking and dragging on the preview section of the dialog. Review the entire preview section.            
        #Confirm the preview section displays accurate results.            
        #Confirm the print preview dialog has a "Print" and "Cancel" button, Paper Source, Printer and Format combobox, Number of Copies text field, and a checkbox labeled "Collated".            
        #Confirm zooming works when clicking and dragging on the preview section.            
        #Confirm there arrow buttons at the bottom used for next page, previous page, first page and last page.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We are not currently doing a screen shot compare on the click and drag preview section for automation")
            
        #Confirm the preview section displays accurate results.
        #Confirm the print preview dialog has a "Print" and "Cancel" button, Paper Source, Printer and Format combobox, Number of Copies text field, and a checkbox labeled "Collated".
        shared.results.printdialog.confirmPrintButton()
        shared.results.printdialog.confirmCancelButton()
        shared.results.printdialog.confirmPaperSourceComboBox()
        shared.results.printdialog.confirmPrinterComboBox()
        shared.results.printdialog.confirmFormatComboBox()
        shared.results.printdialog.confirmNumberOfCopiesTextField()
        shared.results.printdialog.confirmCollatedCheckbox()
        #Confirm zooming works when clicking and dragging on the preview section.
        test.log("Automation is not currently testing clicking and dragging in the preview section")
        #Confirm there arrow buttons at the bottom used for next page, previous page, first page and last page.
        shared.results.printdialog.confirmNextPageButton("disabled")
        shared.results.printdialog.confirmPreviousPageButton("disabled")
        shared.results.printdialog.confirmFirstPageButton("disabled")
        shared.results.printdialog.confirmLastPageButton("disabled")
        
        #116. Observe that the Print Report is defaulted to Chartable format. Select 'Lab Only (Raw)' or 'Lab Only (Latest)' format and page through the results by pressing the arrow buttons; then press the "Cancel" button and reopen the Print Report dialog        [VM 12.16.13] - If one sample with multiple runs is selected, the Chartable option will only allows to see one page, so going through the results can not take place. However, it could take place if "Lab - Only (Raw)" or "Lab - Only (Latest)" is selected.    "(N) You could page back-and-forth if there were multiple results selected, but only one sample is selected in step 112.  This step needs to be clarified.
        #[VM 02.27.14] - Added permutations (Steps 117-121). 
        #1. If sample has multiple runs and gets released, then Print Report defaults to 'Chartable' and there are no back-and-forth unless 'Lab Only (Raw)' or 'Lab Only (Latest)' is selected.
        #2. If sample has multiple runs and archived, then Print Report default to 'Lab Only (Raw)' and it is possible to back-and-forth between the runs. 'Chartable' does not appear to be an option."
        #Confirm proper paging works as expected, Print Report is defaulted to Chartable. The dialog can be close and reopen without a problem            
        
        #Observe that the Print Report is defaulted to Chartable format
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.confirmFormatComboBoxSelection("Chartable")
        #Select 'Lab Only (Raw)' or 'Lab Only (Latest)' format 
        shared.results.printdialog.selectAFormatComboItem("Lab-only (Raw)")
        #and page through the results by pressing the arrow buttons;
        shared.results.printdialog.clickNextPageButton()
        #then press the "Cancel" button and reopen the Print Report dialog
        shared.results.printdialog.clickCancelButton()
        shared.archives.clickPrintButton()
        
        test.log("Get total pages to be printed for later verification")
        total_pages = shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel")
        
        #117. Click on the "Print" button in the dialog to print the results.            
        #Confirm the printing occurs on the selected printer.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Remove all printer files before printing")
        shared.results.printdialog.deletePrinterFiles()
        test.log("Print")
        test.log("Make sure the PDF Printer Driver is Selected")
        shared.results.printdialog.selectAPrinterComboItem("PDFwriter")
        shared.results.printdialog.clickPrintButton()
        #Confirm the printing occurs on the selected printer.
        test.log("Here I am confirming that the correct number of pages were printed")
        printerfiles = shared.results.printdialog.getPrintedFilesTotal(total_pages)
        test.verify(len(printerfiles) == total_pages,"Confirm that the total number of pages printed are equal to the total pages displayed in the preview")
    
        #118. Navigate back to Results page and find a sample with multiple runs. Select that sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Create a sample with a mutliple run")
        shared.spritecanvas.selectAnalyzerSimulator()
        mouse_position = shared.spritecanvas.getAccessionNumberFromAFinishedRack()
        accession_number = shared.spritecanvas.runSampleInOpenMode(mouse_position[0],mouse_position[1])
        
        shared.selectBloodhoundViewingStation()
        shared.results.clickTab()
        shared.results.populateTableData()
        shared.results.clickOnRowByAccessionNumber(accession_number)
        
        #119. Click Archive button. Enter your login credentials. Click on Archive button in the Unreleased Tests dialog box.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickArchiveButton()
        shared.results.archivesampledialog.setUsername(shared.vadim.username)
        shared.results.archivesampledialog.setPassword(shared.vadim.password)
        shared.results.archivesampledialog.clickArchiveButton()
        test.log("Have to click one more time because a message box appears that says 'Are you sure?")
        shared.results.archivesampledialog.clickArchiveButton()
        
        #120. Navigate back to Archives. Enter the accession number in search text box and click Search Archives button.            
        #Confirm the sample is found and appears in the table.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickTab()
        shared.archives.setSearchText(accession_number)
        shared.archives.confirmArchiveRecordsDisplayed()
        
        #121. Select the sample and click on Print button.            
        #Confirm the Print Report dialog box appears. Format is defaulted to 'Lab-only (Raw)'.
        #Confirm user can scroll through the runs by clicking left and right arrow buttons
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickOnRowByAccessionNumber(accession_number)
        shared.archives.clickPrintButton()
        shared.results.printdialog.confirmPrintDialogAppears()
        shared.results.printdialog.confirmFormatComboBoxSelection("Lab-only (Raw)")
        test.log("Note: the method below clicks both the right and left arrow button")
        shared.results.printdialog.confirmLabOnlyForAnySample()
        
        #122. Click Cancel button in Print Report dialog box
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.clickCancelButton()
        
        #123. Clear out the Search field. Press the "Search Archives" button to do a complete record search. Select about 5 samples and press the "Print" button.            
        #"Confirm a status messages appears at the bottom left of the screen saying “Printing Report: Page [n] of [total]"".
        #NOTE: The status message appears only for a brief moment. To catch that message, user is recommended to select multiple samples and/or samples with multiple runs. That way, the message stays on the screen for a little longer. Print to printer the first time. However, to avoid ink waste, it is recommended to print to PDF thereafter. 
        #NOTE: if not running in kiosk mode, the printer icon will appear in the dashboard indicating printer receiving the print job."            "(N) If the Viewing Station is running in windowed mode (not kiosk), the user can observe a printer icon appearing and disappearing multiple times in the dashboard on the bottom of the screen.
        #[VM 02.27.14] - Altered. "
        #Confirm Printing occurs and that the print out matches the Preview display including each run printed on its own page.            "(Re) Real print-outs should be verified, not just PDFs as suggested in the note on line 252 above.
        #[VM 02.27.14] - Altered."
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
        test.log("Highlight two more rows")
        shared.results.selectTableRows(0,1)
        shared.results.clickArchiveButton()
        shared.results.archivesampledialog.setUsername(shared.vadim.username)
        shared.results.archivesampledialog.setPassword(shared.vadim.password)
        shared.results.archivesampledialog.clickArchiveButton()
        test.log("Have to click one more time because a message box appears that says 'Are you sure?")
        shared.results.archivesampledialog.clickArchiveButton()
        
        shared.archives.clickTab()
        shared.archives.setSearchText("")
        shared.archives.clickSearchArchivesButton()
        
        shared.archives.selectTableRows(0,4)
        
        #124. Click the "Print" button and select "Lab-only (Raw)" option. Page through the results by pressing the arrow buttons; then press the "Cancel" button. Reopen the print preview dialog            
        #Confirm Print Report dialog displays only the raw results (no morphology changes), proper paging and preview zooming work as expected.
        #Confirm after closing and reopening, original results data is still displayed without discrepancy.                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickPrintButton()
        shared.results.printdialog.selectAFormatComboItem("Lab-only (Raw)")
        shared.results.printdialog.confirmLabOnlyForAnySample()
        shared.results.printdialog.clickCancelButton()
        
        test.log("We need to get Medical Record in order find out which screen shot to compare against")
        row = shared.archives.getTableRowByName("Accession #", "SL00007")
        test.log("Here is medical record: " + str(row['Medical\nRecord #']))
        
        test.log("Re-open print preivew dialog")
        shared.results.printdialog.clickPrintButton()
        
        test.log("Confirm No Morphology Changes")
        if (str(row['Medical\nRecord #']) == '4711'):
            test.vp("No Morphology 4711")
        else:
            test.vp("No Morphology 4712")
        
        test.log("Confirm proper paging")
        shared.results.printdialog.confirmLabOnlyForAnySample()
        test.log("TODO we have not yet implemented preview zooming")
        
        shared.results.printdialog.clickLastPageButton()
        shared.results.printdialog.clickFirstPageButton()
        
        test.log("Confirm after closing and reopening - original results data is still displayed")
        shared.results.printdialog.clickCancelButton()
        shared.results.printdialog.clickPrintButton()
    
        if (str(row['Medical\nRecord #']) == '4711'):
            test.vp("First Page 4711")
        else:
            test.vp("First Page 4712")
            
        shared.results.printdialog.clickCancelButton()
        
        #125. Click the "Print" button.            
        #Confirm printout matches the Print Report dialog
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickPrintButton()            
        shared.results.printdialog.deletePrinterFiles()
        total_pages = shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel")
        shared.results.printdialog.clickPrintButton()
        
        test.log("Here I am only confirming that the correct number of pages were printed")
        test.log("TODO turn the printed output into png files and compare those")
        test.log("Wait a second for the file to appear")
    
        shared.results.printdialog.confirmTotalPrintedPages(total_pages)
            
        #126. Once again, reopen the Print Report dialog and select "Lab-only (Latest)" option, page through the results by pressing the arrow buttons; then press the "Cancel" button and reopen the Print Report dialog            
        #Confirm Print Report dialog displays only the current results and proper paging and preview zooming all works
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.clickPrintButton()
        shared.results.printdialog.selectAFormatComboItem("Lab-only (Latest)")
        
        shared.results.printdialog.confirmLabOnlyForAnySample()
        shared.results.printdialog.clickCancelButton()
        shared.results.printdialog.clickPrintButton()
        
        test.log("Confirm after closing and reopening - original results data is still displayed")
        if (str(row['Medical\nRecord #']) == '4711'):
            test.vp("First Page 4711")
        else:
            test.vp("First Page 4712")
            
        test.log('Click through, stepping through each page and checking that all format options exist')
        test.log("TODO not currently checking the zoom feature")
        shared.results.printdialog.confirmLabOnlyForAnySample()
        shared.results.printdialog.clickCancelButton()

    except:
        test.fail("Test failed due to exception")
    finally:
        shared.system.terminateViewingStation()


        