# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish

from tables import Tables
from graphs import Graphs

class Controls(Tables,Graphs):
    
    def confirmSelectedItem(self,object,expected_item,comment):
        test.verify(str(object.selecteditem) == expected_item, "Confirm that the " + comment + " selected item is " + expected_item)
        
    def getSelectedComboboxItem(self,object):
        combo_box = squish.findObject(object)
        return str(combo_box.selecteditem)
        
    def confirmTableHeaders(self,object_symbol,table_headers):
        Tables.populateTableData(self,object_symbol)
        table_data = Tables.getTableData(self)
        
        test.verify(len(table_headers) == len(table_data[0]), "Confirm that there are the expected " + str(len(table_headers)) + " columns in the table.")
        
        for key in table_data[0].keys():
            test.verify(table_headers[str(key)] == 0, "Confirm that column " + str(key) + " exists")
                        
    def confirmTableData(self,object_symbol,expected_table_data,comment):
        Tables.populateTableData(self,object_symbol)
        table_data = Tables.getTableData(self)

        test.verify(len(expected_table_data) == len(table_data), "Confirm that there are the expected " + str(len(expected_table_data)) + " rows in the " + comment + " table.")
        
        for row in range(len(expected_table_data)):
            for key in expected_table_data[row].keys():
                test.verify(expected_table_data[row][key] == table_data[row][key], "Confirm that the expected data " + expected_table_data[row][key] + " exists in the " + comment + "table. Actual value: " + table_data[row][key])
            
    def confirmListBoxItems(self,control_object,listbox_items,comment):
       #Verify that the list box contains the expected number of items
        test.verify(len(listbox_items) == control_object.getItemCount(), "Confirm that the " + comment + " List box contains " + str(len(listbox_items)) + " items")

        #Check for each expected item in the listbox        
        for item in range(control_object.getItemCount()):
            item_string = self.removeNonAscii(str(control_object.getItemAt(item)))
            if item_string in listbox_items:
                test.verify(listbox_items[item_string] == 0,"Confirm that the " + comment + " list box contains " + item_string)
            else:
                test.fail(item_string + " does not exist in " + str(listbox_items))

    def getListBoxItems(self,control_object):
        items = []
        #Check for each expected item in the listbox        
        for item in range(control_object.getItemCount()):
            items.append(str(control_object.getItemAt(item)))
        
        return items
            
    def selectComboboxItem(self,object_symbol, item_name):
        exists = False
        combo_box = squish.findObject(object_symbol)
        for index in range(combo_box.getItemCount()):
            if str(combo_box.getItemAt(index)) == item_name:
                combo_box.setSelectedIndex(index)
                exists = True
                break
        return exists
    
    def confirmRadioButton(self,object_symbol, enable, state, text):
        if state.lower() == "selected":
            selected = True
        else:
            selected = False
            
        if enable.lower() == "not-editable":
            enabled = False
        else:
            enabled = True
        
        radio = squish.findObject(object_symbol)
        test.verify(radio.selected == selected,"Confirm that the " + text + " Radio Button is " + state)
        test.verify(radio.enabled == enabled, "Confirm that the " + text + " Radio Button is " + enable)

    
    #This function removes all unicode from a string.
    def removeNonAscii(self,s): 
        return "".join(filter(lambda x: ord(x)<128, s))

    def clickCheckbox(self,checkbox_symbol):
        checkbox = squish.findObject(checkbox_symbol)
        checkbox.doClick()
        
    def confirmCheckboxState(self,checkbox_symbol,selected,name):
        checkbox = squish.findObject(checkbox_symbol)
        if selected.lower() == "selected":
            test.verify(checkbox.selected == True, " Confirm that the " + name + " checkbox is selected")
        else:
            test.verify(checkbox.selected == False, " Confirm that the " + name + " checkbox is not selected")

