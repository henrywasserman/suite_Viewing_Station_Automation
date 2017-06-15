# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string
import time
import __builtin__

from tables import Tables

class Archives(Tables):
    
    def __init__(self):
        version = Config().version
        self.object_symbol =                 ":Bloodhound™ Viewing Station " + version + ".Archives_TabProxy"
        self.search_text_symbol =            ":Archives.Search_JTextField"
        self.view_results_button_symbol =    ":Archives.View Results_JButton"
        self.search_button_symbol =          ":Archives.Search Archives_JButton"
        self.search_start_month_symbol =     ":Archives.Start:_JTextField"
        self.search_start_day_symbol =       ":Archives./_JTextField"
        self.search_start_year_symbol =      ":Archives./_JTextField_2"
        self.search_end_month_symbol =       ":Archives.End:_JTextField"
        self.search_end_day_symbol =         ":Archives./_JTextField_3"
        self.search_end_year_symbol =        ":Archives./_JTextField_4"
        self.search_table_symbol =           ":Archives.Search Archives_JTable"
        self.primary_search_table_symbol =   ":Archives_JTable"
        self.close_button_symbol =           ":Archives.Close_JButton"
        self.export_button_symbol =          ":Archives.Export_JButton"
        self.print_button_symbol =           ":Archives.Print_JButton"
        self.export_current_button_symbol =  ":Archives.Export Current_JButton" 
        self.export_raw_button_symbol =      ":Archives.Export Raw_JButton"
        self.dialog_username_symbol =        ":Bloodhound™ Viewing Station " + version + ".Username:_JTextField"
        self.dialog_password_symbol =        ":Bloodhound™ Viewing Station " + version + ".Password:_JPasswordField"
        self.dialog_archive_button_symbol =  ":Bloodhound™ Viewing Station " + version + ".Archive_JButton"
        self.number_of_samples_symbol =      ":Archives.4 samples_JLabel"
        self.file_dialog_symbol =            ":Bloodhound™ Viewing Station " + version + "_FileDialog"
        
    def clickTab(self):
        clickTab(findObject(self.object_symbol))
    
    def setSearchText(self, text):
        findObject(self.search_text_symbol).document.contents = text
        
    def clickViewResultsButton(self):
        clickButton(findObject(self.view_results_button_symbol))
        
    def clickSearchArchivesButton(self):
        self.clickTab()
        clickButton(waitForObject(self.search_button_symbol))
        
    def clickOnArchiveRow(self):
        Tables.clickOnTableRow(self,"Released")
        
    def getTableRowByName(self,field_name, cell_value):
        return Tables.getTableRowByName(self,self.primary_search_table_symbol,field_name,cell_value)
        
        
    def populateTableData(self):
        return Tables.populateTableData(self, self.primary_search_table_symbol)
        
    def confirmArchiveRecordsDisplayed(self):
        counter = 0
        we_have_at_least_one_record = False
        while(True):
            snooze(1.0)
            self.clickSearchArchivesButton()
            self.populateTableData()
            if len(Tables.getTableData(self)) > 0:
                we_have_at_least_one_record = True
                break
            counter += 1
            if counter == 10:
                break
        
        if (we_have_at_least_one_record):
            test.verify(we_have_at_least_one_record == True,"Confirm that at least one record exists in the Archive Table")
        else:
            test.verify(we_have_at_least_one_record == True,"Possible Mantis Bug 0013439")
        
    def clickOnTableRow(self,status):
        Tables.clickOnTableRow(self,status)
        
    def clickCloseButton(self):
        clickButton(self.close_button_symbol)

    def confirmExportButton(self,status):
        self.confirmButton(status,self.export_button_symbol,"Export Button")
        
    def clickExportButton(self):
        clickButton(self.export_button_symbol)
        
    def getFileExportDialogTitle(self):
        dialog_string = findObject(self.file_dialog_symbol).parent.toString()
        #Don't ask how this works
        #But if you need to know - 
        #just break up the individual calls
        title = dialog_string.rsplit(",")[0][dialog_string.rsplit(",")[0].find("-")+1:len(dialog_string.rsplit(",")[0])]
        return title
            
    def confirmPrintButton(self,status):
        self.confirmButton(status,self.print_button_symbol,"Print Button")
    
    def clickPrintButton(self):
        squish.clickButton(self.print_button_symbol)
        
    def confirmExportCurrentButton(self,status):
        self.confirmButton(status,self.export_current_button_symbol,"Export Current Button")
        
    def confirmExportRawButton(self,status):
        self.confirmButton(status,self.export_raw_button_symbol, "Export Raw Button")
        
    def confirmViewResultsButton(self,status):
        self.confirmButton(status,self.view_results_button_symbol,"View Results Button")
            
    def confirmButton(self,status,object_symbol,button_name):        
        if status =="enabled":
            test.verify(findObject(object_symbol).enabled == True, "Confirm that the " + button_name + " is enabled")
        else:
            test.verify(findObject(object_symbol).enabled == False, "Confirm that the " + button_name + " is disabled")
            
    def selectTableRows(self,start,end):
        Tables.selectTableRows(self,start,end,self.search_table_symbol)
        
    def authenticateArchiveSamplesDialog(self, user):
        username_editbox = findObject(self.dialog_username_symbol)
        password_editbox = findObject(self.dialog_password_symbol)
        
        username_editbox.text = user.username
        password_editbox.setContent(user.password)
        squish.clickButton(self.dialog_archive_button_symbol)
        #This second click is for the Unreleased Tests 'MessageBox'
        #3 of these samples have unreleased tests. Are you sure you wantto archive them?
        squish.clickButton(self.dialog_archive_button_symbol)
        
    def setSearchArchivesDatesToCurrentDate(self):
        
        month = time.strftime("%m")
        day = time.strftime("%d")
        year = time.strftime("%Y")
        
        findObject(self.search_start_month_symbol).text = month  
        findObject(self.search_start_day_symbol).text = day
        findObject(self.search_start_year_symbol).text = year
        findObject(self.search_end_month_symbol).text = month
        findObject(self.search_end_day_symbol).text = day
        findObject(self.search_end_year_symbol).text = year
        
    def confirmNumberOfSamplesText(self,samples_text):
        number_of_samples_text = findObject(self.number_of_samples_symbol).text
        test.verify(samples_text == number_of_samples_text,"Confirm that the number of samples text is displayed as: " + samples_text)
    
    def selectAllRowsWithCommand_a(self):
        squish.mouseClick(squish.findObject(self.search_table_symbol), 40, 15, 0, squish.Button.Button1) 
        squish.type(findObject(self.search_table_symbol),"<Command+a>")

    def clickOnRowByAccessionNumber(self,accession_number):
        Tables.clickOnTableRowByName(self,self.primary_search_table_symbol,"Accession #", accession_number)
