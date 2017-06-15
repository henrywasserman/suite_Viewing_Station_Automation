# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import re
import codecs
import shutil

from controls import Controls
from newreproducibilitytestdialog import NewReproducibilityTestDialog


class ReproducibilityTab(Controls):
    
    def __init__(self):
        self.last_run_pattern = re.compile('.*Last\\s+run\\s+on\\s+\\d+\/\\d+\/\\d+\\s+\\d+\:\\d+\\s+\\w+.*')
        self.fail_warn_pattern = re.compile('.*fail.*')
        
        self.object_symbol = ":QC.Reproducibility_TabProxy"
        self.exclude_button_symbol = ":QC.Exclude_JButton"
        self.export_button_symbol = ":QC.Export_JButton"
        self.cancel_button_symbol =  ":QC.Cancel_JButton"
        self.analyzer_combobox_symbol = ":QC.New control on Bloodhound 1:_JComboBox"
        self.print_button_symbol = ":QC.Print_JButton"
        self.reproducibility_button_symbol = ":QC.Reproducibility_JButton"
        self.right_table_object_symbol = ":Reproducibility.fail*_QCTable_2"
        self.reproducibility_whole_blood_table_symbol = ":Reproducibility.Whole Blood_QCTable_2"
        self.left_table_object_symbol = ":Reproducibility.fail*_QCTable" 
        self.whole_blood_button_symbol = ":QC.Whole Blood_JButton"
        
        self.newreproducibilitytestdialog = NewReproducibilityTestDialog()
    
    def clickTab(self):
        clickTab(waitForObject(self.object_symbol))
        
    def clickWholeBloodButton(self):
        squish.clickButton(self.whole_blood_button_symbol)
        
    def clickReproducibilityButton(self):
        squish.clickButton(self.reproducibility_button_symbol)    

    def confirmQCButtons(self):
        #Confirm the DigiCount, Reproducibility and Whole Blood Buttons are enabled.
        qctab = QCTab()
        qctab.confirmQCButtons()
        
        #Confirm Exclude button functionality
        test.verify(findObject(self.exclude_button_symbol).enabled == False, "Confirm that the Exclude button is disabled")
        test.log("Click on Table Cell row 0, column 0")
        Tables.clickOnTableCellByIndex(self,self.right_table_object_symbol,0,0)
        test.verify(findObject(self.exclude_button_symbol).enabled == True, "Confirm that the Exclude button is Enabled")
        #Confirm Export button is enabled
        test.verify(findObject(self.export_button_symbol).enabled == True, "Confirm that the Export button is enabled")
        #Confirm that the Cancel button is disabled
        test.verify(findObject(self.cancel_button_symbol).enabled == False, "Confirm that the Cancel button is disabled")
        #Confirm that the Control selector combobox is enabled
        test.verify(findObject(self.analyzer_combobox_symbol).enabled == True, "Confirm that the Control selector combobox is enabled")
        #Confirm Control Details text under the Control selector bombobox and the Control Status to the right of the combo box.
        test.verify(self.last_run_pattern.match(findObject(":QC.Last Run on AM_JLabel").text) != None,"Confirm the Control Status to the right of the combobox - Last Run on ##/##/## ##:## AM/PM")
        test.verify(findObject(":QC.Completed_JLabel").text == "Completed", "Confirm the Text under the ComboBox reads 'Completed'")
        if (object.exists(":QC.Fail 5; Warn 34_JLabel")):
            test.verify(self.fail_warn_pattern.match(findObject(":QC.Fail 5; Warn 34_JLabel").text) != None,"Confirm that there is Fail Warn text and it conforms to the expected pattern Fail #;Warn #")
        else:
            test.fail("Check if this label should exist on the QC Reproducibility Panel")
        #Confirm that the Print button is disabled
        test.verify(findObject(self.print_button_symbol).enabled == False, "Confirm that the Print button is currently disabled - grayed out")
        #TODO get inheritted methods working in python
     
    def confirmReproducibilityTable(self):
        list = QCTab().getControlDropdownListItems()
        previous_keys = []
        exported_table = {}
        previouse_exported_table = {}

        for item in range(len(list)):
            findObject(self.analyzer_combobox_symbol).setSelectedIndex(item)
            
            #Create an export file in the data/reproducibility directory
            exportfile = QCTab().exportData("reproducibility")
            exported_table = Tables().createTableDictionary(exportfile)
        
            keys = []
            for key, value in exported_table.items():
                keys.append(key)
        
            keys.sort()

            if (not previous_keys):
                previous_keys = keys
                previous_exported_table = exported_table
                continue
            
            #These Parameters should be the same for each control in the list
            test.compare(previous_keys,keys,"Comparing the Parameter list on the Reproducibility Tab while changing Controls in the List Box")
            previous_keys = keys
            
            #This table data should be different for each control in the list
            test.verify(not (previous_exported_table["WBC"] == exported_table["WBC"]), "Comparing the current WBC data with the previous table WBC data")

    def populateTableData(self):
        return Tables.populateReproducibilityTableData(self,self.left_table_object_symbol,self.right_table_object_symbol)
    
    def confirmTableHasTheRightNumberOfRuns(self,runs):
        table = findObject(self.left_table_object_symbol)
        test.verify(table.getColumnCount() == runs, "Confirm that the expected columns in the table: " + str(runs) + " is equal to the actual runs in the table: " + str(table.getColumnCount()))
    
    def confirmTableNumbers(self):
        table_data = self.populateTableData()
        for index in range(len(table_data)):
            for key in table_data[index].keys():
                if "Rack" in key:
                    test.verify(float(re.sub("[^0-9|.]","",table_data[index][key])) >= 0, "Confirm that every Rack cell in a Rack row contains positive numbers "  + re.sub("[^0-9|.]","",table_data[index][key]))
            
        