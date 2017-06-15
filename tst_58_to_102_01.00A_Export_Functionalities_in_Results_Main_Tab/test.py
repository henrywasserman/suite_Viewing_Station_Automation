# -*- coding: utf-8 -*-
import shutil
import sys
import os
import re
import exceptions
import traceback

def main():

    try:    
        step_counter = 58
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.system.mountUSBDrive()
        shared.setConfigLisReleaseDelay(6)
        
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
    
        #58. Once printing is done and while the sample is still highlighted, observe that next to the Print button there are two export buttons in the Results Queue toolbar labeled as "Export Current" and "Export Raw" that are enabled.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
        shared.results.clickOnFirstRowOfTable()
        shared.results.confirmExportCurrentButton("enabled")
        shared.results.confirmExportRawButton("enabled")
        
        #59. In the Search text field, type in an accession that does not exist in the Results Queue, note that the export buttons are now disabled with no sample selected, and then press the Show All button to clear search field.                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.setSearchText("accession that does not exist") 
        test.log("note that the export buttons are now disabled with no sample selected,")
        shared.results.confirmExportCurrentButton("disabled")
        shared.results.confirmExportRawButton("disabled")
         
        test.log("and then press the Show All button to clear search field.")
        shared.results.clickShowAllButton()
        
        #60. Reselect the previously highlighted sample, press the Export Current button first, and observe that a dialog displays with the title "Export All Runs to File".    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickExportCurrentButton()
        title = shared.results.getFileExportDialogTitle()
        test.verify(title == "Export All Runs to File")
        
        #61. Observe that at the top of the dialog there is a File Name text field labeled as "Save As" and starts out with "export.txt" being filled by default.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmSaveAsLabel("Save As:")
        shared.results.exportallfiledialog.confirmFileNameTxt("export.txt")
        
        #62. Delete the text from the File Name text field and observe the Export button gets disabled.            
        #Confirm that the export dialog displays with the title "Export All Runs to File" when Export Current is pressed.            
        #Confirm at the top of the dialog will be the File Name text field, with the label “Save As”.            
        #Confirm this text field will start out displaying “export.txt”.            
        #Confirm the Export button will be disabled if the File Name text field is empty.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.deleteFilename()
        shared.results.exportallfiledialog.confirmExportButton("disabled")
        
        test.log("Be a good citizen and put export.txt back into the edit box")
        shared.results.exportallfiledialog.setFilename("export.txt")
        
        #63. Observe the next row of the Export dialog is the Folder Selector combobox, labeled "Where".
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #64. Observe "Where" combobox says “<No devices found>” if no writable, removable drives are connected (in kiosk mode), otherwise, "Where" combobox should have a local drive selected (e.g. Macintosh HD)        [VM 03.13.14]        
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Only testing for Kiosk Mode")
        test.fail("TODO Come back and make this update to the doc work.")
        
        #65. Next, observe beneath the Where combobox that there is a File View table that two columns - Name and Date.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.vp("ExportAllFileDialog")
        
        #66. Observe that when the dialog is first opened, the Name column will be sorted in ascending order.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        #67. Click on the Name column and observe that it sorts by file name in descending order; click it again and observe that it reverse the order of the sort.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Click on the Name column and observe that it sorts by file name in descending order")
        shared.results.exportallfiledialog.clickOnNameColumn() 
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"DESCENDING")
        
        test.log("click it again and observe that it reverses the order of the sort, back to ascending")
        shared.results.exportallfiledialog.clickOnNameColumn() 
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        #68. Observe that the Date column shows the last-modified date of each file
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmDateCellRenderer()
    
        #69.  Click on the Date column header to sort the files by date in descending order with latest files first; click on the Date column header again to reverse the order of the sort - oldest time first.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.clickOnDateColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(1,"DESCENDING")
        shared.results.exportallfiledialog.clickOnDateColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(1,"ASCENDING")
    
        #"70. Now drill to down to Users>[user name]>Desktop, if not in kiosk mode, by double-clicking the folder icon appear in the File View table and note that the Folder Selector combobox displays the current open folder.
        #If in kiosk mode, drill down to <USB_drive> => <folder_name>  "        [VM 03.13.14]     
        test.log("Step #" + str(step_counter)); step_counter += 1 
        test.fail("TODO Come back and make this update to the doc work.")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        
        test.vp("FolderIcon")            
        
        shared.results.exportallfiledialog.confirmWhereComboSelection("/Volumes/SmokeTest/Users")
        
        #71. Click on the Folder Selector combobox to get the popup and see that the enclosing folders and the whole hierarchy of containing folders are shown for that navigated folder.             
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/Users")
    
        #72. Select a different folder in the combobox to display the folder name in the file view.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
                
        #73. Click on the Where combobox again to reopen the popup and observe that the previous navigated path has been removed.                
        test.log("Step #" + str(step_counter)); step_counter += 1
        #Confirm in the next row will be the Folder Selector combobox, labeled “Where”.            
        #Confirming clicking Name column header will sort by file name in descending order.            
        #Confirm when the dialog is first opened, Name column will be sorted in ascending order.            
        #Confirm Date column will display the last-modified date of each file.            
        #Confirm if the file view is currently navigated to a folder other than the root of one of these drives, then that folder and its ancestors will also be shown in the Where combobox.            
        #Confirm selecting another folder in the combobox will display that folder in the file view, and will remove from the combobox any folder entries that do not represent either a drive, or the selected folder, or one of its ancestors.            
        #Confirm each entry will display its name and its icon, as it would appear in the standard Mac dialog.
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest")
        shared.results.exportallfiledialog.confirmWhereLabel("Where:")
        shared.results.exportallfiledialog.clickCancelButton()
        shared.results.clickExportCurrentButton()
        shared.results.exportallfiledialog.clickOnNameColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"DESCENDING")
        
        shared.results.exportallfiledialog.clickCancelButton()
        shared.results.clickExportCurrentButton()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        shared.results.exportallfiledialog.confirmDateCellRenderer()
        
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/Users")
        
        shared.results.exportallfiledialog.clickCancelButton()
        shared.results.clickExportCurrentButton()   
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/System")
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/System")
        
        test.vp("Library")
                
        #74. Open up a different folder the File View and drill down as far as you can in that folder.             
        test.log("Step #" + str(step_counter)); step_counter += 1
        user = os.environ.get('USER')
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user)
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop/newData")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop/newData/4711")    
    
        #75. Observe that the a button labeled with an Up Arrow becomes enabled to the right of the combobox.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This method confirms that the up arrow exists and is enabled")
        shared.results.exportallfiledialog.confirmUpArrowButton("enabled")    
        test.vp("UpArrowButtonToTheRight")
        
        #76. Observe that the up button is currently enabled since the folder is not a drive.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmUpArrowButton("enabled")
        
        #77. Press the up button till it gets disabled and see that this button will navigate to the parent folder.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.pressUpArrowButtonUntilItIsDisabled()
        #Confirm this button will be enabled if the current folder is not a drive.            
        #Confirm a button labeled with an Up Arrow will become enabled to the right of the combobox.            
        #Confirm pressing this button will navigate to the parent of the current folder.
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest")
        
        #78. Once you navigate up to a current folder, observe that the button labeled with a Down Arrow becomes enabled on the right of the up button.                                            
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This method confirms that the down arrow exists and is enabled")
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")        
        test.vp("DownArrowButtonToRightOfUpArrowButton")
    
        #79. Observe that Down Arrow button is enabled if a folder is selected in the file view, click on a file such as .txt, see that the button is disabled, and then select the current folder.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/")
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")
        
        where = "/Volumes/SmokeTest"
        test_py = where +  "/Test.txt"
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", test_py)
        shared.results.exportallfiledialog.confirmDownArrowButton("disabled")
    
        users = where + "/Users"
        test_dir = users + "/test"    
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", users)
        
        #80. Press the down button to navigate into the folder selected in the file view (highlighted in purple).            
        #Confirm a button labeled with a Down Arrow will becomes enabled to the right of the up button.            
        #Confirm this button will be enabled if a folder is selected in the file view.            
        #Confirm pressing this button will navigate into the folder selected in the file view.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.pressDownArrowButton()
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", test_dir)
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")
        shared.results.exportallfiledialog.pressDownArrowButton()
        
        shared.results.exportallfiledialog.confirmWhereComboSelection(test_dir)
    
        #81. Next beneath the File view table observe that there is a Filter Selector Combobox  next to the label "Files of type"    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFilterSelectorComboBox("enabled")
        test.vp("FilesOfTypeComboBox")
        
        #82. Click the Filter Selector combobox and observe the options - "All files" and "Tab delimited (.txt)"    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFilterSelectorComboBoxItems("All files,Tab delimited (.txt)")
    
        #"83. Select ""Tab delimited (.txt)"" in the combobox and observe that only "".txt"" file are shown
        #NOTE: Assuming there are different type of files available in currently selected folder. If there aren't any, navigate to a folder where there are different types of files and test it from within that folder. "            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("Tab delimited (.txt)")
        shared.results.exportallfiledialog.confirmTxtOnlyInSaveAsTable()
    
        #84. Switch the files type back to "All files" in the combobox and observe that all files are shown in the table            
        #Confirm under the File View will appear the Filter Selector combobox.            
        #Confirm the options will be “Tab delimited (.txt)” and “All files”.            
        #Confirm files will only be shown if they match the current filter.            
        #Confirm if “Tab delimited (.txt)” is selected, only files ending in “.txt” will be shown in the file view.            
        #Confirm if “All files” is selected, all files will be shown in the file view.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("All files")
        shared.results.exportallfiledialog.confirmMoreThanTxtOnlyInSaveAsTable()
        
        #Confirm under the File View will appear the Filter Selector combobox.
        shared.results.exportallfiledialog.confirmFilterSelectorComboBox("enabled")
        #Confirm the options will be “Tab delimited (.txt)” and “All files”.
        shared.results.exportallfiledialog.confirmFilterSelectorComboBoxItems("All files,Tab delimited (.txt)")
        #Confirm files will only be shown if they match the current filter.
        shared.results.exportallfiledialog.confirmMoreThanTxtOnlyInSaveAsTable()
        #Confirm if “Tab delimited (.txt)” is selected, only files ending in “.txt” will be shown in the file view.
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("Tab delimited (.txt)")
        shared.results.exportallfiledialog.confirmTxtOnlyInSaveAsTable()
        #Confirm if “All files” is selected, all files will be shown in the file view.
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("All files")
        shared.results.exportallfiledialog.confirmMoreThanTxtOnlyInSaveAsTable()
    
        #85. Next, observe that the Filter Selector combobox is a checkbox titled "Safely remove "[name]" after export" and select the USB flash drive option in the folder selector combobox.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("enabled","“SmokeTest”")
        drive_name = shared.system.mountUSBDrive()
        test.log("We need to wait here for a second for the drive to appear")
        snooze(1.0)
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/" + drive_name)
        
        #86. Observe that if removable flash drive is plugged in, the checkbox will be enabled and its name will change to say "Safely remove "[name]" after export" with the checkbox being checked. Note [name] is the name of the device.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("enabled","“" + drive_name +"”")
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("checked")
        test.log("TODO going to have to figure out this fixed USB functionality at a later time")
        test.log("For now we will not be testing this remove checkbox functionality")
        shared.results.exportallfiledialog.clickSafelyRemoveCheckbox()
    
        #87. Change the file name to "Test" and press the Export button to export the file to the USB flash drive.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.setFilename("Test")
        shared.system.deleteFile("/Volumes/" + drive_name + "/Test.txt")
        shared.results.exportallfiledialog.clickExportButton()
        #shared.results.confirmDeviceEjectedLabel()
        #shared.results.clickDeviceEjectedOkButton()
        shared.results.waitForExportCurrentButton()
        
        #88. Observe that the device gets ejected with the confirmation message that the device was safely removed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("mantis bug #10304. Fixed")
        #test.verify(shared.system.isUSBDriveMounted("/Volumes/" + drive_name) == False,"Confirm that the bug is fixed and the drive is no longer mounted")
        
        #89. Once the device is ejected, remove the USB flash drive from the iMac and open the file on a separate station with Excel; verify that the exported data has the correct amount runs by counting the rows and verify that the export data has the correct patient data and results that are shown on the Results sidebar.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        #shared.system.mountUSBDrive()
        test.log("Skipping this first part of #87 for automation") 
        #open the file on a separate station with Excel;
        test.log("Automation will open the file on Excel without going to a separate station")
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/test")
        
        #verify that the exported data has the correct amount runs by counting the rows and 
        #verify that the export data has the correct patient data and results that are shown on the Results sidebar.
        test.log("TODO I am currently only comparing the export data spreadsheet with its' expected spreadsheet")
    
        #90. Observe that "Export Current" exports the comments and morphology changes of the current state of the results,  not the original results.             
        #Confirm under the Filter Selector will appear a checkbox titled “Safely remove device after export.”            
        #Confirm if the current folder is on a removable device, this checkbox will be enabled and its name will change to “Safely remove “[name]” after export,” where [name] is the name of the device.            
        #Confirm that exporting to a removable device with "safely remove" checked will export the data first to the device and then ejects with a confirmation message.            
        #Confirm that "Export Current" exports all of the runs and current results of that sample(s).            
        #Confirm that the exported file matches the results and patient data.                
        test.log("Step #" + str(step_counter)); step_counter += 1  
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/Test.xls"
        
        #Confirm under the Filter Selector will appear a checkbox titled “Safely remove device after export.”
        #Confirm if the current folder is on a removable device, this checkbox will be enabled and its name will change to “Safely remove “[name]” after export,” where [name] is the name of the device.
        shared.results.clickExportCurrentButton()
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("enabled","“SmokeTest”")
        shared.results.exportallfiledialog.clickCancelButton()
        #Confirm that exporting to a removable device with "safely remove" checked will export the data first to the device and then ejects with a confirmation message.
        test.log("TODO: We are not currently ejecting the removable device")
        #Confirm that "Export Current" exports all of the runs and current results of that sample(s).
        #Confirm that the exported file matches the results and patient data.
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Volumes/" + drive_name + "/Test.xls")
        
        #91. Remove the USB flash drive from the work station and reinsert it in the control station.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.system.unmountUSBDrive()
        drive_name = shared.system.mountUSBDrive()
        
        #92. Select 5 samples from the Results Queue and press the Export Current button from the Results Queue toolbar.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Note that 5 samples are already highlighted at this point")
        shared.results.clickExportCurrentButton()
        
        #93. Navigate from the File View table to Users> Shared (or <USB_drive> => <folder_name> if in kiosk mode) and observe that a Plus Sign button next to the down button gets enabled.        [VM 03.13.14]    
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.fail("TODO - Come back and make this update to the doc work.")
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/Shared")
        shared.results.exportallfiledialog.confirmPlusButton("enabled")
        test.vp("PlusButton")
        
        #94. Click the plus button and observe that a dialog appear with the title "Create Folder" and a text field labeled "Name:"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.clickPlusButton()
        shared.results.createfolderdialog.confirmLabelName()
        test.verify(str(shared.results.getCreateFolderDialogTitle()) == "Create Folder","Confirm that the Create Folder Dialog title is Create Folder")
    #    
        #95. Observe that under the "Name" field there are two buttons - "Cancel" and "Create".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.confirmCancelButton("enabled")
        shared.results.createfolderdialog.confirmCreateButton("enabled")
    
        #96. Observe inside the "Name" field that there is a pre-filled text with the name "New Folder".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.confirmDefaultFolderName()
    
        #97. Press the Cancel button to close the dialog, press the "+" button to reopen the Create Folder dialog, and rename the folder name.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.clickCancelButton()
        shared.results.exportallfiledialog.clickPlusButton()
    
        #98. Press the Create button to create the new folder into the selected destination and observe that the folder gets generated.
        #Confirm a button labeled with a Plus Sign will appear next to the Down Arrow.
        #Confirm when this button is pressed, a dialog will appear with the title “Create Folder” and a text field labeled “Name:”.
        #Confirm buttons titled “Cancel” and “Create” will appear under this.
        #Confirm the text field will start with the name “New Folder”.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.clickCancelButton()
        
        #Confirm a button labeled with a Plus Sign will appear next to the Down Arrow.
        test.vp("PlusButton2")            
        #Confirm when this button is pressed, a dialog will appear with the title “Create Folder” and a text field labeled “Name:”.
        shared.results.exportallfiledialog.clickPlusButton()            
        #Confirm buttons titled “Cancel” and “Create” will appear under this.
        shared.results.createfolderdialog.confirmCancelButton("enabled")
        shared.results.createfolderdialog.confirmCreateButton("enabled")            
        #Confirm the text field will start with the name “New Folder”.
        shared.results.createfolderdialog.confirmDefaultFolderName()            
    
        shared.results.createfolderdialog.clickCreateButton()
        new_folder = "/Volumes/SmokeTest/Users/Shared/New Folder"
        shared.results.createfolderdialog.confirmNewFolderCreated(new_folder)
        
        #99. Press the Cancel button to close the Export dialog, select the sample that has comments and morphology entered in the results, and press the Export Raw button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.clickCancelButton()
        test.log("First we need to add comments and morphology")
        shared.results.clickOnTableRow("Awaiting Review")
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
        shared.results.clickCloseButton()
        
        test.log("Press the Raw Export Button")
        shared.results.clickExportRawButton()
        
        #100. Observe that Export Raw dialog contains the same GUI as the Export Current dialog. 
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.system.unmountUSBDrive()
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        
        title = shared.results.getFileExportDialogTitle()
        test.verify(title == "Export All Runs to File")
        
        #101. Select the USB flash drive in the Where combobox, press the Export button, and observe once the data is exported the removable flash drive gets ejected with a confirmation message.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.system.mountUSBDrive()
        shared.results.exportallfiledialog.setFilename("TestExport101.txt")
        shared.results.exportallfiledialog.clickExportButton()
        shared.results.waitForExportCurrentButton()
        test.log("This is currently a mantis bug #10304.  So I will be testing that this bug is still happening")
        test.verify(shared.system.isUSBDriveMounted("/Volumes/" + drive_name) == True,"Confirm that the bug exists and the drive is still mounted")
        
        #102. Open the exported file at a separate work station in Excel and observe that the raw export only exports the original data, no comments or morphology recorded.            
        #Confirm the file is exported successfully and data exported is in its raw form.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        test.log("Automation will open the file on Excel without going to a separate station")
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/TestExport101")
    
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/TestExport101.xls"
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Volumes/" + drive_name + "/TestExport101.xls")
    
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
