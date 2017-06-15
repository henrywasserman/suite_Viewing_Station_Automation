# -*- coding: utf-8 -*-
import shutil
import sys
import os
import exceptions
import traceback

def main():
    
    try:
        step_counter = 101
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.setConfigLisReleaseDelay(6)
        shared.system.unmountUSBDrive()
    
        #101. Click on the Archives main tab. Check the state of the buttons in the toolbar, and then press the 
        #"Search Archives" button with the current default date range filled
    
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
        
        shared.wbc.setAuerRods("true")
        shared.wbc.setDysplasticCells("true")
        shared.wbc.setSmudgeCells("true")
    
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
        
        #102. Select a sample with multiple runs. 
        #Type a comment and update the morphology by turning on a reportable in its the Review page.
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
        
        shared.wbc.setAuerRods("true")
        shared.wbc.setDysplasticCells("true")
        shared.wbc.setSmudgeCells("true")
        
        #103. In the Review page, press the "Release" button to release and archive the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickReleaseButton2()
        shared.results.clickCloseButton()
        
        #104. Go to Archives main tab, search for the archived sample by entering the accession number, 
        #and then press the "Export" button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickTab()
        shared.archives.setSearchText(shared.results.getAccessionNumber())
        shared.archives.confirmArchiveRecordsDisplayed()
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
        
        #105. Insert flash drive into the iMac computer.
        test.log("Step #" + str(step_counter)); step_counter += 1
        drive_name = shared.system.mountUSBDrive()
        
        #106. Change the text under "Save As" to a different name.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.setFilename("a_different_name")
        
        #107. Under the "Where" combobox, select the USB flash drive as the location to export the file.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/" + drive_name)
        
        #108. Make sure that the "Safely remove "[flash drive]" after export" checkbox is checked.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Wait a second before checking")
        snooze(1.0)
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("checked") 
        #Press the "Export" button, and wait until the "Device Ejected" dialog opens.
        shared.system.deleteFile("/Volumes/" + drive_name + "/a_different_name.txt")
        shared.results.exportallfiledialog.clickExportButton()
        test.log("The Device Ejected dialog does not open here. This is Mantis Bug 10304")
        
        #109. Press the "OK" button. Take the flash drive to another station.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("No OK button currently appears due to Mantis Bug 10304")
        
        #Confirm a file has been saved on the flash drive.
        test.verify(shared.system.confirmFileExists("/Volumes/" + drive_name + "/a_different_name.txt") == True,"Confirm that the following file: /Volumnes/" + drive_name + "/a_different_name.txt exists")
        
        #Confirm the file opens in Excel with the exported data matching the results from the Archives table.
        test.log("TODO: Open Bug - Needs to be entered in mantis - we are missing the following columns")
        test.log("Status, Name, Accession #, Medical Record #, Dept., Analyzer, Archived By User, Completion Time, Release Time")
        test.log("For now I am using an expected spreadsheet that does not contain these columns")
        test.log("This new spreadsheet should fail when the 'defect is fixed'")
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/a_different_name")
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/a_different_name.xls"
        medical_record = shared.archives.populateTableData()[0]['Medical\nRecord #']
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Volumes/" + drive_name + "/a_different_name.xls",medical_record)
        
        #110. Repeat previous exporting step without inserting a USB flash drive.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.system.unmountUSBDrive()
        test.log("Wait a second to make sure that the USB drive gets unmounted")
        shared.results.exportallfiledialog.clickExportButton()
        #The "Safely remove "[flash drive] after export" is grayed out with the checkbox unchecked.
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("disabled","device")
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("unchecked")
        #Under "Where", the flash drive location is not an option
        shared.results.exportallfiledialog.confirmWhereComboSelection("<null>")
        shared.results.exportallfiledialog.clickCancelButton()
        
        #111. Select the same sample with multiple runs, press on the "Export Current" button, 
        #and export it to Users > … > Desktop.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.clickExportCurrentButton()
        
        shared.system.deleteFile("/Users/" + shared.config.getSystemUserName() + "/Desktop/test_step_111.txt")
        shared.results.exportallfiledialog.setFilename("/Users/" + shared.config.getSystemUserName() + "/Desktop/test_step_111")
        shared.results.exportallfiledialog.clickExportButton()
        
        #Confirm the file opens in Excel with the exported data matching the results from the Archives table
        shared.spreadsheets.openExcelAndSaveFile("/Users/" + shared.config.getSystemUserName() + "/Desktop/test_step_111")
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/test_step_111.xls"
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Users/" + shared.config.getSystemUserName() + "/Desktop/test_step_111.xls")
        
        #112. Select the sample with multiple runs and click on the "Print" button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickPrintButton()
        test.log("Wait a couple of seconds for the preview to appear")
        snooze(2.0)
        
        #"Confirm that the Print Report dialog displays and the multiple results 
        #(unless Chartable is selected) reflected in the preview section are accurate."
        test.log("TODO Find out what Chartable selected means and how to test it")
        test.vp("Test_112")
        
        #113. Preview the results by clicking and dragging on the preview section of the dialog. 
        #Review the entire preview section.
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
        
        #114. Observe that the Print Report is defaulted to Chartable format
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.confirmFormatComboBoxSelection("Chartable") 
        #and page through the results by pressing the arrow buttons;
        test.log("TODO Note: In this case there is only one page in the results") 
        #then press the "Cancel" button and reopen the Print Report dialog
        shared.results.printdialog.clickCancelButton()
        shared.archives.clickPrintButton()
        shared.results.printdialog.selectAPrinterComboItem("PDFwriter")
        #Confirm proper paging works as expected, Print Report is defaulted to Chartable.
        test.log("TODO Again there is nothing to page through here")
        shared.results.printdialog.confirmFormatComboBoxSelection("Chartable")
        test.log("Get total pages to be printed for later verification")
        total_pages = shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel")
        #The dialog can be closed and reopen without a problem
        
        #115. Click on the "Print" button in the dialog to print the results.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Remove all printer files before printing")
        shared.results.printdialog.deletePrinterFiles()
        test.log("Print")
        shared.results.printdialog.clickPrintButton()
        #Confirm the printing occurs on the selected printer.
        test.log("Here I am confirming that the correct number of pages were printed")
        printerfiles = shared.results.printdialog.getPrintedFilesTotal(total_pages)
        test.verify(len(printerfiles) == total_pages,"Confirm that the total number of pages printed are equal to the total pages displayed in the preview")
        
        #116. Clear out the Search field. Press the "Search Archives" button to do a complete record search. Select about 5 samples and press the "Print" button.
        #Confirm a status messages appears at the bottom left of the screen saying “Printing Report: Page [n] of [total]".
        #Confirm Printing occurs and that the print out matches the Preview display including each run printed on its own page.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We need to archive 3 more records for these next steps")
        shared.results.archiveRecords(shared.vadim, 3)
        test.log("Go back to the Archives Tab")
        shared.archives.clickTab()
        shared.archives.setSearchText("")
        shared.archives.clickSearchArchivesButton()
        shared.archives.selectTableRows(0,4)
        shared.archives.clickPrintButton()
        shared.results.printdialog.clickPrintButton()
        test.vp("PrintingPages")
        
        test.log("For now we can print to pdf. We can transform from pdf to png")
        test.log("We will be implementing image compare with masking a little later down the road.")
        
        #117. Click the "Print" button and select "Lab-only (Raw)" option. Page through the results 
        #by pressing the arrow buttons; then press the "Cancel" button. Reopen the print preview dialog
        #Confirm Print Report dialog displays only the raw results (no morphology changes), proper paging and preview zooming work as expected.
        #Confirm after closing and reopening, original results data is still displayed 
        #without discrepancy.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.clickPrintButton()
        test.log("Select Lab-only (Raw) Format")
        shared.results.printdialog.selectAFormatComboItem("Lab-only (Raw)")
        test.log("Page through the results by pressing arrow buttons")
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
        
        shared.results.printdialog.clickFirstPageButton()
        
        test.log("Confirm after closing and reopening - original results data is still displayed")
        if (str(row['Medical\nRecord #']) == '4711'):
            test.vp("First Page 4711")
        else:
            test.vp("First Page 4712")
            
        #118. Click the "Print" button.
        #Confirm printout matches the Print Report dialog
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.deletePrinterFiles()
        total_pages = shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel")
        shared.results.printdialog.clickPrintButton()
        
        test.log("Here I am only confirming that the correct number of pages were printed")
        test.log("TODO turn the printed output into png files and compare those")
        test.log("Wait a second for the file to appear")
    
        shared.results.printdialog.confirmTotalPrintedPages(total_pages)
        
        #119. Once again, reopen the Print Report dialog and select "Lab-only (Latest)" option, 
        #page through the results by pressing the arrow buttons; then press the "Cancel" button 
        #and reopen the Print Report dialog
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

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
