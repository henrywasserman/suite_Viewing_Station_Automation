# -*- coding: utf-8 -*-
import __builtin__
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from datetime import datetime, date, time, timedelta
from spritecanvas import SpriteCanvas
from config import Config

class NewDigiCountControlDialog(Controls,SpriteCanvas):
    
    def __init__(self):
        #The next line makes sure that the SpriteCanvas object can see it's own variables
        #when its' methods are called from this class.
        super(NewDigiCountControlDialog, self).__init__()
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.table_symbol = ":Bloodhound™ Viewing Station " + version + "_JTable"
        self.lot_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.level_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.analyzer_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox_2"
        self.expires_month_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField_2"
        self.expires_day_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ". / _JTextField"
        self.expires_year_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ". / _JTextField_2"
        self.active_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Active_JCheckBox"
        
        self.copy_button_1_symbol = ":Bloodhound™ Viewing Station " + version + ".Copy_JButton"
        self.copy_button_2_symbol = ":Bloodhound™ Viewing Station " + version + ".Copy_JButton_2"
        self.clear_button_1_symbol = ":Bloodhound™ Viewing Station " + version + ".Clear_JButton"
        self.clear_button_2_symbol = ":Bloodhound™ Viewing Station " + version + ".Clear_JButton_2"
        self.copy_button_3_symbol = ":Bloodhound™ Viewing Station " + version + ".Copy_JButton_3"
        
        self.left_arrow_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↩_JButton"
        self.right_arrow_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↪_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.new_button_symbol = ":Bloodhound™ Viewing Station " + version + ".New_JButton"
        self.jtabbed_pane_symbol = ":Bloodhound™ Viewing Station " + version + "_JTabbedPane"
        
        self.scan_dictionary = {"low":"S1401001L", "normal":"S1401001N","high":"S1401001H"}
        
    def clickTab(self):
        clickTab(self.object_symbol)

    def clickCopyButton1(self):
        clickButton(self.copy_button_1_symbol)
        
    def clickCopyButton2(self):
        clickButton(self.copy_button_2_symbol) 
        
    def clickCopyButton3(self):
        clickButton(self.copy_button_3_symbol)
        
    def clickClearButton1(self):
        clickButton(self.clear_button_1_symbol)
        
    def clickClearButton2(self):
        clickButton(self.clear_button_2_symbol)
    
    def clickLeftArrowButton(self):
        clickButton(self.left_arrow_button_symbol)
    
    def clickRightArrowButton(self):
        clickButton(self.right_arrow_button_symbol)
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def clickNewButton(self):
        clickButton(self.new_button_symbol)
        
    def confirmLevelComboBoxSelectedItem(self,expected_item):
        level = findObject(self.level_combobox_symbol)
        Controls.confirmSelectedItem(self,level,expected_item, "Level")
        
    def setLotNumber (self,lot_number):
        lot = findObject(self.lot_textfield_symbol)
        lot.text = lot_number
        
    def setExpirationDate(self):
        
        thirty_days_from_now = datetime.now() + timedelta(days = 30)
        
        month = str(thirty_days_from_now.month)
        day = str(thirty_days_from_now.day)
        year = str(thirty_days_from_now.year)
        
        month_textfield = findObject(self.expires_month_textfield_symbol)
        day_textfield = findObject(self.expires_day_textfield_symbol)
        year_textfield = findObject(self.expires_year_textfield_symbol)
        
        month_textfield.text = month
        day_textfield.text = day
        year_textfield.text = year
        
        mouseClick(self.expires_month_textfield_symbol,10, 20, 0, Button.Button1 )
        mouseClick(self.expires_day_textfield_symbol,10, 20, 0, Button.Button1 )
        
    def enterDigiCountTableData(self,filename):        
        table_object = findObject(self.table_symbol)
        Tables.enterDigiCountTableData(self,table_object,filename)
        
    def confirmDigiCountTableData(self,filename):
        table_object = findObject(self.table_symbol)
        Tables.confirmDigiCountTableData(self,table_object,filename)
                
    def confirmLotNumber(self,lot_number):
        lot = findObject(self.lot_textfield_symbol)
        test.verify(lot.text == lot_number,"Confirm that the expected lot number : " + lot_number + " is equal to the actual lot number: " + lot.text) 
    
    def confirmDefaultAnalyzerComboBoxSelectedItem(self):
        analyzer = findObject(self.analyzer_combobox_symbol)
        Controls.confirmSelectedItem(self,analyzer,"Bloodhound 1", "Analyzer")
        
    def confirmAnalyzerComboBoxSelectedItem(self,analyzer_item):
        analyzer = findObject(self.analyzer_combobox_symbol)
        Controls.confirmSelectedItem(self,analyzer,analyzer_item, "Analyzer")        
        
    def confirmExpiresDate(self):
        thirty_days_from_now = datetime.now() + timedelta(days = 30)
        
        month = str(thirty_days_from_now.month)
        day = str(thirty_days_from_now.day)
        year = str(thirty_days_from_now.year)
        
        if __builtin__.int(month) < 10:
            month = "0" + month
            
        if __builtin__.int(day) < 10:
            #This is just in case we don't need the 0 character buffer
            day_other = day
            day = "0" + day
            
                
        month_textfield = findObject(self.expires_month_textfield_symbol)
        day_textfield = findObject(self.expires_day_textfield_symbol)
        year_textfield = findObject(self.expires_year_textfield_symbol)
        
        test.verify(month == str(month_textfield.text),"Confirm that the expected month: " + month + " is equal to the month that is displayed " + str(month_textfield.text))
        test.verify(day == str(day_textfield.text) or day_other == str(day_textfield.text),"Confirm that the expected day: " + day + " is equal to the day that is displayed: " + str(day_textfield.text))
        test.verify(year == str(year_textfield.text),"Confirm that the expected year: " + year + " is equal to the year that is displayed: " + str(year_textfield.text)) 
    
    def confirmDefaultActiveCheckBox(self):
        active = findObject(self.active_checkbox_symbol)
        test.verify(active.selected == False, "Confirm that the active checkbox exists and is not checked by default")
            
    def confirmHistoricalSDEntries(self):
        table = findObject(self.table_symbol)        
        Tables.populateTableData(self,self.table_symbol)
        table_data = Tables.getTableData(self)
        
        for row in range(len(table_data)):
            test.verify(__builtin__.float(table_data[row]['Historical\nSD']) >= 0, "Confirm that row " + str(row) + " in the New DigiCount Control Historical SD Table contains data.")
        
    def getRangeRendering(self):
        range = {}
        table = findObject(self.table_symbol)
        #In this case the range is located in the 3rd column (2)
        cell = table.getCellRenderer(0,2)
        
        field = cell.getClass().getDeclaredField("low")
        field.setAccessible(True)
        low = field.get(cell)
        range["low"] = low.text
        
        field = cell.getClass().getDeclaredField("dash")
        field.setAccessible(True)
        dash = field.get(cell)
        range["dash"] = dash.text

        field = cell.getClass().getDeclaredField("high")
        field.setAccessible(True)
        high = field.get(cell)
        range["high"] = high.text
        
        return range
    
    def confirmDialogWasDismissed(self):
        dialog = findObject(self.object_symbol)
        test.verify(dialog.getName() == "null.contentPane", "Confirm that the dialog box has been dismissed")
    
    def selectLevelComboboxItem(self,item_name):
        Controls.selectComboboxItem(self, self.level_combobox_symbol, item_name)
        
    def digiCountTableDataToCSV(self, filename):
        table = findObject(self.table_symbol)
        Tables.digiCountTableDataToCSV(self,table , filename)
        
    def simulateDigiCountScan(self,control_type):
        config = Config()

        if control_type.lower() == "low":
            self.selectLevelComboboxItem("Low DigiCount™ control")
            self.enterDigiCountTableData(getattr(config,"expected_csv_result_dir") + "/digicountlow.csv")

        elif control_type.lower() == "normal":
            self.selectLevelComboboxItem("Normal DigiCount™ control")
            self.enterDigiCountTableData(getattr(config,"expected_csv_result_dir") + "/digicountnormal.csv")

        elif control_type.lower() == "high":
            self.selectLevelComboboxItem("High DigiCount™ control")
            self.enterDigiCountTableData(getattr(config,"expected_csv_result_dir") + "/digicounthigh.csv")
        
        self.setLotNumber(self.scan_dictionary[control_type.lower()])
        self.setExpirationDate()
        self.clickNewButton()
        
        