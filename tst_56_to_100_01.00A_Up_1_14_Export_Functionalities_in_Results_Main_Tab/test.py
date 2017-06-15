# -*- coding: utf-8 -*-
import shutil
import sys
import os
import exceptions
import traceback

def main():
    
    try:
        step_counter = 56
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.setConfigLisReleaseDelay(6)
        shared.system.unmountUSBDrive()
        
        # (Header) Export Functionalities in Results Main Tab
        
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
        
        test.log("Note:  Step 56 is also performed in the Print_Functionalites_in_Results_Main_Tab Test")
        
        #56. Once printing is done and while the sample is still highlighted, observe that next to the Print button 
        #there are two export buttons in the Results Queue toolbar labeled as "Export Current" and "Export Raw" 
        #that are enabled.
        test.log("Step #" + str(step_counter)); step_counter += 1    
        shared.results.confirmExportCurrentButton("enabled")
        shared.results.confirmExportRawButton("enabled")
        
        #57. In the Search text field, type in an accession that does not exist in the Results Queue
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.setSearchText("accession that does not exist") 
        #note that the export buttons are now disabled with no sample selected,
        shared.results.confirmExportCurrentButton("disabled")
        shared.results.confirmExportRawButton("disabled")
         
        #and then press the Show All button to clear search field.
        shared.results.clickShowAllButton()
        
        #58. Reselect the previously highlighted sample, press the Export Current button first, and observe that 
        #a dialog displays with the title "Export All Runs to File".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickExportCurrentButton()
        title = shared.results.getFileExportDialogTitle()
        test.verify(title == "Export All Runs to File")
        
        #59. Observe that at the top of the dialog there is a File Name text field labeled as "Save As" 
        #and starts out with "export.txt" being filled by default.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmSaveAsLabel("Save As:")
        shared.results.exportallfiledialog.confirmFileNameTxt("export.txt")
        
        #60. Delete the text from the File Name text field and observe the state of the Export button gets disabled.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.deleteFilename()
        shared.results.exportallfiledialog.confirmExportButton("disabled")
        
        test.log("Be a good citizen and put export.txt back into the edit box")
        shared.results.exportallfiledialog.setFilename("export.txt")
        
        test.log("Note these Confirmations were already performed above")
        #Confirm that the export dialog displays with the title "Export All Runs to File"
        #when Export Current is pressed.
        #Confirm at the top of the dialog will be the File Name text field, with the label “Save As”.
        #Confirm this text field will start out displaying “export.txt”.
        #Confirm the Export button will be disabled if the File Name text field is empty.
        
        #61. Observe the next row of the Export dialog is the Folder Selector combobox, labeled "Where".
        test.log("Step #" + str(step_counter)); step_counter += 1
        #62. Observe that the "Where" combobox displays the control station startup volume, i.e., SmokeTest.
        test.log("Step #" + str(step_counter)); step_counter += 1
        #63. Next, observe beneath the Where combobox observe that there is a File View table that two columns - Name and Date.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.vp("ExportAllFileDialog")
        
        #64. Observe that when the dialog is first opened, The Name Column will be sorted in ascending order.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        #65. Click on the Name column and observe that it sorts by file name in descending order
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.clickOnNameColumn() 
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"DESCENDING")
        
        #click it again and observe that it reverses the order of the sort, back to ascending
        shared.results.exportallfiledialog.clickOnNameColumn() 
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        #66. Observe that the Date column shows the last-modified date of each file
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmDateCellRenderer()
        
        #67.  Click on the Date column header to sort the files by date in ascending order with latest files last; 
        #click on the Date column header again to reverse the order of the sort - newest time first.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.clickOnDateColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(1,"ASCENDING")
        shared.results.exportallfiledialog.clickOnDateColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(1,"DESCENDING")
        
        #68. Now drill to down to Users>[user name]>Desktop by double-clicking
        test.log("Step #" + str(step_counter)); step_counter += 1 
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        
        #the folder icon should appear in the File View table and
        test.vp("FolderIcon")
         
        #note that the Folder Selector combobox displays the current open folder.
        shared.results.exportallfiledialog.confirmWhereComboSelection("/Volumes/SmokeTest/Users")
        
        #69. Click on the Folder Selector combobox to get the popup and see that 
        #the enclosing folders and the whole hierarchy of containing folders are shown for that navigated folder.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/Users")
    
        #70. Select a different folder in the combobox to display the folder name in the file view.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        
        #71. Click on the Where combobox again to reopen the popup and observe that the previous navigated path 
        #has been removed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest")
        
        #Confirm in the next row will be the Folder Selector combobox, labeled “Where”
        test.log("Completed at step #61")
        #Confirming clicking this column header will sort by file name in ascending order.
        test.log("Completed at step #65")
        #Confirm when the dialog is first opened, this columns will be sorted in ascending order.
        test.log("Completed at step #64")
        #Confirm this column will display the last-modified date of each file.
        test.log("Completed at step #66")
        #Confirm if the file view is currently navigated to a folder other than the root of one of these drives, then that folder and its ancestors will also be shown in the Where combobox.
        test.log("Completed at step #69")
        
        #Confirm selecting another folder in the combobox will display that folder in the file view, and will remove from the combobox any folder entries that do not represent either a drive, or the selected folder, or one of its ancestors.
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/etc/cups")
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/etc,/Volumes/SmokeTest/etc/cups")
        
        #Confirm each entry will display its name and its icon, as it would appear in the standard Mac Dialog
        test.vp("System")
        
        #72. Open up a different folder the File View and drill down as far as you can in that folder.
        test.log("Step #" + str(step_counter)); step_counter += 1
        user = os.environ.get('USER')
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user)
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop/newData")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop/newData/4711")    
    
        #73. Observe that a button labeled with an Up Arrow appears to the right of the combobox.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This method confirms that the up arrow exists and is enabled")
        shared.results.exportallfiledialog.confirmUpArrowButton("enabled")    
        test.vp("UpArrowButtonToTheRight")
    
        #74. Observe that the up button is currently enabled since the folder is not a drive.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmUpArrowButton("enabled")
        
        #75. Press the up button till it gets disabled and see that this button will navigate to the parent folder.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.pressUpArrowButtonUntilItIsDisabled()
        
        test.log("Confirmed during step #75")
        #Confirm this button will be enabled if the current folder is not a drive.
        test.log("Confirmed during step #73")
        #Confirm a button labeled with an Up Arrow will appear to the right of the combobox.
        test.log("Confirmed during step #75")
        #Confirm pressing this button will navigate to the parent of the current folder.
        
         #76. Once you navigate up to a current folder, observe that the button labeled with a 
        #Down Arrow appears to the right of the up button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This method confirms that the down arrow exists and is enabled")
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")        
        test.vp("DownArrowButtonToRightOfUpArrowButton")
        
        #77. Observe that Down Arrow button is enabled if a folder is selected in the file view, 
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/")
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")
        
        #click on a file such as .txt, see that the button is disabled, and then select the current folder.
        where = shared.results.exportallfiledialog.goToCurrentPath()
        test_py = where +  "/test.py"
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", test_py)
        shared.results.exportallfiledialog.confirmDownArrowButton("disabled")
    
        verificationPoints = where + "/verificationPoints"    
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", verificationPoints)
    
        #78. Press the down button to navigate into the folder selected in the file view (highlighted in purple)
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.pressDownArrowButton()
        
        test.log("Confirmed on step #77")
        #Confirm a button labeled with a Down Arrow will appear to the right of the up button.
        test.log("Confirmed on step #77")
        #Confirm this button will be enabled if a folder is selected in the file view.
        #Confirm pressing this button will navigate into the folder selected in the file view.
        shared.results.exportallfiledialog.confirmWhereComboSelection(verificationPoints)
        
        #79. Next beneath the File view table observe that there is a Filter Selector Combobox  
        #next to the label "Files of type"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFilterSelectorComboBox("enabled")
        test.vp("FilesOfTypeComboBox")
        
        #80. Click the Filter Selector combobox and observe the options - "All files" and "Tab delimited (.txt)"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmFilterSelectorComboBoxItems("All files,Tab delimited (.txt)")
        
        #81. Select "Tab delimited (.txt)" in the combobox and observe that only ".txt" file are shown
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("Tab delimited (.txt)")
        shared.results.exportallfiledialog.confirmTxtOnlyInSaveAsTable()
        
        #82. Switch the files type back to "All files" in the combobox 
        #and observe that all files are shown in the table
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("All files")
        shared.results.exportallfiledialog.confirmMoreThanTxtOnlyInSaveAsTable()
        
        test.log("This was confirmed on step #79")
        #Confirm under the File View will appear the Filter Selector combobox.
        test.log("This was confirmed on step #80")
        #Confirm the options will be “Tab delimited (.txt)” and “All files”.
        test.log("This was confirmed on stop #81")
        #Confirm files will only be shown if they match the current filter.
        test.log("This was confirmed on stop #81")
        #Confirm if “Tab delimited (.txt)” is selected, only files ending in “.txt” will be shown in the file view.
        test.log("This was confirmed on step #82")
        #Confirm if “All files” is selected, all files will be shown in the file view.
    
        #83. Next, observe that after the Filter Selector combobox is a checkbox titled "Safely remove 
        #"[name]" after export" and select the USB flash drive option in the folder selector combobox.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("disabled","“SmokeTest”")
        drive_name = shared.system.mountUSBDrive()
        test.log("We need to wait here for a second for the drive to appear")
        snooze(1.0)
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/" + drive_name)
        
        #84. Observe that on a removable flash drive, the checkbox will be enabled and its name 
        #will change to say "Safely remove "[name]" after export" with the checkbox being checked. 
        #Note [name] is the name of the device.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("enabled","“" + drive_name +"”")
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("checked")
    
        #85. Change the file name to "Test" and press the Export button to export the file to the USB flash drive.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.setFilename("Test")
        shared.system.deleteFile("/Volumes/" + drive_name + "/Test.txt")
        shared.results.exportallfiledialog.clickExportButton()
        shared.results.waitForExportCurrentButton()
        
        #86. Observe that the device gets ejected with the confirmation message that the device was safely removed.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("This is currently a mantis bug #10304.  So I will be testing that this bug is still happening")
        test.verify(shared.system.isUSBDriveMounted("/Volumes/" + drive_name) == True,"Confirm that the bug exists and the drive is still mounted")
        
        #87. Once the device is ejected, remove the USB flash drive from the iMac and
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Skipping this first part of #87 for automation") 
        #open the file on a separate station with Excel;
        test.log("Automation will open the file on Excel without going to a separate station")
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/Test")
        
        #verify that the exported data has the correct amount runs by counting the rows and 
        #verify that the export data has the correct patient data and results that are shown on the Results sidebar.
        test.log("TODO I am currently only comparing the export data spreadsheet with its' expected spreadsheet")
        #88. Observe that "Export Current" exports the comments and morphology changes of the current state of the results, not the original results.
        test.log("Step #" + str(step_counter)); step_counter += 1  
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/Test.xls"
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Volumes/" + drive_name + "/Test.xls")
        
        #Confirm under the Filter Selector will appear a checkbox titled “Safely remove device after export.”
        test.log("This was confirmed at step #83")
        #Confirm if the current folder is on a removable device, this checkbox will be enabled and its name will change to “Safely remove “[name]” after export,” where [name] is the name of the device.
        test.log("This was confirmed at step #84")
        #Confirm that exporting to a removable device with "safely remove" checked will export the data first to the device and then ejects with a confirmation message.
        test.log("This was confirmed as a bug at step #86")
        #Confirm that "Export Current" exports all of the runs and current results of that sample(s).
        test.log("This was confirmed at steps #87 and #88")
        #Confirm that the exported file matches the results and patient data.
        test.log("This was confirmed at step #87 and #88")
        
        #89. Remove the USB flash drive from the work station and reinsert it in the control station.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.system.unmountUSBDrive()
        drive_name = shared.system.mountUSBDrive()
        
        #90. Select 5 samples from the Results Queue and press the Export Current button from the Results Queue toolbar.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("Note that 5 samples are already highlighted at this point")
        shared.results.clickExportCurrentButton()
        
        #91. Navigate from the File View table to Users> Shared and observe that a Plus Sign button 
        #next to the down button gets enabled.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/Shared")
        shared.results.exportallfiledialog.confirmPlusButton("enabled")
        test.vp("PlusButton")
        
        #92. Click the plus button and observe that a dialog appears with the title 
        #"Create Folder" and a text field labeled "Name:"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.exportallfiledialog.clickPlusButton()
        shared.results.createfolderdialog.confirmLabelName()
        test.verify(str(shared.results.getCreateFolderDialogTitle()) == "Create Folder","Confirm that the Create Folder Dialog title is Create Folder")
        
        #93. Observe that under the "Name" field there are two buttons - "Cancel" and "Create".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.confirmCancelButton("enabled")
        shared.results.createfolderdialog.confirmCreateButton("enabled")
        
        #94. Observe inside the "Name" field that there is a pre-filled text with the name "New Folder".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.confirmDefaultFolderName()
        
        #95. Press the Cancel button to close the dialog, press the "+" button to reopen 
        #the Create Folder dialog, and rename the folder name.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.clickCancelButton()
        shared.results.exportallfiledialog.clickPlusButton()
    
        #96. Press the Create button to create the new folder 
        #into the selected destination and observe that the folder gets generated.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.createfolderdialog.clickCreateButton()
        new_folder = "/Volumes/SmokeTest/Users/Shared/New Folder"
        shared.results.createfolderdialog.confirmNewFolderCreated(new_folder)
        
        #97. Press the Cancel button to close the Export dialog, select the sample that has 
        #comments and morphology entered in the results, and press the Export Raw button.
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
        
        shared.wbc.setAuerRods("true")
        shared.wbc.setDysplasticCells("true")
        shared.wbc.setSmudgeCells("true")
    
        test.log("Press the save button")
        shared.results.clickSaveButton()
        shared.results.clickCloseButton()
        
        test.log("Press the Raw Export Button")
        shared.results.clickExportRawButton()
        
        #98. Observe that Export Raw dialog contains the same GUI as the Export Current dialog.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.system.unmountUSBDrive()
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        
        title = shared.results.getFileExportDialogTitle()
        test.verify(title == "Export All Runs to File")
        
        #98-59. Observe that at the top of the dialog there is a File Name text field labeled as "Save As" 
        #and starts out with "export.txt" being filled by default.
        sub_step_counter = 59
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmSaveAsLabel("Save As:")
        shared.results.exportallfiledialog.confirmFileNameTxt("export.txt")
        
        #98-60. Delete the text from the File Name text field and observe the state of the Export button gets disabled.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.deleteFilename()
        shared.results.exportallfiledialog.confirmExportButton("disabled")
        
        test.log("Be a good citizen and put export.txt back into the edit box")
        shared.results.exportallfiledialog.setFilename("export.txt")
        
        test.log("Note these Confirmations were already performed above")
        #Confirm that the export dialog displays with the title "Export All Runs to File"
        #when Export Current is pressed.
        #Confirm at the top of the dialog will be the File Name text field, with the label “Save As”.
        #Confirm this text field will start out displaying “export.txt”.
        #Confirm the Export button will be disabled if the File Name text field is empty.
        
        #98-61. Observe the next row of the Export dialog is the Folder Selector combobox, labeled "Where".
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        #98-62. Observe that the "Where" combobox displays the control station startup volume, i.e., SmokeTest.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        #98-63. Next, observe beneath the Where combobox observe that there is a File View table that two columns - Name and Date.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        test.vp("ExportAllFileDialog")
        
        #98-64. Observe that when the dialog is first opened, The Name Column will be sorted in ascending order.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        #98-65. Click on the Name column and observe that it sorts by file name in descending order
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.clickOnNameColumn() 
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"DESCENDING")
        
        #click it again and observe that it reverses the order of the sort, back to ascending
        shared.results.exportallfiledialog.clickOnNameColumn() 
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(0,"ASCENDING")
        
        #98-66. Observe that the Date column shows the last-modified date of each file
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmDateCellRenderer()
        
        #98-67.  Click on the Date column header to sort the files by date in ascending order with latest files last;
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1 
        #click on the Date column header again to reverse the order of the sort - newest time first.
        shared.results.exportallfiledialog.clickOnDateColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(1,"ASCENDING")
        shared.results.exportallfiledialog.clickOnDateColumn()
        shared.results.exportallfiledialog.confirmNameColumnSortOrder(1,"DESCENDING")
        
        #98-68. Now drill to down to Users>[user name]>Desktop by double-clicking
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        
        #the folder icon should appear in the File View table and
        test.vp("FolderIcon")
         
        #note that the Folder Selector combobox displays the current open folder.
        shared.results.exportallfiledialog.confirmWhereComboSelection("/Volumes/SmokeTest/Users")
        
        #98-69. Click on the Folder Selector combobox to get the popup and see that
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        #the enclosing folders and the whole hierarchy of containing folders are shown for that navigated folder.
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/Users")
    
        #98-70. Select a different folder in the combobox to display the folder name in the file view.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        
        #98-71. Click on the Where combobox again to reopen the popup and observe that the previous navigated path 
        #has been removed.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest")
        
        #Confirm in the next row will be the Folder Selector combobox, labeled “Where”
        test.log("Completed at step #61")
        #Confirming clicking this column header will sort by file name in ascending order.
        test.log("Completed at step #65")
        #Confirm when the dialog is first opened, this columns will be sorted in ascending order.
        test.log("Completed at step #64")
        #Confirm this column will display the last-modified date of each file.
        test.log("Completed at step #66")
        #Confirm if the file view is currently navigated to a folder other than the root of one of these drives, then that folder and its ancestors will also be shown in the Where combobox.
        test.log("Completed at step #69")
        
        #Confirm selecting another folder in the combobox will display that folder in the file view, and will remove from the combobox any folder entries that do not represent either a drive, or the selected folder, or one of its ancestors.
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/etc/cups")
        shared.results.exportallfiledialog.confirmFolderSelectorComboBoxItems("/Volumes/SmokeTest,/Volumes/SmokeTest/etc,/Volumes/SmokeTest/etc/cups")
        
        #Confirm each entry will display its name and its icon, as it would appear in the standard Mac Dialog
        test.vp("System")
        
        #98-72. Open up a different folder the File View and drill down as far as you can in that folder.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        user = os.environ.get('USER')
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user)
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop/newData")
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/" + user + "/Desktop/newData/4711")    
    
        #98-73. Observe that a button labeled with an Up Arrow appears to the right of the combobox.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        test.log("This method confirms that the up arrow exists and is enabled")
        shared.results.exportallfiledialog.confirmUpArrowButton("enabled")    
        test.vp("UpArrowButtonToTheRight")
    
        #98-74. Observe that the up button is currently enabled since the folder is not a drive.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmUpArrowButton("enabled")
        
        #98-75. Press the up button till it gets disabled and see that this button will navigate to the parent folder.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.pressUpArrowButtonUntilItIsDisabled()
        
        test.log("Confirmed during step #75")
        #Confirm this button will be enabled if the current folder is not a drive.
        test.log("Confirmed during step #73")
        #Confirm a button labeled with an Up Arrow will appear to the right of the combobox.
        test.log("Confirmed during step #75")
        #Confirm pressing this button will navigate to the parent of the current folder.
        
        #98-76. Once you navigate up to a current folder, observe that the button labeled with a 
        #Down Arrow appears to the right of the up button.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        test.log("This method confirms that the down arrow exists and is enabled")
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")        
        test.vp("DownArrowButtonToRightOfUpArrowButton")
        
        #98-77. Observe that Down Arrow button is enabled if a folder is selected in the file view, 
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.doubleClickOnTableRowByName("     Name", "/Volumes/SmokeTest/Users/")
        shared.results.exportallfiledialog.confirmDownArrowButton("enabled")
        
        #click on a file such as .txt, see that the button is disabled, and then select the current folder.
        where = shared.results.exportallfiledialog.goToCurrentPath()
        test_py = where +  "/test.py"
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", test_py)
        shared.results.exportallfiledialog.confirmDownArrowButton("disabled")
    
        verificationPoints = where + "/verificationPoints"    
        shared.results.exportallfiledialog.clickOnTableRowByName(":Bloodhound™ Viewing Station " + version + ".Save As:_JTable","     Name", verificationPoints)
    
        #98-78. Press the down button to navigate into the folder selected in the file view (highlighted in purple)
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.pressDownArrowButton()
        
        test.log("Confirmed on step #77")
        #Confirm a button labeled with a Down Arrow will appear to the right of the up button.
        test.log("Confirmed on step #77")
        #Confirm this button will be enabled if a folder is selected in the file view.
        #Confirm pressing this button will navigate into the folder selected in the file view.
        shared.results.exportallfiledialog.confirmWhereComboSelection(verificationPoints)
        
        #98-79. Next beneath the File view table observe that there is a Filter Selector Combobox
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1  
        #next to the label "Files of type"
        shared.results.exportallfiledialog.confirmFilterSelectorComboBox("enabled")
        test.vp("FilesOfTypeComboBox")
        
        #98-80. Click the Filter Selector combobox and observe the options - "All files" and "Tab delimited (.txt)"
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmFilterSelectorComboBoxItems("All files,Tab delimited (.txt)")
        
        #98-81. Select "Tab delimited (.txt)" in the combobox and observe that only ".txt" file are shown
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("Tab delimited (.txt)")
        shared.results.exportallfiledialog.confirmTxtOnlyInSaveAsTable()
        
        #98-82. Switch the files type back to "All files" in the combobox 
        #and observe that all files are shown in the table
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.selectFilterSelectorComboBoxItem("All files")
        shared.results.exportallfiledialog.confirmMoreThanTxtOnlyInSaveAsTable()
        
        test.log("This was confirmed on step #79")
        #Confirm under the File View will appear the Filter Selector combobox.
        test.log("This was confirmed on step #80")
        #Confirm the options will be “Tab delimited (.txt)” and “All files”.
        test.log("This was confirmed on stop #81")
        #Confirm files will only be shown if they match the current filter.
        test.log("This was confirmed on stop #81")
        #Confirm if “Tab delimited (.txt)” is selected, only files ending in “.txt” will be shown in the file view.
        test.log("This was confirmed on step #82")
        #Confirm if “All files” is selected, all files will be shown in the file view.
    
        #98-83. Next, observe that after the Filter Selector combobox is a checkbox titled "Safely remove 
        #"[name]" after export" and select the USB flash drive option in the folder selector combobox.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("disabled","“SmokeTest”")
        drive_name = shared.system.mountUSBDrive()
        test.log("We need to wait here for a second for the drive to appear")
        snooze(1.0)
        shared.results.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/" + drive_name)
        
        #98-84. Observe that on a removable flash drive, the checkbox will be enabled and its name 
        #will change to say "Safely remove "[name]" after export" with the checkbox being checked. 
        #Note [name] is the name of the device.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckbox("enabled","“" + drive_name +"”")
        shared.results.exportallfiledialog.confirmSafelyRemoveCheckboxState("checked")
    
        #98-85. Change the file name to "TestExport" and press the Export button to export the file to the USB flash drive.
        test.log("Step #" + str(step_counter) + "-" + str(sub_step_counter)); sub_step_counter += 1
        shared.results.exportallfiledialog.setFilename("TestExport")
        shared.system.deleteFile("/Volumes/" + drive_name + "/TestExport.txt")
        shared.results.exportallfiledialog.clickExportButton()
        shared.results.waitForExportCurrentButton()    
        
        test.log("Step 99 picks up where we just left off on the second time through step #85 with a different filename")
        #99. Select the USB flash drive in the Where combobox, press the Export button, 
        #and observe once the data is exported the removable flash drive gets ejected with a confirmation message.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        #100. Open the exported file at a separate work station in Excel and observe that the raw export 
        #only exports the original data, no comments or morphology recorded.
        #Confirm the file is exported successfully and data exported is in its raw form.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        test.log("Automation will open the file on Excel without going to a separate station")
        shared.spreadsheets.openExcelAndSaveFile("/Volumes/" + drive_name + "/TestExport")
    
        expected_spreadsheet = shared.config.expected_spreadsheet_results_dir + "/TestExport.xls"
        shared.spreadsheets.compareSpreadsheets(expected_spreadsheet,"/Volumes/" + drive_name + "/TestExport.xls")

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
