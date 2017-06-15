# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import os, time
import squishinfo
import squish

from stat import ST_MTIME
from time import strftime
from tables import Tables
from config import Config

class ExportAllFileDialog(Tables):
    
    def __init__(self):
        version = Config().version
        self.object_symbol =                    ":Bloodhound™ Viewing Station " + version + "_FileDialog"
        self.save_as_table_symbol =             ":Bloodhound™ Viewing Station " + version + ".Save As:_JTable"
        self.save_as_label_symbol =             ":Bloodhound™ Viewing Station " + version + ".Save As:_JLabel"
        self.where_label_symbol =               ":Bloodhound™ Viewing Station " + version + ".Where:_JLabel"
        self.file_name_text_symbol =            ":Bloodhound™ Viewing Station " + version + ".Save As:_JTextField"
        self.up_arrow_button_symbol =           ":Bloodhound™ Viewing Station " + version + ".↑_JButton"
        self.down_arrow_button_symbol =         ":Bloodhound™ Viewing Station " + version + ".↓_JButton"
        self.filter_selector_combo_box_symbol = ":Bloodhound™ Viewing Station " + version + ".Files of type:_JComboBox"
        self.where_combo_box_symbol =           ":Bloodhound™ Viewing Station " + version + ".Where:_JComboBox"
        self.export_button_symbol =             ":Bloodhound™ Viewing Station " + version + ".Export_JButton"
        self.export_current_symbol =            ":Archives.Export Current_JButton"
        self.safely_remove_checkbox =           ":Bloodhound™ Viewing Station " + version + ".Safely remove “Untitled” after export_JCheckBox"
        self.plus_button_symbol =               ":Bloodhound™ Viewing Station " + version + ".+_JButton"
        self.cancel_button_symbol =             ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.save_as_table_header_symbol =      ":Bloodhound™ Viewing Station " + version + "_JTableHeader"
        
        self.file_exists_messagebox_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.file_exists_overwrite_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Overwrite_JButton"
    
    def confirmSaveAsLabel(self,text):
        test.verify(squish.findObject(self.save_as_label_symbol).text == text,"Confirm that the Save as label is: " + text)
        
    def confirmWhereLabel(self,expected_text):
        text = squish.findObject(self.where_label_symbol).text
        test.verify( expected_text == text, "Confirm that the expected text: " + expected_text + " for the Where label is " + text)
        
    def confirmFileNameTxt(self,text):
        test.verify(squish.findObject(self.file_name_text_symbol).text == text,"Confirm that the Save as edit box contains the text: " + text)
        
    def confirmUpArrowButton(self,status):
        test.verify(object.exists(self.up_arrow_button_symbol) == True, "Confirm that the up arrow button exists")
        if status == "enabled":
            test.verify(squish.findObject(self.up_arrow_button_symbol).enabled == True,"Confirm that the up arrow button is enabled")
        else:
            test.verify(squish.findObject(self.up_arrow_button_symbol).enabled == False,"Confirm that the up arrow button is disabled")            
        
    def pressUpArrowButtonUntilItIsDisabled(self):
        up_arrow_button = squish.findObject(self.up_arrow_button_symbol)
        while (up_arrow_button.enabled == True):
            squish.clickButton(up_arrow_button)
            
    def confirmDownArrowButton(self,status):
        test.verify(object.exists(self.down_arrow_button_symbol) == True, "Confirm that the down arrow button exists")
        if status == "enabled":
            test.verify(squish.findObject(self.down_arrow_button_symbol).enabled == True,"Confirm that the down arrow button is enabled")
        else:
            test.verify(squish.findObject(self.down_arrow_button_symbol).enabled == False,"Confirm that the down arrow button is enabled")
            
    def pressDownArrowButton(self):
        down_arrow_button = squish.findObject(self.down_arrow_button_symbol)
        squish.clickButton(down_arrow_button)
        
    def pressUpArrowButton(self):
        up_arrow_button = squish.findObject(self.up_arrow_button_symbol)
        squish.clickButton(up_arrow_button)        
        
    def confirmFilterSelectorComboBox(self,status):
        test.verify(object.exists(self.filter_selector_combo_box_symbol) == True, "Confirm that the Filter Selector ComboBox button exists")
        if status == "enabled":
            test.verify(squish.findObject(self.filter_selector_combo_box_symbol).enabled == True,"Confirm that the Filter Selector ComboBox is enabled")
        else:
            test.verify(squish.findObject(self.filter_selector_combo_box_symbol).enabled == False,"Confirm that the Filter Selector ComboBox is enabled")
            
    def confirmSafelyRemoveCheckbox(self,status,drive):
        label = "Safely remove " + drive + " after export" 
        test.verify(object.exists(self.safely_remove_checkbox) == True, "Confirm that the Safely remove checkbox exists")
        test.verify(str(squish.findObject(self.safely_remove_checkbox).label) == label, "Confirm that the Safely remove checkbox label displays: " + label)
        if status == "enabled":     
            test.verify(squish.findObject(self.safely_remove_checkbox).enabled == True,"Confirm that the Safely Remove Checkbox is enabled")
        else:
            test.verify(squish.findObject(self.safely_remove_checkbox).enabled == False,"Confirm that the Safely Remove Checkbox is disabled")
            
    def confirmSafelyRemoveCheckboxState(self,state):
        if state == "checked":
            test.verify(squish.waitForObject(self.safely_remove_checkbox).selected == True,"Confirm that the Safely Remove Checkbox is checked")
        else:
            test.verify(squish.findObject(self.safely_remove_checkbox).selected == False,"Confirm that the Safely Remove Checkbox is not checked")
    
    def clickSafelyRemoveCheckbox(self):
        checkbox = squish.findObject(self.safely_remove_checkbox)
        checkbox.doClick()
    
    def deleteFilename(self):
        squish.findObject(self.file_name_text_symbol).text = ""
        
    def confirmExportButton(self,status):
        if status == "enabled":            
            test.verify(squish.findObject(self.export_button_symbol).enabled == True,"Confirm that the Export button is enabled")
        else:
            test.verify(squish.findObject(self.export_button_symbol).enabled == False,"Confirm that the Export button is disabled")
            
    def confirmCancelButton(self,status):
        if status == "enabled":
            test.verify(squish.findObject(self.cancel_button_symbol).enabled == True, "Confirm that the Cancel button is enabled")
        else:
            test.verify(squish.findObject(self.cancel_button_symbol).enable == False, "Confirm that the Cancel button is disabled")
            
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
            
    def clickExportButton(self):
        squish.clickButton(squish.waitForObject(self.export_button_symbol))
        counter = 0
        #Test for 3 seconds if file exists message box pops up
        while (True):
            if object.exists(self.file_exists_messagebox_symbol):
                messagebox = squish.findObject(self.file_exists_messagebox_symbol)
                if str(messagebox.name) == "LayeredDialog-File Exists":
                    self.clickOverwriteButton()
                    break
            
            squish.snooze(1.0)
            counter += 1
            
            if counter == 3:
                break

    def clickOverwriteButton(self):
        squish.clickButton(self.file_exists_overwrite_button_symbol)
    
    def clickExportCurrentButton(self):
        squish.clickButton(self.export_current_symbol)
        
    def confirmPlusButton(self,status):
        test.verify(object.exists(self.plus_button_symbol) == True, "Confirm that the Plus button exists")
        if status == "enabled":
            test.verify(squish.findObject(self.plus_button_symbol).enabled == True, "Confirm that the Plus button is enabled")
        else:
            test.verify(squish.findObject(self.plus_button_symbol).enabled == False, "Confirm that the Plus button is disabled")
            
    def clickPlusButton(self):
        squish.clickButton(squish.findObject(self.plus_button_symbol))
        
    def setFilename(self,filename):
        squish.findObject(self.file_name_text_symbol).text = filename
        
    def confirmNameColumnSortOrder(self,column,expected_sort_order):
        order = squish.findObject(self.save_as_table_symbol).getRowSorter().getSortKeys().get(0).getSortOrder()
        
        if (column == 0):
            actual_sort_order = order
        #TODO:  Find a better way to do this
        #But For now, I found a reliable way of testing the Date Column Sort Order
        #The logic here is that when the Name column is reliably returning being sorted one way, 
        #the Date column is always sorted the opposite way.
        else:
            if str(order) == "ASCENDING":
                actual_sort_order = "DESCENDING"
            else:
                actual_sort_order = "ASCENDING"
        
        test.verify(expected_sort_order == str(actual_sort_order),"Confirm that the expected order " + str(expected_sort_order) + " is being used: " + str(actual_sort_order))
        
    def confirmColumnName(self,column,name):
        column_name = squish.findObject(self.save_as_table_header_symbol).getColumnModel().getColumn(column).getHeaderValue().toString()
        test.verify(name == str(column_name).strip(), "Confirm that the expected Column name for column " + str(column) + " is " + column_name)
        
    def clickOnNameColumn(self):
        #Click on the name column
        squish.mouseClick(":     Name_TableHeaderItemProxy")
        
    def clickOnDateColumn(self):
        #Click on the date column
        squish.mouseClick(":Date_TableHeaderItemProxy")
        
    def confirmDateCellRenderer(self):
        #Get the table
        table = squish.findObject(self.save_as_table_symbol)
        #Select the first for in the Table this helps getCellRenderer get the right row
        table.setRowSelectionInterval(0,0)
        #Get the Formated Date from the first cell in the Date Column (column 1)
        table_formatted_date_or_time = table.getCellRenderer(0,1).getText()
        #Get the path and filename from that column
        filename = table.getModel().getValueAt(0,0)
        file = os.stat(str(filename))
        file_formatted_date = str(time.localtime(file[ST_MTIME])[1]) + "/" + str(time.localtime(file[ST_MTIME])[2]) + "/" + str(time.localtime(file[ST_MTIME])[0])[2:]
        file_formatted_time = self.getTime(os.stat(str(filename)))
        if ":" in table_formatted_date_or_time:
            test.verify(table_formatted_date_or_time == file_formatted_time,"Confirm that the table time " + table_formatted_date_or_time + " is equal to the modified file time " + file_formatted_time)
        else:
            test.verify(table_formatted_date_or_time == file_formatted_date,"Confirm that the table date " + table_formatted_date_or_time + " is equal to the modified file date " + file_formatted_date)
        
    def confirmTxtOnlyInSaveAsTable(self):
        #Get the table
        table = squish.findObject(self.save_as_table_symbol)
        # Make sure every filename in the table ends in .txt
        for row in range(table.getRowCount()):
            if os.path.isfile(str(table.getValueAt(row,0))):
                test.verify(str(table.getValueAt(row,0)).endswith(".txt") != False,"Confirm that each file in the table ends with .txt " + str(table.getValueAt(row,0)))
            
    def confirmMoreThanTxtOnlyInSaveAsTable(self):
        #Get the table
        table = squish.findObject(self.save_as_table_symbol)
        # Make sure every filename in the table ends in .txt
        result = False
        for row in range(table.getRowCount()):
            if os.path.isfile(str(table.getValueAt(row,0))) and str(table.getValueAt(row,0)).endswith(".txt") == False:
                result = True
                break
            
        test.verify(result == True,"Confirm that there is at least one file in the table that does not have .txt at the end" + str(table.getValueAt(row,0)))
         
        
    def doubleClickOnTableRowByName(self,field_name,cell_value):
        Tables.populateTableData(self,self.save_as_table_symbol)
        Tables.doubleClickOnTableRowByName(self,self.save_as_table_symbol,field_name,cell_value)
        
    def clickOnTableRowByName(self,object_symbol,field_name,cell_value):
        Tables.populateTableData(self,self.save_as_table_symbol)
        Tables.clickOnTableRowByName(self,object_symbol,field_name,cell_value)
        
    def confirmWhereComboSelection(self,selected):
        selection = str(squish.findObject(self.where_combo_box_symbol).selecteditem)
        test.verify(selected == selection,
            "Confirm that the expected selection: " + selected + " is selected " + selection)
        
    def confirmFilterSelectorComboBoxSelection(self,selected):
        selection = str(squish.findObject(self.filter_selector_combo_box_symbol).selecteditem.getDescription())
        test.verify(selected == selection,
            "Confirm that the expected selection: " + selected + " is selected " + selection)
        
    def confirmFolderSelectorComboBoxItems(self,expected_items):
        item_list = expected_items.split(",")
        combo = squish.findObject(self.where_combo_box_symbol)
        for index in range(len(item_list)):
            test.verify(item_list[index] == str(combo.getItemAt(index)), "Confirm that expected item: " + item_list[index] + " is equal to " + str(combo.getItemAt(index)))
   
    def confirmFilterSelectorComboBoxItems(self,items):
        item_list = items.split(",")
        combo = squish.findObject(self.filter_selector_combo_box_symbol)
        for index in range(combo.getItemCount()):
            test.verify(item_list[index] == str(combo.getItemAt(index).getDescription()), 
                "Confirm that expected item: " + item_list[index] + " is equal to " + str(combo.getItemAt(index).getDescription()))
    
    def selectFilterSelectorComboBoxItem(self,item):
        combo = squish.findObject(self.filter_selector_combo_box_symbol)
        for index in range(combo.getItemCount()):
            if str(combo.getItemAt(index).getDescription()) == item:
                combo.setSelectedIndex(index)
                break
            
    def selectFolderSelectorComboBoxItem(self,item):
        combo = squish.findObject(self.where_combo_box_symbol)
        for index in range(combo.getItemCount()):
            if str(combo.getItemAt(index)) == item:
                combo.setSelectedIndex(index)
                break
        
    def goToCurrentPath(self):
        where = "/Volumes/SmokeTest"
        self.selectFolderSelectorComboBoxItem(where)
        
        current_path = os.getcwd()
        paths = current_path.split("/")
    
        for path in paths:
            if not path:
                continue
            where += "/" + path 
            self.doubleClickOnTableRowByName("     Name",where)
            
        return where
    
    def getTime(self,file):
        if time.localtime(file[ST_MTIME])[3] <= 11:
            if time.localtime(file[ST_MTIME])[3] == 0:
                hour = "12"
            else:
                hour = str(time.localtime(file[ST_MTIME])[3])
            time_of_day = "AM"
        else:
            if time.localtime(file[ST_MTIME])[3] == 12:
                hour = "12"
            else:
                hour = str(time.localtime(file[ST_MTIME])[3] - 12)
            time_of_day = "PM"
                    
        time_string = hour + ":" + str(time.localtime(file[ST_MTIME])[4]) + " " + time_of_day
            
        return time_string