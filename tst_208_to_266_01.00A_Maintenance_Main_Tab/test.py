# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try:
        step_counter = 208
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        #shared = Startup("start_display_control_debug_true")
        shared = Startup("VANILLA")
        
        #208. Go to the Maintenance main tab.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.clickTab()
        
        #209. Press the New Special Sample button on the toolbar and view the options on the Profile selector combobox.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.clickNewSpecialSampleButton()
        
        #210. Observe that the complete list of possible profiles will be: Default, DigiCount™, Apheresis, Unstained, and Stained.        [VM 02.27.14]    "(Re) Supravital is out; Apheresis is in. If the tester observes profiles named ""Custom A"" or similar, the Viewing Station has been misconfigured.
        #[VM 02.27.14] - Adjusted."
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.newspecialsampledialog.confirmNewSpecialSampleButton()
        
        #211. Minimize the Viewing Station to windowed mode by control+command+clicking on the Bloodhound Infinity Symbol, log out of the current Kiosk user, and log in to the other station where the ViewingStation.jar file is stored in Applications folder.
        #TODO: Minimizing viewing station and kiosk mode not important at this point.
        #We will come back to this if it becomes an issue.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.vadim.logout()
        
        #212. Right-click on the ViewingStation.jar file, select "Show Package Contents" in the popup menu, and go to Contents>Resources>Java.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This has been handled by starting with start_display_control_debug_true")
        
        #213. Open the bloodhound.properties file in TextEdit and type in the command line: "display.control.debug=true in bloodhound.properties".
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Again This has been handled by starting with start_display_control_debug_true")
    
        #214. Save the changes and relogin to the kiosk user in order to run the Viewing Station.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Again This has been handled by starting with start_display_control_debug_true")
    
        #215. Relogin to the Viewing Station, go to the Maintenance main tab, and press the New Special Sample button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.vadim.login()
        shared.maintenance.clickTab()
        shared.maintenance.clickNewSpecialSampleButton()
        
        #216. Scan in a barcode, press the Save button with the current "Default" profile selected, place this registered sample in Rack position 1 and set it aside.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("TODO for now because there are simulator bar code scan issues")
        test.log("I am just going to type in the barcode number")
        test.log("But I have to get the accession number first")
        accession_number = shared.spritecanvas.moveObjectAndSetAccessionNumber(956,54,956,180)
        shared.selectBloodhoundViewingStation()
        shared.maintenance.newspecialsampledialog.setAccessionNumber(accession_number)
        shared.maintenance.newspecialsampledialog.setAccessionNumberType(accession_number,"Default")
        shared.maintenance.newspecialsampledialog.appendAccessionNumber(accession_number)
        shared.maintenance.newspecialsampledialog.clickSaveButton()
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.moveEmptyRackToTheBelt()
        emptyrack_position = getattr(shared.spritecanvas,"emptyrack_position_1")
        shared.spritecanvas.moveObject(956,180,emptyrack_position[0],emptyrack_position[1])
    
        #217. Press the New Special Sample button again, scan a different barcode, select "DigiCount™" profile in the Profile combobox, press the Save button, and place this registered sample in Rack position 2 and set it aside.        [VM 12.16.13] - We need to scan the barcode here. Otherwise it will not save. Also, do we scan the same bar code as in previous step or new one?    "(N) The tester should scan a different tube (with a different barcode) for steps 216 and 217 here.
        #[VM 02.27.14] - Added."
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.maintenance.clickNewSpecialSampleButton()
        test.log("TODO for now because there are simulator bar code scan issues")
        test.log("I am just going to type in the barcode number")
        test.log("But I have to get the accession number first")
        accession_number = shared.spritecanvas.moveObjectAndSetAccessionNumber(956,54,956,180)
        shared.selectBloodhoundViewingStation()
        shared.maintenance.newspecialsampledialog.setAccessionNumber(accession_number)
        shared.maintenance.newspecialsampledialog.selectProfileItem("DigiCount™")
        shared.maintenance.newspecialsampledialog.setAccessionNumberType(accession_number,"DigiCount™")
        shared.maintenance.newspecialsampledialog.appendAccessionNumber(accession_number)
        shared.maintenance.newspecialsampledialog.clickSaveButton()
        emptyrack_position = getattr(shared.spritecanvas,"emptyrack_position_2")
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.moveObject(956,180,emptyrack_position[0],emptyrack_position[1])
        
        #218. Run the rack on the Analyzer, click to the In Process main tab, and each time the sample is scanned for the first time, select the sample in the In Process Samples List and look at the  sidebar.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.runSampleRack()
        shared.selectBloodhoundViewingStation()
        test.log("TODO for now this dialog does not appear")
        #shared.maintenance.newspecialsampledialog.clickCancelButton()
        shared.inprocess.clickTab()
    
        #"219. Note down the accession number and time and observe that a line displays for each profile saying 
        #""Special sample with the ""<profile_name>"" profile.""."        [VM 02.27.14]    
        #Confirm each run of a sample will use a particular profile.            
        #Confirm New Special Sample dialog displays when pressing New Special Sample button.            
        #Confirm the sample profiles will be defined as those which a user may select to run from a sample tube, through the Special Sample dialog.                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.checkInProcessAccessionNumbers(shared)
        
        #220. Go back to the Maintenance main tab, press the Close Special Sample button, and click on the Barcode combobox.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.clickTab()
        shared.maintenance.clickCloseSpecialSampleButton()
        #shared.maintenance.closespecialsampledialog.clickBarcodeComboBox()
    
        #221. Select a registered special sample barcode in the Close Special Sample dialog and press the Close Sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.closespecialsampledialog.selectComboBoxItem(shared.maintenance.newspecialsampledialog.accession_numbers[0])
        shared.maintenance.closespecialsampledialog.clickCloseSampleButton()
        
        #222. Once the Close Special Sample dialog is closed, press the Run Maintenance Action button in the toolbar and observe the Profile combobox displaying "Prime Stainer" selected by default.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.clickRunMaintenanceActionButton()
        shared.maintenance.runmaintenanceactiondialog.confirmProfileSelected("Prime Stainer")
    
        #223. Press the Run button to initiate prime staining and click to the In Process main tab to look at the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.runmaintenanceactiondialog.clickRunButton()
        shared.inprocess.clickTab()
        
        #224. Select the "(Prime Stainer)" in the In Process Samples list, press the Edit Patient button, and observe that the Patient Information dialog displays "Special sample with 2 repetitions of the "Prime Stainer" profile."
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickOnTableRowByName("Name", "(Prime Stainer)")
        shared.inprocess.clickEditPatientButton()
        test.fail("This is an issue that Vlad is going to adjudicate.  When he lets me know, I will either update the expected results or enter a mantis defect number here.") 
        shared.inprocess.patientinformationdialog.confirmOrderLabelText("Special sample with 2 repetitions of the “Prime Stainer” profile.")
        shared.inprocess.patientinformationdialog.clickCancelButton()
    
        #225. Go back to the Maintenance main tab, press the Bootstrap Population Means button in the toolbar, and observe a dialog displays with the title "Bootstrap Population Means".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.clickTab()
        shared.maintenance.clickBootstrapPopulationMeansButton()
        shared.maintenance.bootstrappopulationmeansdialog.confirmDialogName("Bootstrap Population Means")
        
        #226. Observe the dialog has a Analyzer selector combobox, a "Number of batches" text field with "10" filled by default, and a Reason comment box on the left section of the dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.bootstrappopulationmeansdialog.confirmDefaultControls()
        
        #227. Observe on the right section there is a list of checkboxes that is labeled with a parameter; check the WBC checkbox on.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.bootstrappopulationmeansdialog.setParameterCheckBox("WBC",True)
        
        #228. Type in a comment in the comment box and observe the Bootstrap button gets enabled.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.bootstrappopulationmeansdialog.setReasonsTextArea("This is a comment from automation")
        shared.maintenance.bootstrappopulationmeansdialog.confirmBootstrapButtonEnabled()
        
        #229. Press the Cancel button to close the Bootstrap Population Means dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.bootstrappopulationmeansdialog.clickCancelButton()
        
        #230. Click to the Calibration sub-subtab and observe that at the left is a table of the current calibration factors with the Calibration Factor column set to "1" by default for WBC, RBC, HGB, MCV, PLT, and MPV parameter.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationtab.clickTab()
        shared.maintenance.calibrationtab.confirmDefaultCalibrationFactors()
        
        #231. Observe that there is Save, Revert, Undo and Redo button that are disabled by default unless the calibration factor is changed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationtab.confirmDefaultButtons()
        
        #232. Observe that at the right of the Calibration tab is a table showing the history of how these calibration factors have been updated with the column "Date/Time", "Lot number", "Tech ID", "WBC", "RBC", "HGB", "MCV", "PLT", and "MPV".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationtab.confirmRightTableHeaders()
        
        #233. Observe that at the far right of the table there is an Export and Print button.            
    
        #Confirm the special sample marked for closing is no longer in the Close Special Sample dialog.             
        #Confirm the prime stainer runs with a "Special sample" type  with a "Prime Stainer" profile."            
        #Confirm Bootstrap Population Means dialog displays when the Bootstrap Population Means button is pressed.             
        #Confirm the dialog has a Analyzer selector combobox, a "Number of batches" text field with "10" filled by default, and a Reason comment box on the left section of the dialog.
        #Confirm that the Bootstrap Population Means dialog has a list of checkboxes that is labeled with a parameter on the right section.            
        #Confirm the Calibration sub-subtab has a table of the current calibration factors with the Calibration Factor column set to "1" by default for WBC, RBC, HGB, MCV, PLT, and MPV parameter.            
        #Confirm that the Calibration sub-subtab has a Save, Revert, Undo and Redo button that are disabled by default unless the calibration factor is changed.            
        #Confirm that the Calibration sub-subtab has a table showing the history of how these calibration factors have been updated with the column "Date/Time", "Lot number", "Tech ID", "WBC", "RBC", "HGB", "MCV", "PLT", and "MPV".
        #Confirm that at the far right of the table there is an Export and Print button.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationtab.confirmExportAndPrintButton()
        #Confirm the special sample marked for closing is no longer in the Close Special Sample dialog.
        shared.maintenance.closespecialsampledialog.confirmItemDoesNotExist(shared.maintenance.newspecialsampledialog.accession_numbers[0]) 
        #Confirm the prime stainer runs with a "Special sample" type  with a "Prime Stainer" profile."
        shared.inprocess.clickTab()
        shared.inprocess.checkInProcessAccessionNumbers(shared)
        #Confirm Bootstrap Population Means dialog displays when the Bootstrap Population Means button is pressed.
        shared.maintenance.clickTab()
        shared.maintenance.clickBootstrapPopulationMeansButton()
        shared.maintenance.bootstrappopulationmeansdialog.confirmDialogName("Bootstrap Population Means")     
        #Confirm the dialog has a Analyzer selector combobox, a "Number of batches" text field with "10" filled by default, and a Reason comment box on the left section of the dialog.
        shared.maintenance.bootstrappopulationmeansdialog.confirmDefaultControls()
        shared.maintenance.bootstrappopulationmeansdialog.clickCancelButton()
        #Confirm that the Bootstrap Population Means dialog has a list of checkboxes that is labeled with a parameter on the right section.
        shared.maintenance.bootstrappopulationmeansdialog.setParameterCheckBox("WBC",True)
        #Confirm the Calibration sub-subtab has a table of the current calibration factors with the Calibration Factor column set to "1" by default for WBC, RBC, HGB, MCV, PLT, and MPV parameter.
        shared.maintenance.calibrationtab.clickTab()
        shared.maintenance.calibrationtab.confirmDefaultCalibrationFactors()
        #Confirm that the Calibration sub-subtab has a Save, Revert, Undo and Redo button that are disabled by default unless the calibration factor is changed.
        shared.maintenance.calibrationtab.confirmDefaultButtons()
        #Confirm that the Calibration sub-subtab has a table showing the history of how these calibration factors have been updated with the column "Date/Time", "Lot number", "Tech ID", "WBC", "RBC", "HGB", "MCV", "PLT", and "MPV".
        shared.maintenance.calibrationtab.confirmRightTableHeaders()
        #Confirm that at the far right of the table there is an Export and Print button.
        shared.maintenance.calibrationtab.confirmExportAndPrintButton()
        
        #234. Click to the Calibration Runs sub-subtab and observe a combobox appears at the top left of the page listing the barcode and date of every calibrator run on this Analyzer, including the active run if there is one. Note: If there is no run, the combobox is grayed out.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationrunstab.clickTab()
        shared.maintenance.calibrationrunstab.confirmBlankComboBoxIsDisabled()
            
        #235. Observe that under the run selector the Print and Export buttons.
        #235. Observe that the Print and Export buttons exist under the run selector.
        test.log("Step #" + str(step_counter)); step_counter += 1 
        shared.maintenance.calibrationrunstab.confirmPrintAndExportButtons()
    
        #236. Observe that there are buttons labeled “Save and Close” and “Discard” on the right side of the Calibration Runs sub-subtab, which are disabled if there are no calibrator run. If there are no previous calibration runs, the run selector will be disabled and "Save and Close" button would be "Apply and Close".        [VM 02.27.14]    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationrunstab.confirmDefaultButtonsOnTheRightSide()
        
        #237. Observe that there are buttons labeled “Set up run...” and “Exclude” will appear at the right also with "Exclude" being disabled out if there are no calibrator run. 
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("TODO: This page has changed, wait for the protocol update")
        #shared.maintenance.calibrationrunstab.confirmDefaultSetupRunAndExludeButtons()
    
        #238. Observe that there is a runs table at the bottom of this tab with the first column, titled “Parameter”, listing the same calabratable parameters that are in the Calibration tab.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.calibrationrunstab.confirmDefaultRunTable()
        
        #239. Observe the next two columns are labeled "Target Mean" and “Measured”, where "Measured" is consisted of a set of columns “Mean”, “SD”, and “CV”.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Had to punt here for now, just taking a screenshot to verify")
        
        #240. Observe the last three columns are titled “Old Factor”, "New Factor", and "Applied".            
        #Confirm that a combobox appears at the top left of the Calibration Runs page, listing the barcode and date of every calibrator run on this Analyzer, including the active run if there is one.            
        #Confirm that under the run selector the Print and Export buttons.            
        #Confirm that there are buttons labeled "Apply and Close" and “Discard” on the right side of the Calibration Runs sub-subtab, which are disabled if there are no calibrator run.            
        #Confirm that there are buttons labeled “Set up run...” and “Exclude” will appear at the right also with "Exclude" being grayed out if there are no calibrator run.             
        #Confirm that there is a runs table at the bottom of this tab with the first column, titled “Parameter”, listing the same calabratable parameters that are in the Calibration tab.              
        #Confirm the next two columns are labeled "Target Mean" and “Measured”, where "Measured" is consisted of a set of columns “Mean”, “SD”, and “CV”.            
        #Confirm the last three columns are titled “Old Factor”, "New Factor", and "Applied".
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Had to punt here for now, just taking a screenshot to verify")
        test.vp("Table_Header")
    
        #Confirm that a combobox appears at the top left of the Calibration Runs page, listing the barcode and date of every calibrator run on this Analyzer, including the active run if there is one.
        shared.maintenance.calibrationrunstab.confirmBlankComboBoxIsDisabled()
        #Confirm that under the run selector the Print and Export buttons.
        shared.maintenance.calibrationrunstab.confirmPrintAndExportButtons()
        #Confirm that there are buttons labeled "Apply and Close" and “Discard” on the right side of the Calibration Runs sub-subtab, which are disabled if there are no calibrator run.
        shared.maintenance.calibrationrunstab.confirmDefaultButtonsOnTheRightSide()
        #Confirm that there are buttons labeled “Set up run...” and “Exclude” will appear at the right also with "Exclude" being grayed out if there are no calibrator run.
        test.warning("TODO: These controls have changed waiting for protocol update")
        #shared.maintenance.calibrationrunstab.confirmDefaultSetupRunAndExludeButtons() 
        #Confirm that there is a runs table at the bottom of this tab with the first column, titled “Parameter”, listing the same calabratable parameters that are in the Calibration tab.
        shared.maintenance.calibrationrunstab.confirmDefaultRunTable()  
        #Confirm the next two columns are labeled "Target Mean" and “Measured”, where "Measured" is consisted of a set of columns “Mean”, “SD”, and “CV”.
        #Confirm the last three columns are titled “Old Factor”, "New Factor", and "Applied".
        test.log("Had to punt here for now, just taking a screenshot to verify")
        test.vp("Table_Header")
        
        #241. Eject the fluidics drawer and observe that the Analyzers tab is toggled automatically with the Consumable/Waste Management dialog open.    1/14/14 HT - Amended step 241 - 249    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.analyzers.clickTab()
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.clickFluidicEjectButton()
        shared.selectBloodhoundViewingStation()
        test.log("TODO: analyzer dialog does not appear automaticaly here unless we do this manually")
        test.log("Have to figure out what message is sent when a click happens manually.")
        
        #242. Remove the stain pack (DigiMAC3) and wash solution (DigiWash) from the fluidics drawer first.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.removeReagentPack()
        shared.spritecanvas.removeSystemWash()
        shared.analyzers.consumablewastemanagementdialog.confirmConsumableWasteManagementDialogExists()
         
        #243. Observe that the Consumable/Waste Management dialog highlights the two consumable rows in red.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        test.log("TODO Currently I am not able to get the color from the first row")
        test.log("Need to look into this later")
        #shared.analyzers.consumablewastemanagementdialog.confirmBackgroundColorIsRed("Stain Pack")
        shared.analyzers.consumablewastemanagementdialog.confirmBackgroundColorIsRed("Wash Solution")
        
        #244. Scan in a stain pack barcode, replace them in the fluidics drawer, and perform this same step for the wash solution.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        stain_pack_lot_number = shared.spritecanvas.scanAndReplaceReagentPack()
        wash_solution_lot_number = shared.spritecanvas.scanAndReplaceSystemWash()
        
        #245. Once replacements are performed, close the fluidics drawer and press the "OK" button to close the Consumable/Waste Management dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.closeTheFluidicsDrawer()
        shared.selectBloodhoundViewingStation()
        shared.analyzers.consumablewastemanagementdialog.clickOKButton()
        
        #246. While in the Analyzers main tab, press the Cleaning Solution button in the toolbar and scan in a new cleaning solution barcode.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.analyzers.clickCleaningSolutionButton()
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.scanCleaningSolution()
        
        #247. Press the Replace button in the cleaning solution dialog, run the cleaning solution via rack mode, and wait for the new bleach to be replaced into the bleach pocket.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.analyzers.cleaningsolutiondialog.clickReplaceButton() 
        shared.analyzers.analyzereventsdialog.clickHideButton()
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.moveEmptyRackToTheBelt()
        accession_number = shared.spritecanvas.moveObjectAndSetAccessionNumber(957,428,330,177)
        shared.spritecanvas.runSampleRack()
    
        #248. Next, click to the Consumable History sub-subtab under Maintenance main tab and observe the first section in the tab contains a date widget that allows the consumable history report to search and display the consumable record in that time period.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.maintenance.clickTab()
        shared.maintenance.consumablehistorytab.clickTab()
        shared.maintenance.consumablehistorytab.confirmDateWidget()
    
        #249. Press the Search button with the defaulted current date filled and observe that all the logged data that were recorded on the system during that search time period are filled in the DigiMAC, DigiWash, DigiClean, and DigiMAC3 Reticulocyte Stain table.        [VM 02.27.14]
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.consumablehistorytab.clickSearchButton()
        accession_number = shared.spritecanvas.getAccessionNumber(445,123)
        test.log("TODO find out why digi_clean_solution is no longer appearing in the table here.")
        #digi_clean_solution_lot_number = shared.maintenance.consumablehistorytab.accessionToLotNumber(accession_number)
        shared.selectBloodhoundViewingStation()
        shared.maintenance.consumablehistorytab.confirmDigiMacTableData(stain_pack_lot_number)
        shared.maintenance.consumablehistorytab.confirmDigiWashTableData(wash_solution_lot_number)
        #shared.maintenance.consumablehistorytab.confirmDigiCleanSolutionTableData(digi_clean_solution_lot_number)
    
        #250. Observe that the consumable replacement is recorded into the five column headers, starting from left to right - "Install Date", "Lot Number", "Exp Date (Open)", "Exp Date (Closed)", and "Tech ID" in each one of the four tables.    
        #250. Observe that the consumable replacement is recorded into the five column headers, starting from left to right - "Install Date", "Lot Number", "Exp Date (Open)", "Exp Date (Closed)", and "Tech ID" in each one of the three tables.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.consumablehistorytab.confirmDigiCleanSolutionHeaders()
        shared.maintenance.consumablehistorytab.confirmDigiMac3StainPackHeaders()
        shared.maintenance.consumablehistorytab.confirmDigWashSolutionHeaders()
        shared.maintenance.consumablehistorytab.confirmDigiMac3ReticulocyteHeaders()
        
        #251. Verify that the reported consumable records are correct and then press the Consumable History Report button to open the "Consumable History Log" print dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.consumablehistorytab.confirmDigiMacTableData(stain_pack_lot_number)
        shared.maintenance.consumablehistorytab.confirmDigiWashTableData(wash_solution_lot_number)
        #shared.maintenance.consumablehistorytab.confirmDigiCleanSolutionTableData(digi_clean_solution_lot_number)
        shared.maintenance.consumablehistorytab.clickConsumableHistoryReportButton()
    
        #252. Click and drag in the preview section as you would on any other print preview dialog and see that information here matches what was shown in the consumable history table precisely.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.vp("ConsumableHistoryLog")
    
        #253. Press the Print button in the dialog to proceed with printing.            
        #Confirm the first top two items under the Consumable History tab will display the consumable records (DigiMAC™ and DigiWash™) that were logged on the system, as specified by the date range, and will match the consumable history report precisely.             
        #Confirm the bottom two tables in the consumable history tab will be the DigiClean™ Solution; this section will behave like the two other consumable tables.            
        #Confirm Consumable History Report button will bring up the consumable report dialog, titled "Consumable History Log" and has the same functionalities as any other print preview dialog.            
        #Confirm the date widget in the consumable history table allows the consumable history report to search and display the consumable record in that specified date range.
    
        #Confirm the first top two items under the Consumable History tab will display the consumable records (DigiMAC™ and DigiWash™) that were logged on the system, as specified by the date range, and will match the consumable history report precisely.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.consumablehistoryprintdialog.selectPrinterItem("PDFwriter")
        shared.maintenance.consumablehistoryprintdialog.clickPrintButton()
        test.log("TODO: When time allows we will implement the PDF print compare process with masking - about 1 day of work")
     
        #Confirm the bottom two tables in the consumable history tab will be the DigiClean™ Solution; this section will behave like the two other consumable tables.
        test.log("Step #" + str(step_counter)); step_counter += 1
        #shared.maintenance.consumablehistorytab.confirmDigiCleanSolutionTableData(digi_clean_solution_lot_number)
        
        #Confirm Consumable History Report button will bring up the consumable report dialog, titled "Consumable History Log" and has the same functionalities as any other print preview dialog.
        shared.maintenance.consumablehistorytab.clickConsumableHistoryReportButton()
        test.vp("ConsumableHistoryLog")
        shared.maintenance.consumablehistoryprintdialog.clickCancelButton()
        
        #Confirm the date widget in the consumable history table allows the consumable history report to search and display the consumable record in that specified date range.
        shared.maintenance.consumablehistorytab.clickSearchButton()
        shared.maintenance.consumablehistorytab.confirmDigiMacTableData(stain_pack_lot_number)
        shared.maintenance.consumablehistorytab.confirmDigiWashTableData(wash_solution_lot_number)
        #shared.maintenance.consumablehistorytab.confirmDigiCleanSolutionTableData(digi_clean_solution_lot_number)
        
        #254. Click to the next sub-subtab - Event Logs
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.eventlogstab.clickTab()
        
        #255. Observe the Event Logs tab has text fields to set the date range and a button to search for all logs in that range.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.eventlogstab.confirmDateTextFields()
        
        #256. Observe that the  data range is defaulted to the current day.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.eventlogstab.confirmDataRangeDefaultedToCurrentDay()
        
        #257. Observe that there are three buttons at the top right corner, after the date range, "Search", "Export" and "Print Event Log" button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.eventlogstab.confirmSearchButton()
        shared.maintenance.eventlogstab.confirmExportButton()
        shared.maintenance.eventlogstab.confirmPrintEventLogButton()
    
        #258. Press the Search button with the default date listed and observe that upon searching, the table will fill in with log data.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.eventlogstab.clickSearchButton()
        shared.maintenance.eventlogstab.confirmLogDataExists()
        
        #259. Observe that the filled columns in the table are: Code, Name, Message, Timestamp, Severity, and Details.            
        #Confirm the Event Logs tab has text fields to set the date range and a button to search for all logs in that range.             
        #Confirm that the  data range is defaulted to the current day.             
        #Confirm that there are three buttons at the top right corner, after the date range, "Search", "Export" and "Print Event Log" button.            
        #Confirm that upon searching, the table will fill in with log data.             
        #Confirm that the filled columns in the table are: Code, Name, Message, Timestamp, Severity, and Details.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.eventlogstab.confirmTableHeaders()        
        #Confirm the Event Logs tab has text fields to set the date range and a button to search for all logs in that range.
        shared.maintenance.eventlogstab.confirmDateTextFields()
        shared.maintenance.eventlogstab.confirmSearchButton()
        #Confirm that the  data range is defaulted to the current day.
        shared.maintenance.eventlogstab.confirmDataRangeDefaultedToCurrentDay()
        #Confirm that there are three buttons at the top right corner, after the date range, "Search", "Export" and "Print Event Log" button.        
        shared.maintenance.eventlogstab.confirmSearchButton()
        shared.maintenance.eventlogstab.confirmExportButton()
        shared.maintenance.eventlogstab.confirmPrintEventLogButton()
        #Confirm that upon searching, the table will fill in with log data.
        shared.maintenance.eventlogstab.confirmLogDataExists()         
        #Confirm that the filled columns in the table are: Code, Name, Message, Timestamp, Severity, and Details.
        shared.maintenance.eventlogstab.confirmTableHeaders()
        
        #260. Click to the next sub-subtab - Usage History.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.clickTab()
      
        #261. Observe the Usage History tab has text field to search the usage history recorded by the username.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.confirmUsernameTextField()
    
        #262. Observe the Usage History tab has a text fields to set the date range and a button to search for all logs in that range.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.confirmDateTextFields()
        
        #263. Observe that the  data range is defaulted to the current day.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.confirmDataRangeDefaultedToCurrentDay()
    
        #264. Observe that there are three buttons at the top right corner, after the date range, "Search", "Export" and "Print Usage History" button.#
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.confirmSearchButton()
        shared.maintenance.usagehistorytab.confirmExportButton()
        shared.maintenance.usagehistorytab.confirmPrintUsageHistoryButton()
        
        #265. Type in your username in the Username text field and press the Search button with the default date listed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.setUsername(shared)
        shared.maintenance.usagehistorytab.clickSearchButton()
            
        #266. Observe that upon searching, the usage logged data will be filled in the columns in the table - Code, Username,  Timestamp, and Details.            
        #Confirm on the Usage History page, counters will appear giving information on how many runs of various types have been done.            
        #Confirm the Usage History tab has text field for username to be entered to filter search by username.            
        #Confirm the Usage History tab has text fields to set the date range and a button to search for all logs in that range.             
        #Confirm that the  data range is defaulted to the current day.             
        #Confirm that there are three buttons at the top right corner, after the date range, "Search", "Export" and "Print Event Log" button.            
        #Confirm that upon searching, the table will fill in with log data.             
        #Confirm that the filled columns in the table are: Code, Name, Message, Timestamp, Severity, and Details.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.maintenance.usagehistorytab.confirmTableData()
        #Confirm on the Usage History page, counters will appear giving information on how many runs of various types have been done.
        shared.maintenance.usagehistorytab.confirmResultsLabel()
        #Confirm the Usage History tab has text field for username to be entered to filter search by username.
        shared.maintenance.usagehistorytab.confirmUsernameTextField()
        #Confirm the Usage History tab has text fields to set the date range and a button to search for all logs in that range.
        shared.maintenance.usagehistorytab.confirmDateTextFields()         
        #Confirm that the  data range is defaulted to the current day.
        shared.maintenance.usagehistorytab.confirmDataRangeDefaultedToCurrentDay()
        #Confirm that there are three buttons at the top right corner, after the date range, "Search", "Export" and "Print Usage History Log" button.
        shared.maintenance.usagehistorytab.confirmSearchButton()
        shared.maintenance.usagehistorytab.confirmExportButton()
        shared.maintenance.usagehistorytab.confirmPrintUsageHistoryButton()        
        #Confirm that upon searching, the table will fill in with log data.
        shared.maintenance.usagehistorytab.clickSearchButton()
        shared.maintenance.usagehistorytab.confirmResultsLabel()
        #Confirm that the filled columns in the table are: Code, Name, Message, Timestamp, Severity, and Details.
        shared.maintenance.usagehistorytab.confirmTableHeaders()
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
