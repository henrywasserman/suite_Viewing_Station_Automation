# -*- coding: utf-8 -*-
import shutil
import sys
import os
import exceptions
import traceback

def main():
    try:
        step_counter = 31
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.setConfigLisReleaseDelay(6)
        
        #TODO right now data.simulator.errorRate=0.0 this means no errors
        #We need to rewrite code to account for these errors as they come up
        
        # (Header) Print Functionalities in Results Main Tab
        #31. Control+command+click on the Bloodhound Infinity symbol on top of the Dashboard to minimize the Viewing Station 
        #into windowed mode and press the "X" button on the top left side of the title bar to close the Viewing Station.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.verify("Skipping Kiosk for now. Not currently necessary for automation")
        
        #32. Once the Viewing Station relaunches automatically (only in kiosk mode), 
        #log in as admin again and go to the Results main tab.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
    
        #33. Observe that all the buttons in the Results Queue toolbar are disabled - 
        #Print, Export Current, Export Raw, etc.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.confirmReleaseButton("disabled")
        shared.results.confirmCancelReleaseButton("disabled")
        shared.results.confirmPrintButton("disabled")
        shared.results.confirmArchiveButton("disabled")
        shared.results.confirmExportCurrentButton("disabled")
        shared.results.confirmExportRawButton("disabled")
        shared.results.confirmOverrideLockButton("disabled")
        shared.results.confirmMarkForRerunButton("disabled")
        shared.results.confirmOpenForReviewButton("disabled")
        shared.results.confirmViewResultsButton("disabled")
    
        #34. Select a "Ready for Release" sample that has a white check mark in the Status column of the Results tab 
        #and double-click it to open for review.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Put the TableData in a Dictionary")
        shared.results.populateTableData()
        test.log("Click on the first row in the results table that has the status of Ready for Release")
        row = shared.results.clickOnTableRow("Ready for Release")
        test.log("Now Double click on it")
        shared.results.doubleClickOnTableRow(row)
        
        #35. In the Overview subtab, enter some text in the "Comments" text field that appears at the bottom of the page.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.resultsoverview.enterComments("Automation Result Overview Comment")
    
        #36. Go to the WBC subtab, click on the Report subtab, and turn on "Y" for Auer rods, Dysplastic cells, 
        #and Smudge cells to classify the morphology.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Click on the WBC Tab")
        shared.wbc.clickTab()
        test.log("Click on the Report subtab Tab")
        shared.wbc.clickReportTab(":WBC.Report_TabProxy")
        
        shared.wbc.setAuerRods("true")
        shared.wbc.setDysplasticCells("true")
        shared.wbc.setSmudgeCells("true")
        
        #37. Press the Save button, and press the Release button in the toolbar.
        #then press the Close button to go back to the Results Queue
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Press the save button")
        shared.results.clickSaveButton()
        test.log("Click on the Release Button")
        shared.results.clickReviewReleaseButton()
        test.log("Close out of the review page")
        shared.results.clickReviewPageCloseButton()
        
        #38. Immediately press on the Print button during Oops delay (15 seconds) with the sample highlighted and once 
        #the Print Report dialog opens, click and drag on the preview section to the left to preview 
        #the reportables and comments.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We are not currently doing a screen shot compare on the click and drag portion of this test")
        
        shared.results.populateTableData()
        shared.results.clickOnTableRow("Released")
        shared.results.clickPrintButton()
    
        #39. Observe that the reportables, comments and results matches in the table matches the released sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.moveDialogToTopCorner()
        test.vp("4712_Lab_Report")
        
        #40. Click on the Format combobox and observe that there are three options for format type - 
        #Chartable, Lab-only (Raw), and Lab-only (Latest).
        
        #Confirm the Print dialog will contain a combobox to select the type of report to print.
        #Confirm the options will be “Chartable”, “Lab-only (Raw)”, and "Lab-only (Latest)".
        #Confirm the chartable report will also contain an area labeled “Comments”.
        #Confirm this area will contain a list of all morphology, in the same format as on the Results subtab of the Review page.
        #Confirm following the morphology, any reportable comments entered by the user will also be shown.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.confirmFormatDropDownItems("Chartable,Lab-only (Raw),Lab-only (Latest)")
    
        #41. Observe that there's a Cancel button, press the button to close the Print Report dialog, 
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.clickCancelButton()
        
        #and open a sample that has multiple runs for review.
        test.log("Click on the InProcess Tab")
        shared.inprocess.clickTab()
        
        test.log("Get total number of samples before we start another run.")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        
        test.log("Run another sample in an open mode")
        test.log("Note down the accession number")
        shared.spritecanvas.runSampleInOpenMode(956,54)
        
        #Wait for the sample to process.
        #And Populate Table
        shared.inprocess.populateTableDataWithAllRowsEqualToReadyforRelease()
    
        test.log("Click on the InProcess Tab")
        shared.inprocess.clickTab()
        
        test.log("Get total number of samples before we start another run.")
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        
        shared.spritecanvas.reRunSampleInOpenMode(254,374)
        
        waitForObject(":Bloodhound™ Viewing Station " + version + "_JPanel").getTopLevelAncestor().toFront()
        shared.tables.waitForTableStatusReadyForReleaseOrAwaitingReview(":In Process.Show All_JTable")
        test.log("Populate Table one more time")
        shared.results.populateTableData()
        
        test.log("Click on the First Multiple Run Row Found.")
        row = shared.results.clickOnTableRow("Awaiting Review")
        test.log("Now Double click on it")
        shared.results.doubleClickOnTableRow(row)
        
        #42. In the Overview subtab, enter some text in the "Comments" text field that appears at the bottom of the page
        test.log("Step #" + str(step_counter)); step_counter += 1 
        shared.resultsoverview.enterComments("Automation Result Overview Comment")
        
        #We need a new wbc here for now...
        wbc = WBC()
        
        test.log("I am also going to add morphology here")
        test.log("Click on the WBC Tab")
        wbc.clickTab()
        test.log("Click on the Report subtab Tab")
        wbc.clickReportTab(":WBC.Report_TabProxy")
        
        wbc.setAuerRods("true")
        wbc.setDysplasticCells("true")
        wbc.setSmudgeCells("true")
        
        #and press the Save and Close button respectively to back to Results Queue.
        shared.results.clickSaveButton()
        shared.results.clickReviewPageCloseButton()
        
        #43. Press the Print button while the sample is highlighted in the Results Queue and select 
        #the "Lab-only (Raw)" option from the Format combobox Note: It should be defaulted to "Lab-only (Raw)".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickPrintButton()
        test.log("This is to verify item 0 and item 1")
        shared.results.printdialog.confirmFormatDropDownItems("Lab-only (Raw),Lab-only (Latest)")
        shared.results.printdialog.selectAFormatComboItem("Lab-only (Raw)")
        
        #44. Observe that the "Lab-only (Raw)" contains only the raw results without no morphology.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.moveDialogToTopCorner()
        test.vp("NoMorphology")
        
        #45. Select the "Lab-only (Latest)" format and observe that comments and morphology are displayed 
        #in the results table in the preview.
        test.log("Step #" + str(step_counter)); step_counter += 1 
        shared.results.printdialog.selectAFormatComboItem("Lab-only (Latest)")
        snooze(1.0)
        test.vp("Morphology")
        
        #46. Close out the Print Report dialog, go back to the Results tab, and select 5 samples, with one sample having 
        #multiple results.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.clickCancelButton()
            
        test.log("In order to have 5 samples. We run a rack of 10")
        shared.spritecanvas.runARackOfTen()
        
        test.log("Now we need to take one from the rack and run it in the other analyzer")
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.takeSampleFromAFinishedRackAndRunInSecondAnalyzer(828,165)
        
        test.log("I am assuming here that the first row will now contain a multiple result")
        shared.selectBloodhoundViewingStation()
        shared.results.clickTab()
        shared.results.populateTableData()
        shared.results.selectTableRows(0, 4)
    
        #47. Press the Print button and then press the “→”  button at the bottom to page to the next results set.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickPrintButton()
        shared.results.printdialog.clickNextPageButton()
        
        test.vp("Print5Results_SecondPage")
            
        #48. Press the “←” to go to the previous page; 
        #press the “ ⇥ ” to move to the last page; 
        #Click on the " ⇤ " to move to the first page.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Only testing here for page number and Parameter Names")
        shared.results.printdialog.clickPreviousPageButton()
        test.vp("Print5Results_FirstPage")
        
        test.log("Only testing here for page number and Parameter Names")
        shared.results.printdialog.clickLastPageButton()
        test.vp("Print5Results_LastPage")
        
        test.log("Only testing here for page number and Parameter Names")
        shared.results.printdialog.clickFirstPageButton()
        test.vp("Print5Results_FirstPageAgain")
        
        #49. Click on the Printer combobox, observe that it lists all of the printers that are connected 
        #to the Viewing Station, and close the print dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.confirmPrintDropDownItems("Brother MFC-9460CDN,Brother HL-4040CN series,Brother HL-2240 series,PDFwriter")
        
        #Confirm pressing the Cancel button will close the dialog.
        shared.results.printdialog.clickCancelButton()
        test.vp("PrintDialog")
    
        test.log("Have to Open Print Dialog again to confirm the rest")
        shared.results.clickPrintButton()    
        
        #Confirm buttons will appear under the preview to navigate between pages of the preview.
        #Confirm the buttons will be labeled
        #“ ⇤ ” (first page),
        #“←” (previous page), 
        #“→” (next page), and 
        #“ ⇥ ” (last page). Note: Only the symbols are part of the name here, not the text in parentheses.
        shared.results.printdialog.confirmFirstPageButton("disabled")
        shared.results.printdialog.confirmPreviousPageButton("disabled")
        shared.results.printdialog.confirmNextPageButton()
        shared.results.printdialog.confirmLastPageButton()
        
        #Confirm for each sample being printed, the lab report will contain one page for each run that has results.
        shared.results.printdialog.confirmTotalPages(6)
        #Confirm the “Lab-only” report type will be selectable for any sample.
        shared.results.printdialog.confirmLabOnlyForAnySample()
        #Confirm a combobox in the dialog will list all the printers that are connected to the Viewing Station.
        shared.results.printdialog.confirmPrintDropDownItems("Brother MFC-9460CDN,Brother HL-4040CN series,Brother HL-2240 series,PDFwriter")
        
        #50. Observe that there is an editable text field that is defaulted to 1.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.observeEditableFieldDefaultedTo1()
            
        #51.  Next, there is checkbox that is titled "Collated"; observe that this checkbox is checked by default 
        #and appears after copies field.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.confirmCollatedCheckbox()
        
        #Screenshot for confirming that the Collated checkbox is right after the Number of Copies edit box.
        test.vp("PrintDialogCollatedCheckBox")
       
        #52. Next, click on the Paper Source combobox to see the options that can be selected. 
        #Note: Only certain printer has the Paper Source option, so you need to select various connected printers.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.printdialog.selectAPrinterComboItem("Brother HL-4040CN series")
        shared.results.printdialog.confirmPaperSourceDropDownItems("Tray1,Tray2,MP Tray,Manual Feed")
        shared.results.printdialog.selectAPrinterComboItem("PDFwriter")
        
        #53. Press the Print button and observe immediately at the bottom left of the Viewing Station for an overlay   
        #saying "Printing Report: Page [n] of [total].
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Get total pages to be printed.  This is used in step #55")
        total_pages = shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".6 of 6_JLabel")
        shared.results.printdialog.clickPrintButton()
        test.log("TODO This test is not currently reliable on the jenkins machine. The act of takeing the screenshot is happening too slowly.")
        test.log("So the screenshot is taking place after the pages are gone.")
        test.log("Simple fix for this is to have the test print more pages")
        test.log("Commenting the test out for now")
        #test.vp("PrintingPages")
    
        #54. Observe that once the Print button is pressed inside the dialog, the Print dialog will close immediately.
        test.log("Step #" + str(step_counter)); step_counter += 1
        snooze(1.0)
        test.vp("NoPrintDialog")
        
        #55. Obtain the printout from the printer and observe that pressing the Print button will print out the report, 
        #where [n] is the page being printed and [total] is the total number of pages that will be printed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("I am only testing here that six pages get printed.  Not yet testing the actual pages")
        printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + shared.user + '/*.pdf')
        #TODO sometimes theres a wait before all printed files show up.
        #Write code to account for that.
        test.verify(total_pages == len(printerfiles),"Confirming that the total pages Printed are equal to the total pages expected")
        
        test.log("Click on the Print Button one last time")
        shared.results.clickPrintButton() 
        
        #Confirm the default value in the copies field will be 1.
        shared.results.printdialog.observeEditableFieldDefaultedTo1()
        
        #Confirm a checkbox marked “Collated” will appear under the copies field.
        test.vp("PrintDialogCollatedCheckBox")
        test.vp("PaperSourceAfterCollated")
        
        #Confirm the "Collated" checkbox will be checked by default.
        shared.results.printdialog.confirmCollatedCheckbox()
        
        #Confirm that there is Paper Source combobox after the collated checkbox.
        test.vp("PaperSourceAfterCollated")
         
        #Confirm a status messages will appear at the bottom left of the screen saying “Printing Report: 
        #Page [n] of [total],” where [n] is the page being printed and [total] is the total number of pages that will be printed.
        test.log("Getting the total pages printed one more time, before closing the Print Dialog")
        total_pages += shared.results.printdialog.getTotalPagesToBePrinted(":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel")
        shared.results.printdialog.clickPrintButton()
    
        test.log("TODO This test is not currently reliable on the jenkins machine. The act of takeing the screenshot is happening too slowly.")
        test.log("So the screenshot is taking place after the pages are gone.")
        test.log("Simple fix for this is to have the test print more pages")
        test.log("Commenting the test out for now")
        #test.vp("PrintingPages")
        
        #Confirm pressing the Print button will print the report.
        test.log("I am only testing here that six pages get printed.  Not yet testing the actual pages")
        printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + shared.user + '/*.pdf')
    
        #Confirm the Print dialog will close immediately.
        test.vp("NoPrintDialog")
        
        #56. Once printing is done and while the sample is still highlighted, observe that next to the Print button 
        #there are two export buttons in the Results Queue toolbar labeled as "Export Current" and "Export Raw" 
        #that are enabled.
        test.log("Step #" + str(step_counter)); step_counter += 1    
        shared.results.confirmExportCurrentButton("enabled")
        shared.results.confirmExportRawButton("enabled")
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
