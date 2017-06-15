# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from configurationtab import ConfigurationTab
from config import Config

class AnalyzersTab(ConfigurationTab):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Configuration.Analyzers_TabProxy"
        self.analyzer_table_symbol = ":Analyzers_JTable"
        self.analyzer_table_controlVS_cell_symbol = ":0_1_TableItemProxy"
        self.analyzer_table_LIS_VS_cell_symbol = ":0_2_TableItemProxy_2"
        self.analyzer_tabel_control_listbox_symbol = ":Bloodhound™ Viewing Station " + version + "_JList"
        self.delete_button_symbol = ":Analyzers.Delete_JButton"
        self.viewing_station_name_textfield_symbol = ":Analyzers.This Viewing Station's name_PlaceholderOverlay"
        self.cleaning_solution_button_symbol = ":Analyzers.Cleaning Solution_JButton"
        
    def clickTab(self):
        clickTab(self.object_symbol)

    #Confirm the table contains the following columns:
    #-Analyzer Name
    #-Control Viewing Station
    #-LIS Viewing Station
    #When the columns are clicked, they become editable combobox
    #Confirm that below the table the following is displayed:
    #-"Delete" button (inactive)
    #-"Viewing Station's name" text field
    def confirmDefaultControlsAndValues(self):
        analyzer_columns = {'Analyzer Name':0, 'Control Viewing Station':0, 'LIS Viewing Station':0}
        self.confirmTableHeaders(self.analyzer_table_symbol,analyzer_columns)

        analyzer_table_controlVS_cell = findObject(self.analyzer_table_controlVS_cell_symbol)
        analyzer_table_LIS_VS_cell = findObject(self.analyzer_table_LIS_VS_cell_symbol)
        delete_button = findObject(self.delete_button_symbol)
        viewing_station_name = findObject(self.viewing_station_name_textfield_symbol)

        
        #When the columns are clicked, they become editable comboboxes
        mouseClick(analyzer_table_controlVS_cell, 221, 12, 0, Button.Button1)
        listbox_item = waitForObjectItem(self.analyzer_tabel_control_listbox_symbol, "_0")
        mouseClick(waitForObjectItem(self.analyzer_tabel_control_listbox_symbol, "_0"), 78, 11, 0, Button.Button1)
        test.verify(listbox_item.text == "Simulator","Confirm that the listbox in the Control Viewing Station Column exists and contains the string Simulator")
        mouseClick(analyzer_table_LIS_VS_cell, 180, 13, 0, Button.Button1)
        listbox_item = waitForObjectItem(self.analyzer_tabel_control_listbox_symbol, "_0")
        mouseClick(waitForObjectItem(self.analyzer_tabel_control_listbox_symbol, "_0"), 78, 11, 0, Button.Button1)
        test.verify(listbox_item.text == "Simulator","Confirm that the listbox in the LIS Viewing Station Column exists and contains the string Simulator")
        
        #Confirm that below the table the following is displayed:
        #-"Delete" button (inactive)
        #-"Viewing Station's name" text field
        test.verify(delete_button.enabled == False, "Confirm that the Delete Button is disabled by default")
        test.verify(viewing_station_name.visible == True, "Confirm that the Viewing Station's name edit box exists and is visible by default")
