# -*- coding: utf-8 -*-
import decimal
import test
import testData
import object
import objectMap
import squishinfo
import squish
import subprocess

from tables import Tables
from printdialog import PrintDialog
from exportallfiledialog import ExportAllFileDialog
from createfolderdialog import CreateFolderDialog
from archivesampledialog import ArchiveSampleDialog
from resultsoverview import ResultsOverview
from config import Config

class Results(Tables):
    
    def __init__(self):
        version = Config().version
        self.accession_number = 0
        self.printdialog = PrintDialog()
        self.exportallfiledialog = ExportAllFileDialog()
        self.createfolderdialog = CreateFolderDialog()
        self.archivesampledialog = ArchiveSampleDialog()
        self.overview = ResultsOverview()
        self.export_file = ""
        self.exported_file = ""
        self.start_index = 0
        
        self.object_symbol =                        ":Bloodhound™ Viewing Station " + version + ".Results_TabProxy"
        self.jpanel2_object_symbol =                ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.review_symbol =                        ":Bloodhound™ Viewing Station " + version + ".Acknowledge_JButton"
        self.review_button_symbol =                 ":Results.Open for Review_JButton"
        self.show_all_table_symbol =                ":Show All.0_0_TableItemProxy"
        self.save_button_symbol =                   ":Results.Save_JButton"
        self.print_button_symbol =                  ":Results.Print_JButton"
        self.export_current_button_symbol =         ":Results.Export Current_JButton"
        self.close_button_symbol =                  ":Results.Close_JButton"
        self.raw_export_button_symbol =             ":Results.Export Raw_JButton"
        self.show_all_JTable_symbol =               ":Results.Show All_JTable"
        self.archive_button_symbol =                ":Results.Archive_JButton"
        self.release_button_symbol =                ":Results.Release_JButton"
        self.release_button2_symbol =               ":Results.Release_JButton_2"
        self.cancel_release_button =                ":Results.Cancel Release_JButton"
        self.archive_sample_dialog_button_symbol =  ":Bloodhound™ Viewing Station " + version + ".Archive_JButton"
        self.unreleased_test_button_symbol =        ":Bloodhound™ Viewing Station " + version + ".Archive_JButton"
        self.view_results_button_symbol =           ":Results.View Results_JButton"
        self.mark_for_rerun_button_symbol =         ":Results.Mark for Rerun_JButton"
        self.sidebar_sample_run_combobox_symbol =   ":Results_JComboBox"
        self.initial_review_checkbox_symbol =       ":Results.Initial Review_JCheckBox"
        self.level1_review_checkbox_symbol =        ":Results.Level 1 Review_JCheckBox"
        self.level2_review_checkbox_symbol =        ":Results.Level 2 Review_JCheckBox"
        self.level3_review_checkbox_symbol =        ":Results.Level 3 Review_JCheckBox"
        self.review_combobox_symbol =               ":Results_JComboBox_2"
        self.undo_button_symbol =                   ":Results.↩_JButton"
        self.redo_button_symbol =                   ":Results.↪_JButton"
        self.initial_review_combobox_symbol =       ":Results_JComboBox_2"
        self.autodiff_combobox_symbol =             ":Results_JComboBox_3"
        self.revert_button_symbol =                 ":Results.Revert_JButton"
        self.sidebar_table1_symbol =                ":Results_JTable"
        self.sidebar_table2_symbol =                ":Results_JTable_2"
        self.action_button_symbol =                 ":Results.Action_JButton"
        self.override_lock_button_symbol =          ":Results.Override Lock_JButton"
        self.results_tab_symbol =                   ":Bloodhound™ Viewing Station " + version + ".Results_TabProxy_2"
        self.maintenance_tab_symbol =               ":Bloodhound™ Viewing Station " + version + ".Maintenance_TabProxy"
        self.save_as_table_symbol =                 ":Bloodhound™ Viewing Station " + version + ".Save As:_JTable"
        self.export_raw_cancel_button_symbol =      ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.save_as_jlabel_symbol =                ":Bloodhound™ Viewing Station " + version + ".Save As:_JLabel"
        self.save_as_text_field_symbol =            ":Bloodhound™ Viewing Station " + version + ".Save As:_JTextField"
        self.where_combobox_symbol =                ":Bloodhound™ Viewing Station " + version + ".Where:_JComboBox"
        self.export_button_symbol =                 ":Bloodhound™ Viewing Station " + version + ".Export_JButton"
        self.export_dialog_title =                  ":Bloodhound™ Viewing Station " + version + "_FileDialog"
        self.create_folder_dialog_title =           ":Bloodhound™ Viewing Station " + version + ".Name:_JLabel"
        self.sidebar_jpanel_symbol =                ":Bloodhound™ Viewing Station " + version + "_JPanel" 
        self.device_ejected_label_symbol =          ":Bloodhound™ Viewing Station " + version + ".The device may now be safely removed._JLabel"
        self.device_ejected_ok_button_symbol =      ":Bloodhound™ Viewing Station " + version + ".OK_JButton"
        self.dilution_numbers = {}                
        
    def clickTab(self):
        squish.clickTab(self.object_symbol)
        
    def clickDeviceEjectedOkButton(self):
        squish.clickButton(self.device_ejected_ok_button_symbol)
        
    def confirmDeviceEjectedLabel(self):
        label = waitForObject(self.device_ejected_label_symbol)
        test.verify(label.text == "The device may now be safely removed.","Confirm that 'The device may now be safely removed.' label exists")
        
    def getAccessionNumber(self):
        return self.accession_number
       
    def clickOnFirstRowOfTable(self):
        squish.mouseClick(self.show_all_table_symbol)
       
    def clickOpenForReviewButton(self):
       squish.clickButton(self.review_button_symbol)
                
    def clickSaveButton(self):
        squish.clickButton(self.save_button_symbol)
        
    def clickReviewPageCloseButton(self):
        squish.clickButton(self.close_button_symbol)
        
    def getSelectedStatus(self):
        return self.table.getValueAt(self.table.getSelectedRow(),0)
    
    def clickActionButton(self):
        squish.clickButton(waitForObject(self.action_button_symbol))
        
    def clickCloseButton(self):
        squish.clickButton(self.close_button_symbol)
        
    def clickReleaseButton(self):
        squish.clickButton(self.release_button_symbol)
        
    def clickReleaseButton2(self):
        squish.clickButton(self.release_button2_symbol)
        
    def clickReviewReleaseButton(self):
        squish.clickButton(self.release_button2_symbol)
        
    def getDilutionRatioFromSideBar(self,sidebar_text):
        dilution = ""
        for text in sidebar_text:
            #First test if 'text' has a get method
            #Then test if 'text' has 2 elements
            #Then see if Dilution is part of that second element string
            if hasattr(text, 'get') and text.size() > 1 and"Dilution" in text.get(1).toString():
                dilution = text.get(1).toString()
                break
            
        return dilution
        
    def setAccessionNumber(self):
        #The Results tab object changes based on what is being viewed under it
        #So Account for that We might want to refactor this code to use two different result objects.
        #Let's see how it goes.
        if object.exists(self.results_tab_symbol):
            highlevel_tab = object.children(findObject(self.results_tab_symbol))
        elif object.exists(self.maintenance_tab_symbol):
            highlevel_tab = object.children(findObject(self.maintenance_tab_symbol))
        for maintab in highlevel_tab:
            maintab_children = object.children(maintab)
            counter = 0;
            for child in maintab_children:
                #Just for debugging
                #test.log(child.text)
                #If we find the Accession # label it should be two down from there.
                if str(child.text).strip() == "Accession #:":
                    self.accession_number =  str(maintab_children[counter + 2].text)
                    test.log("Note the Accession Number: " + self.accession_number)
                    break
                    test.fail("Could not find an Accession Number")
                    
                counter += 1
                
    def confirmTheWhiteCheckmarkIsNoLongerDisplayed(self):
        #Get the Images Object
        images = Images()
        #Update the Table
        self.populateTableData()
        #Get the selected Row - This should be the row with the Awaiting Review Icon
        row = object.children(object.children(self.table)[self.table.getSelectedRow()])[0]
        #Save off the Awaiting Review Icon
        image_filename1 = images.saveImage("status_icon.png", row)
        #And Compare it to the Expected Awaiting Review Icon
        image_filename2 = Config().images_dir + "/expected_status_icon.png"
        images.compareImages(image_filename1,image_filename2, "true")
        
    def confirmStatusIcon(self,image_type,status):
        #Get the Images Object
        images = Images()
        #Update the Table
        self.populateTableData()
        Tables.clickOnTableRowByName(self,self.show_all_JTable_symbol,'Status', status)
        #Get the Row with the correct status 
        row = object.children(object.children(self.table)[self.table.getSelectedRow()])[0]
        #Save off the Awaiting Review Icon
        images.saveImage(image_type, row)
        #And Compare it to the Expected Awaiting Review Icon
        filename1 = Config().images_dir + "/" + image_type
        filename2 = Config().images_dir + "/expected_" + image_type
        images.compareImages(filename1, filename2, "true")
        
    def populateTableData(self):
        self.clickTab()
        return Tables.populateTableData(self, self.show_all_JTable_symbol)
        
    def populateExportAllRunsTableData(self):
        Tables.populateTableData(self, self.save_as_table_symbol)
        
    def populateTableDataWithAllRowsEqualToReadyforRelease(self):
        Tables.populateTableDataWithAllRowsEqualToReadyforRelease(self, self.show_all_JTable_symbol)
        
    def doubleClickReleasedSampleRow(self):
        self.populateTableData()
        Tables.doubleClickOnTableRow(self, 0)
        
    def doubleClickOnTableRow(self, row):
        Tables.doubleClickOnTableRow(self, row)
        
    def confirmResultsReleaseDialogAppearsOnlyForAShortTime(self,accession_number):
        release_dialog = waitForObject(self.results_tab_symbol)
        self.getAccessionNumber()
        test.verify(self.getAccessionNumber() == accession_number,"Confirm the Accession number on this Dialog")
        counter = 0
        dialog_removed = True
        while (object.exists(self.results_tab_symbol)):
            snooze(1.0)
            counter += 1
            #Break after 5 minutes
            if counter == 300:
                dialog_removed = False
                break
            
        test.verify(dialog_removed,"Confirm that the ResultsDialog Has been Removed")

    def getSideBarText(self):
        sidebartext = Tables.getSideBarText(self,":Results_WrappingDetailsList")
        return sidebartext
    
    def getSideBarTextByIndex(self,index,status):
        text = Tables.getSideBarTextByIndex(self,index,status)
        return text
    
    def confirmSideBarText(self,index, accession_number):
        self.populateTableData()
        Tables.confirmSideBarText(self,index,accession_number)
        
    def confirmSideBarAccessionNumber(self, accession_number):
        sidebar_text = self.getSideBarText()
        test.log("Here is sidebar_text: " + str(sidebar_text))
        test.log("Here is sidebar_text[0]: " + str(sidebar_text[0]))
        test.verify(accession_number == str(sidebar_text[0]), "Confirm that the table accession number: " 
                    + accession_number + " is equal to the sidebar accession number: " + str(sidebar_text[0])) 
        
    def getSideBarTableData(self):
        Tables.populateTableData(self,self.sidebar_table1_symbol)
        sidebar_table = Tables.getTableData(self)
        sidebar_data= {}
        for row in sidebar_table:
            sidebar_data[row['Parameter']] = row['Result']
        return sidebar_data
    
    def getSideBarCellTypeTableData(self):
        sidebar_table = Tables.populateTableData(self,self.sidebar_table2_symbol)
        return sidebar_table
    
    def confirmCellTypeTableData(self,cell_type):
        found_cell_type = False
        data_table = self.getSideBarCellTypeTableData()
        for row in data_table:
            if row['Cell Type'] == cell_type:
                found_cell_type = True
                break
        test.verify(found_cell_type,"Confirm that " + cell_type + " is found in the Sidebar Cell Type Table")
        test.verify('%' in row,"Confirm that a percent column exist in this row also")
        test.verify('10/L' in row, "Confirm that absolute count column exists in this row also")          
    
    def confirmSTATSamples(self,spritecanvas,row_count):
        #Select the Results Tab
        self.clickTab()
        #Get The Table Data
        self.populateTableData()
        #Total number of rows you would like to confirm.
        item = row_count - 1
        for row in self.table_data:
            test.verify(row["Accession #"] == spritecanvas.accession_numbers[item],"Confirm Accession # in Results List, " 
                        + row["Accession #"] + " to Analyzer Simulator Accession # " + spritecanvas.accession_numbers[item])
            test.verify(row["Mode"] == "STAT", "Confirm that the mode for every row is STAT")
            if item == 0:
                break
            
            item -= 1
    
    def confirmReviewPage(self,status="displayed"):
        if status == "displayed":
            test.verify(object.exists(":Results.Overview_TabProxy"),"Confirm that the Results Overview Page is being displayed.")
            self.clickReviewPageCloseButton()
        else:
            test.verify(not object.exists(":Results.Overview_TabProxy"),"Confirm that the Results Overview Page is being displayed.")
        
    def clickOnTableRow(self,status):
        self.populateTableData()
        row = Tables.clickOnTableRow(self,status)
        return row
    
    def setAccessionNumberByRow(self,row):
        self.populateTableData()
        self.accession_number = Tables.getTableData(self)[row]["Accession #"]
        return self.accession_number
        
    def clickOnRowByMedicalRecord(self,medical_record):
        Tables.clickOnRowByMedicalRecord(self,medical_record)
        
    def clickOnRowByAccessionNumber(self,accession_number):
        Tables.clickOnTableRowByName(self,self.show_all_JTable_symbol,"Accession #", accession_number)
        
    def confirmAccessionNumberAppearsInTable(self,accession_number):
        passed = False
        table_data = self.populateTableData()
        for row in table_data:
            if row['Accession #']  == accession_number:
                passed = True
                
        test.verify(passed,"Confirm that the accession_number " + accession_number + " was found in the Result Table")
        
    def doubleClickOnRowByAccessionNumber(self,accession_number):
        Tables.doubleClickOnTableRowByName(self,self.show_all_JTable_symbol, "Accession #", accession_number)
        
    def clickExportRawButton(self):
        clickButton(findObject(self.raw_export_button_symbol))
        
    def clickExportRawCancelButton(self):
        clickButton(findObject(self.export_raw_cancel_button_symbol))
        
    def confirmReleaseButton(self, status):
        self.confirmButton(self.release_button_symbol,status,"Release")
            
    def confirmCancelReleaseButton(self, status):
        self.confirmButton(self.cancel_release_button,status,"Cancel Release")
        
    def clickCancelReleaseButton(self):
        squish.clickButton(self.cancel_release_button)
            
    def confirmPrintButton(self,status):
        self.confirmButton(self.print_button_symbol,status,"Print")

    def confirmArchiveButton(self,status):
        self.confirmButton(self.archive_button_symbol,status,"Archive")
        
    def clickArchiveButton(self):
        squish.clickButton(findObject(self.archive_button_symbol))
        
    def archiveRecords(self,user,total):
        self.populateTableData()
        for index in range(total):
            Tables.clickOnTableRowIndex(self,0)
            self.clickArchiveButton()
            user.enterUsernamePassword()
            self.clickArchiveSampleDialogButton()
            self.clickUnreleasedTestsButton()
            self.clickTab()
            
    def clickArchiveSampleDialogButton(self):
        squish.clickButton(self.archive_sample_dialog_button_symbol)
        
    def clickUnreleasedTestsButton(self):
        squish.clickButton(self.unreleased_test_button_symbol)

    def confirmExportCurrentButton(self,status):
        self.confirmButton(self.export_current_button_symbol,status,"Export Current")
        
    def waitForExportCurrentButton(self):
        waitForObject(self.export_current_button_symbol)
        
    def clickExportCurrentButton(self):
        squish.clickButton(self.export_current_button_symbol)
        
    def confirmExportRawButton(self,status):
        self.confirmButton(self.raw_export_button_symbol,status,"Export Raw")
        
    def confirmOverrideLockButton(self,status):
        self.confirmButton(self.override_lock_button_symbol, status, "Override Lock")
            
    def confirmMarkForRerunButton(self,status):
        self.confirmButton(self.mark_for_rerun_button_symbol,status,"Mark for Rerun")
        
    def clickMarkForRerunButton(self):
        squish.clickButton(self.mark_for_rerun_button_symbol)
        
    def confirmOpenForReviewButton(self,status):
        self.confirmButton(self.review_button_symbol,status,"Open for Review")
        
    def confirmViewResultsButton(self,status):
        self.confirmButton(self.view_results_button_symbol, status, "View Results")
        
    def clickViewResultsButton(self):
        squish.clickButton(self.view_results_button_symbol)
    
    def confirmSaveButton(self,status):
        self.confirmButton(self.save_button_symbol, status,"Save")
        
    def confirmRevertButton(self,status):
        self.confirmButton(self.revert_button_symbol,status,"Revert")
    
    def confirmUndoButton(self,status):
        self.confirmButton(self.undo_button_symbol,status,"Undo")
        
    def confirmRedoButton(self,status):
        self.confirmButton(self.redo_button_symbol,status,"Redo")
        
    def confirmInitialReviewButton(self,status):
        self.confirmButton(self.initial_review_combobox_symbol,status,"Initial Review")

    def confirmAutoDiffButton(self,status):
        self.confirmButton(self.autodiff_combobox_symbol,status,"AutoDiff")
        
    def confirmReleaseButton(self,status):
        self.confirmButton(self.release_button_symbol,status,"Release")
        
    def confirmButton(self,object_symbol,status,button_name):
        if status == "enabled":
            test.verify(findObject(object_symbol).enabled == True,"Confirm that the " + button_name + " Button is enabled")
        elif status == "disabled":
            test.verify(findObject(object_symbol).enabled == False,"Confirm that the " + button_name + " Button is disabled")        
            
    def clickPrintButton(self):
        squish.clickButton(self.print_button_symbol)        
            
    def confirmExportCurrentButton(self,status):
        if status == "enabled":
            test.verify(findObject(self.export_current_button_symbol).enabled == True, "Confirm that the Export Current Button is enabled")
        elif status == "disabled":
            test.verify(findObject(self.export_current_button_symbol).enabled == False, "Confirm that the Export Current Button is disabled")
            
    #-""Save As"" text field with “export.txt”
    def confirmSaveAs(self):
        test.verify(findObject(self.save_as_jlabel_symbol).enabled == True)
        test.verify(findObject(self.save_as_text_field_symbol).enabled == True)
        test.verify(findObject(self.save_as_text_field_symbol).text == "export.txt")

    #- Folder selector combobox labeled “Where”
    def confirmComboboxWhere(self):
        test.verify(findObject(self.where_combobox_symbol).enabled == True)

    #-Name and Date columns in the File View table
    def confirmNameAndDateColumns(self):
        self.populateExportAllRunsTableData()
        test.verify(str('     Name' in self.table_data[0]) == 'True',"Confirm the Name column in the Export All Table")
        test.verify(str('Date' in self.table_data[0]) == 'True', "Confirm the Date column in the Export All Table")

    #-""Cancel"" and ""Export"" buttons"
    def confirmCancelButton(self):
        test.verify(findObject(self.export_raw_cancel_button_symbol).enabled == True)
        
    def confirmExportButton(self):
        test.verify(findObject(self.export_button_symbol).enabled == True)
        
    def confirmStatusByAccessionNumber(self,status,accession_number):
        row = Tables.getTableRowByName(self,self.show_all_JTable_symbol,'Accession #', accession_number)
        test.verify(row['Status'] == 'Awaiting Review',"Confirm that the status for Accession # " + accession_number + " is Awaiting Review")
        snooze(1.0)

    def exportRaw(self,export_method,filename):
        #There are currently two ways to export raw.
        #1. By medical_record
        #2. Export hightlighted records
        #3. If it's not highlighted_rows assume that it's a medical record
        if (export_method != "highlighted_rows"):
            self.populateTableData()
            self.start_index = Tables.clickOnRowByMedicalRecord(self,export_method)
        
        self.clickExportRawButton()
        #Get the text field so we can set it a little later
        textfield = findObject(self.save_as_text_field_symbol)
        #filename = textfield.getText()
        
        
        #First delete the file if it already exists
        self.export_file = Config().results_dir + "/" + filename
        self.exported_file = Config().testdata_dir + "/" + filename + ".xls"
        tempfile = Config().reproducibility_dir + "/tempfile"

        if os.path.exists(self.export_file + ".txt"):
            os.remove(self.export_file + ".txt")
    
        #Now set the edit box to the full pathname to the file
        textfield.setText(self.export_file)
        self.exportallfiledialog.selectFolderSelectorComboBoxItem("/Volumes/SmokeTest")
        squish.clickButton(findObject(self.export_button_symbol))
    
        return self.export_file

    def run_this_scpt(self,scpt, args=[]):
        p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate(scpt)
        return stdout

    def openExcelAndSaveFile(self):
        self.run_this_scpt(
            "tell application \"Microsoft Excel\"\r\
                open \"" + self.export_file + ".txt\"\r \
                set wb to active workbook \r\
                set fn to (POSIX file \"" + self.exported_file + "\") as string\r\
                save workbook as wb filename fn file format Excel7 file format overwrite yes\r\
                quit\r\
            end tell"
    )
        
    def confirmExport(self,filename):
        spreadsheets = SpreadSheets()
        spreadsheets.compareSpreadsheets(Config().results_dir + "/expected/spreadsheets/" + filename + ".xls", 
            Config().testdata_dir + "/" + filename + ".xls")
        
        #spreadsheets.compareSpreadSheetToTableData(self.table_data,
        #Config().testdata_dir + "/" + filename + ".xls", self.start_index)
        
    def selectTableRows(self,start_index,end_index):
        Tables.selectTableRows(self,start_index, end_index,self.show_all_JTable_symbol)
        
    def hightlightAllRowsWithMultipleRuns(self):
        self.clickTab()
        self.populateTableData()
        self.start_index = 0
        end_index = 0
        starting_contiguous_rows = False
        for index in range (len(self.table_data)):
            Tables.clickOnTableRowIndex(self,index)
            number_of_analyzers = findObject(":Results_JComboBox").getItemCount()
            #Check to see if the row has more than one analyzer
            if number_of_analyzers > 1:
                starting_contiguous_rows = True
                #Set the start index
                if self.start_index == 0:
                    self.start_index = index
                #else increment the end_index
                else:
                    end_index = index
            
            else:
                starting_contiguous_rows = False
        
            if self.start_index > 0 and not starting_contiguous_rows:
                break
            
        #Now Highlight all contiguous rows that have more than one analyzer
        Tables.selectTableRows(self,self.start_index,end_index)
        
    def setSearchText(self,text):
        squish.findObject(":Results.Search:_PlaceholderOverlay").parent.setText(text)
        
    def clickShowAllButton(self):
        squish.clickButton(":Results.Show All_JButton")
        
    def getFileExportDialogTitle(self):
        dialog_string = squish.findObject(self.export_dialog_title).parent.toString()
        #Don't ask how this works
        #But if you need to know - 
        #just break up the individual calls
        title = dialog_string.rsplit(",")[0][dialog_string.rsplit(",")[0].find("-")+1:len(dialog_string.rsplit(",")[0])]
        return title
    
    def getCreateFolderDialogTitle(self):
        dialog_string = findObject(self.create_folder_dialog_title).parent.toString()
        #Don't ask how this works
        #But if you need to know - 
        #just break up the individual calls
        title = dialog_string.rsplit(",")[0][dialog_string.rsplit(",")[0].find("-")+1:len(dialog_string.rsplit(",")[0])]
        return title
    
    def getTotalRunsFromSideBar(self):
        combo_box = waitForObject(self.sidebar_sample_run_combobox_symbol)
        return combo_box.getItemCount()
    
    def selectSidebarSampleRunByIndex(self,index,original_size):
        #Go Back to the Viewing Station
        waitForObject(self.sidebar_jpanel_symbol).getTopLevelAncestor().toFront()
        #Click on the Results Tab
        self.clickTab()
        #Need to make sure that the size of the combobox has increased by 1
        combo_box = waitForObject(self.sidebar_sample_run_combobox_symbol)
        counter = 0
        #Wait 10 seconds for this to happen
        timeout = False
        while (True):
            snooze(1.0)
            if combo_box.getItemCount() > original_size:
                break
            counter += 1
            if counter > 10:
                timeout = True
                break
        if not timeout:
            combo_box.setSelectedIndex(index)
        
    def confirmDilutionFactorChange(self,first_run_data,second_run_data,ratio):
        data1 = decimal.Decimal(first_run_data)
        data2 = decimal.Decimal(second_run_data)
        result = False
        product = data1 * ratio 
        d = decimal.Decimal(first_run_data)
        #Find out the tolerance in decimals ie: .1 .01 .001 etc
        tolerance = decimal.Decimal(10 ** d.as_tuple().exponent)
        if (product - tolerance) <= data2 and (product + tolerance) >= data2:
            result = True
        
        return result

    def initialReviewCheckBox(self,status):
        self.clickCheckBox(self.initial_review_checkbox_symbol,status)
        
    def level1ReviewCheckBox(self,status):
        self.clickCheckBox(self.level1_review_checkbox_symbol,status)
        
    def level2ReviewCheckBox(self,status):
        self.clickCheckBox(self.level2_review_checkbox_symbol,status)
        
    def level3ReviewCheckBox(self,status):
        self.clickCheckBox(self.level3_review_checkbox_symbol,status)
        
    def clickCheckBox(self,object_symbol,status):
        check_box = findObject(object_symbol)
        if status == "check" and not check_box.selected == True:
            squish.mouseClick(object_symbol, 26, 23, 0, squish.Button.Button1)
        elif check_box.selected == True:
            squish.mouseClick(squish.waitForObject(object_symbol), 26, 23, 0, squish.Button.Button1)
            
    def selectReviewComboBox(self,item):
        combo_box = findObject(self.review_combobox_symbol)
        
        for index in range(combo_box.getItemCount()):
            if str(combo_box.getItemAt(index)) == item:
                combo_box.setSelectedIndex(index)
                break
                
    def clickOnTableRowByName(self,field_name, cell_value):
        Tables.clickOnTableRowByName(self,self.show_all_JTable_symbol,field_name,cell_value)
        
    def setDilutionNumbers(self):
        self.clickOpenForReviewButton()
        self.populateOverviewTable()
        
    def confirmDilutionFactor(self,original_dilution_numbers,new_dilution_numbers,parameters,factor):
        for parameter in parameters:
            passed = self.confirmDilutionFactorChange(original_dilution_numbers[parameter], new_dilution_numbers[parameter],factor)
            test.verify(passed,"Confirm that the dilution factor of " + str(factor) + " for this parameter " + parameter + " multiplied the original result " + str(original_dilution_numbers[parameter]) + " to equal " + str(new_dilution_numbers[parameter]))
    
    def waitForNoPatientDataRows(self,total):
        passed = False
        counter = 0
        while (True):
            row_count = 0
            table_data = self.populateTableData()
            for row in table_data:
                if row["Name"] == "(No patient data)":
                    row_count += 1
            
            if row_count == total:
                passed = True
                break
            
            if counter == 30:
                break
            
            snooze(1.0)
            counter += 1


