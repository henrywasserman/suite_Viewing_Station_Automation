# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish
import string
import __builtin__

from tables import Tables
from createworkorderdialog import CreateWorkOrderDialog
from deletesampledialog import DeleteSampleDialog
from patientinformationdialog import PatientInformationDialog
from analyzereventsdialog import AnalyzerEventsDialog
from config import Config

class InProcess(Tables):
    
    def __init__(self):
        version = Config().version
        #get_expected_row_count is reserved exclusively for the getExpectedRowCount method
        Tables.__init__(self)
        self.analyzer_object_symbol = ":Bloodhound™ Viewing Station " + version + "_JTabbedPane"
        self.get_expected_row_count = 0
        self.side_bar_sample_pattern = re.compile('.*Open-mode sample taken by Bloodhound\\s\\d at \\d+\:\\d+.*')
        self.table_symbol = ":In Process.Show All_JTable"
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + ".In Process_TabProxy"
        self.first_row_symbol = ":Show All.0_0_TableItemProxy_2"
        self.delete_sample_button_symbol = ":In Process.Delete Sample_JButton"
        self.analyzer_combo_box_symbol = ":In Process.Filter by Analyzer_JComboBox"
        self.create_work_order_button_symbol = ":In Process.Create Work Order_JButton"
        self.edit_patient_button = ":In Process.Edit Patient_JButton"
        self.search_edit_box_symbol = ":In Process.Search:_SearchTextField"
        self.show_all_button_symbol = ":In Process.Show All_JButton"
        self.status_column_header_symbol = ":Status_TableHeaderItemProxy"
        self.name_column_header_symbol = ":Name_TableHeaderItemProxy"
        self.accession_number_column_header_symbol = ":Accession #_TableHeaderItemProxy" 
        self.medicalRecord_column_header_symbol = ":Medical" 
        self.location_column_header_symbol = ":Location_TableHeaderItemProxy" 
        self.date_column_header_symbol = ":Date_TableHeaderItemProxy_2" 
        self.time_column_header_symbol = ":Time_TableHeaderItemProxy"
        self.turn_around_time_header_symbol =  ":Turnaround" 
        self.priority_column_header_symbol = ":Priority_TableHeaderItemProxy" 
        self.analyzer_column_header_symbol = ":Analyzer_TableHeaderItemProxy" 
        self.mode_column_header_symbol = ":Mode_TableHeaderItemProxy"
        self.sidebar_text_symbol = ":In Process_WrappingDetailsList"
        
        self.in_process_tab_symbol = ":In Process_JComponent"
         
        self.createworkorderdialog = CreateWorkOrderDialog()
        self.deletesampledialog = DeleteSampleDialog()
        self.patientinformationdialog = PatientInformationDialog()
        
    def clickTab(self):
        squish.clickTab(squish.findObject(self.object_symbol))

    def getTotalNumberOfSamples(self):
        self.clickTab()
        return squish.findObject(self.table_symbol).getRowCount()
    
    def clickOnFirstRowOfTable(self):
        Tables.clickOnTableCellByIndex(self,self.table_symbol,0,0)

    #This is a special case function that handles looping sample rack runs    
    def waitForRackToFinish(self,starting_sample_number):
        #Wait for a maximum of 300 seconds
        #This does some 'tricky' stuff to handle expected row count while looping.
        #When looping the simulator uses a tube of cleaning solution for every
        #20th sample. 
        squish.waitForObject(self.analyzer_object_symbol).getTopLevelAncestor().toFront()
        self.clickTab()
        table = squish.findObject(self.table_symbol)
        counter = 0
        while table.getRowCount() < self.getExpectedRowCount(starting_sample_number):
            squish.snooze(1.0)
            AnalyzerEventsDialog().dismissAnalyzerEvents()
            counter = counter + 1
            if counter == 300:
                break
        total_samples = self.getTotalNumberOfSamples()
        test.log("Total Samples is now at " + str(total_samples))
        return total_samples
        
    def waitForSampleToFinish(self,starting_sample_number):
        #Wait for a maximum of 300 seconds
        waitForObject(self.analyzer_object_symbol).getTopLevelAncestor().toFront()
        self.clickTab()
        table = squish.findObject(self.table_symbol)
        counter = 0
        while table.getRowCount() < starting_sample_number + 1:
            squish.snooze(1.0)
            AnalyzerEventsDialog().dismissAnalyzerEvents()
            counter = counter + 1
            if counter == 300:
                break
       
        test.log("Total Samples is now at " + str(self.getTotalNumberOfSamples()))
        
    def getExpectedRowCount(self,starting_sample_number):
        if self.get_expected_row_count % 2 == 0:
            expected_count = starting_sample_number + 9
        else:
            expected_count = starting_sample_number + 10
            
        self.get_expected_row_count += 1
        return expected_count

    def getSideBarText(self):
        sidebartext = Tables.getSideBarText(self,self.sidebar_text_symbol)
        return sidebartext
    
    def confirmRackUnderModeColumn(self, starting_sample_number):
        self.clickTab()
        table = Tables.getTableData(self)
        total_samples_of_this_run = len(table) - starting_sample_number
        
        #for index in range (1, total_samples_of_this_run):
        for index in range (len(table)):
            test.verify(table[index]["Mode"],"Confirm the Mode in every row in the table is Rack " + table[index]["Accession #"])
            
    def confirmSamplePatientIdentityInfoExists(self):
        main_tab = findObject(self.in_process_tab_symbol)
        patient_labels = {}
        for index in range(main_tab.getComponentCount()):
            component = main_tab.getComponents().at(index)
            if "JLabel" in component.toString():
                if "Medical Record" in component.text:
                    patient_labels[component.text] = main_tab.getComponents().at(index + 2).text
                elif "Age" in component.toString():
                    patient_labels[component.text] = main_tab.getComponents().at(index + 3).text
                elif "Sex" in component.toString():
                    patient_labels[component.text] = main_tab.getComponents().at(index + 3).text
                elif "Physician" in component.toString():
                    patient_labels[component.text] = main_tab.getComponents().at(index + 3).text
                    
        test.verify(len(patient_labels) == 4, "Confirm that the following labels exist: Medical Record, Age, Sex, Physician")
            
    def confirmARunOnTheSideBar(self):
        #For now just select the first row
        sidebartext = "[]"
        counter = 0
        #Wait Five Seconds to find sidebar text
        while(str(sidebartext) == "[]" or "No sample selected" in str(sidebartext[0])):
            Tables.clickOnTableRowIndex(self,0)
            sidebartext = self.getSideBarText()
            test.log("inside while sidebartext is: " + str(sidebartext))
            squish.snooze(1.0)
            counter += 1
            if counter == 5:
                sidebartext = "Could not find sidebar text"
                break
        
        test.log("Here is sidebartext: " + str(sidebartext))
        test.verify(str(sidebartext[1]).rfind("Ordered tests: CBC, Diff.") != -1, "Confirm that runs are also listed on the sidebar")
        
    def populateTableData(self):
        self.clickTab()
        table_data = Tables.populateTableData(self,self.table_symbol)
        return table_data        
        
    def populateTableDataWithAllRowsEqualToReadyforRelease(self):
        waitForObject(self.analyzer_object_symbol).getTopLevelAncestor().toFront()
        Tables.populateTableDataWithAllRowsEqualToReadyforRelease(self, self.table_symbol)
        
    def getSideBarTextByIndex(self,index,status):
        text = Tables.getSideBarTextByIndex(self,index,status)
        return text

    def confirmSideBarText(self,index,pattern):
        Tables.confirmSideBarText(self,index,pattern)
        
        #Wait For the row count to settledown.
    def waitForSTATRowCount(self,starting_sample_number):
        #Wait for a maximum of 300 seconds
        #The STAT holds 3 samples
        waitForObject(self.analyzer_object_symbol).getTopLevelAncestor().toFront()
        self.clickTab()
        table = squish.findObject(self.table_symbol)
        counter = 0
        while table.getRowCount() < starting_sample_number + 3:
            squish.snooze(1.0)
            AnalyzerEventsDialog().dismissAnalyzerEvents()
            counter = counter + 1
            if counter == 300:
                break
       
        test.log("Total Samples is now at " + str(self.getTotalNumberOfSamples()))
        
    def confirmSTATSamples(self,spritecanvas,row_count):
        #Select the Inprocess Tab
        test.log("Right before self.clickTab()")
        self.clickTab()
        test.log("Right after self.clickTab()")
        #Get The Table Data
        self.populateTableData()
        #Total number of rows you would like to confirm.
        item = row_count - 1
        for row in self.table_data:
            test.verify(row["Accession #"] == spritecanvas.accession_numbers[item],"Confirm Accession # in Process List, " 
                        + row["Accession #"] + " to Analyzer Simulator Accession # " + spritecanvas.accession_numbers[item])
            
            test.verify(row["Mode"] == "STAT", "Confirm that the mode for every row is STAT")
            if item == 0:
                break
            
            item -= 1
            
    def selectEachFilterByAnalizerItem(self):
        analyzer_combo = squish.findObject(self.analyzer_combo_box_symbol)
        for index in range(analyzer_combo.getItemCount()):
            analyzer_combo.setSelectedIndex(index)
            
    def selectFilterByAnalizerName(self,item_name):
        analyzer_combo = squish.findObject(self.analyzer_combo_box_symbol)
        for index in range(analyzer_combo.getItemCount()):
            if str(analyzer_combo.getItemAt(index)) == item_name:
                analyzer_combo.setSelectedIndex(index)
                break
    
    def clickCreateWorkOrderButton(self):
        squish.clickButton(self.create_work_order_button_symbol)
        
    def clickDeleteSampleButton(self):
        squish.clickButton(self.delete_sample_button_symbol)
        
    def confirmDeleteSampleButtonIsDisabled(self):
        button = findObject(self.delete_sample_button_symbol)
        test.verify(button.enabled == False,"Confirm that the Delete Sample Button is disabled")
        
    def confirmDeleteSampleButtonIsEnabled(self):
        button = findObject(self.delete_sample_button_symbol)
        test.verify(button.enabled == True,"Confirm that the Delete Sample Button is enabled")
        
    def clickEditPatientButton(self):
        squish.clickButton(self.edit_patient_button)
    
    def enterSearchText(self,search_text):
        squish.findObject(self.search_edit_box_symbol).text = search_text
        
    def clickShowAllButton(self):
        squish.clickButton(self.show_all_button_symbol)
        
    def clickStatusColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.status_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickNameColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.name_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickAccessionNumberColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.accession_number_column_header_symbol ), 26, 23, 0, squish.Button.Button1)
    
    def clickMedicalRecordColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.medicalRecord_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickLocationColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.location_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickDateColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.date_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickTimeColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.time_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickTurnaroundTimeColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.turn_around_time_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickPriorityColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.priority_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickAnalyzerColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.analyzer_column_header_symbol), 26, 23, 0, squish.Button.Button1)
    
    def clickModeColumnHeader(self):
        squish.mouseClick(squish.waitForObject(self.mode_column_header_symbol), 26, 23, 0, squish.Button.Button1)

    def checkInProcessAccessionNumbers(self,shared):
        for accession_number in shared.spritecanvas.accession_numbers:
            #Seems like we need a little wait here for the table to redraw
            Tables.waitForTableStatusReadyForReleaseOrAwaitingReview(self,self.table_symbol)
            Tables.populateTableData(self,self.table_symbol)
            row = Tables.clickOnTableRowByName(self,self.table_symbol,"Accession #",accession_number)
            name = row["Name"].replace("(","")
            name = name.replace(")","")
            sidebar_text = str(self.getSideBarText()[1])
            expected_sidebar_text = "[" + name + " with the “" + shared.maintenance.newspecialsampledialog.accession_number_types[accession_number] + "” profile, Normal process.]"
            test.verify(expected_sidebar_text == sidebar_text,"Confirm that expected sidebar text " + expected_sidebar_text + " is equal to " + sidebar_text)
            
    def clickOnTableRowByName(self,field_name, cell_value):
        Tables.populateTableData(self,self.table_symbol)
        Tables.clickOnTableRowByName(self,self.table_symbol,field_name, cell_value)
        
    def confirmAccessionNumberExistsInTable(self,accession_number):
        Tables.populateTableData(self,self.table_symbol)
        table_data = Tables.getTableData(self)
        
        for row in range(len(table_data)):
            accession_number_exists = False
            
            if table_data[row]['Accession #'] == accession_number:
                accession_number_exists = True
                 
        return accession_number_exists
        
    def waitForTableStatusReadyForRelease(self):
        Tables._waitForTableStatusReadyForRelease(self,self.table_symbol)
        
    def waitForTableStatus(self,status):
        Tables._waitForTableStatus(self,table_symbol,"Missing Data, Ready For Release")
        
    def waitToClickOnTableRowByName(self,column_name,cell_name):
        return Tables.waitToClickOnTableRowByName(self,self.table_symbol,column_name, cell_name)
                
    def waitForSidebarTextResults(self):
        timer_counter = 0
        counter = 1
        while (counter < 6 ):
            sidebar_text = self.getSideBarText()
        
            for index in range (len(sidebar_text)):
                if "Results " + str(counter) + " of 5" in str(sidebar_text[index]):
                    test.verify(True,"Confirm that Results " + str(counter) + " of 5 will be ready on Bloodhound 1 (Rack mode) was found.")
                    counter += 1
            
            timer_counter += 1
            
            if timer_counter == 1000:
                test.verify(False,"Timer timed out. Could not find Results " + str(counter) + " of 5 will be ready on Bloodhound 1 (Rack mode) in the sidebar")

    def confirmRowIsNotInTable(self,fieldname,key):
        table_data = Tables.populateTableData(self, self.table_symbol)
        
        found_key = False
        
        for index in range(len(table_data)):
            if key in table_data[index]:
                found_key = True
                break;
        
        if not found_key:    
            test.verify(True,"Did not find this key:" + key + " in this column: " + fieldname + " of the inprocess table")
        else:
            test.verify(False,"Found this key:" + key + " in this column: " + fieldname + " of the inprocess table")
