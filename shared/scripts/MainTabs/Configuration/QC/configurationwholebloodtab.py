# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from configurationqctab import ConfigurationQCTab

class ConfigurationWholeBloodTab(ConfigurationQCTab):
    
    def __init__(self):
        self.object_symbol = ":QC.Whole Blood_TabProxy_2"
        self.whole_blood_table_symbol = ":Whole Blood_JTable"
        self.analyzer_combobox_symbol = ":Whole Blood. _JComboBox"
        self.mode_open_radio_button_symbol = ":Whole Blood.Open_JRadioButton"
        self.mode_rack_or_stat_radio_button_symbol = ":Whole Blood.Rack or STAT_JRadioButton"
        self.mode_either_radio_button_sybmol = ":Whole Blood.Either_JRadioButton"
        self.alert_level_combobox_symbol = ":Whole Blood. _JComboBox_2"
        
    def clickTab(self):
        clickTab(self.object_symbol)

    #Confirm the table contains the following columns:
    #-Parameter
    #-Absolute
    #-Percent
    #Confirm the Preferred Reference table contains the following:
    #-Analyzer combobox with "Mean" as the default
    #-Analyzer combobox has the following values: "Mean", "Analyzer_name"
    #-Mode has 3 radio buttons "Open", "Rack or STAT", and "Either" (where "Either" is the default)
    #Confirm the Alert Level table contains the following options in the combobox:
    #-"Lockout"
    #-"Attention" 
    #-"Ignore" (default)
    def confirmDefaultControlsAndValues(self):
        #Sanity check - Take a wholeblood screen shot
        test.vp("WholeBlood")
        
        whole_blood_columns = {'Parameter':0, 'Absolute':0, 'Percent':0}
        self.confirmTableHeaders(self.whole_blood_table_symbol,whole_blood_columns)
               
        #TODO: These table data tests are not defined above.  Just threw them in.  We might need them later.     
        expected_whole_blood_table_data = [{'Percent': '0.031000000000000007', 'Parameter': 'WBC (10/L)', 'Absolute': '0.5'}, 
                                           {'Percent': '0.017', 'Parameter': 'RBC (10/L)', 'Absolute': '0.1'}, 
                                           {'Percent': '0.013999999999999999', 'Parameter': 'HGB (g/dL)', 'Absolute': '0.2'}, 
                                           {'Percent': '0.026000000000000002', 'Parameter': 'HCT (%)', 'Absolute': '1.3'}, 
                                           {'Percent': '0.022000000000000002', 'Parameter': 'MCV (fL)', 'Absolute': '2.0'}, 
                                           {'Percent': '0.019', 'Parameter': 'MCH (pg)', 'Absolute': '0.6'}, 
                                           {'Percent': '0.028999999999999998', 'Parameter': 'MCHC (g/dL)', 'Absolute': '1.0'}, 
                                           {'Percent': '0.031000000000000007', 'Parameter': 'RDW (%)', 'Absolute': '0.5'}, 
                                           {'Percent': '0.031000000000000007', 'Parameter': 'RDW-SD (fL)', 'Absolute': '0.4'}, 
                                           {'Percent': '0.18', 'Parameter': 'PLT (10/L)', 'Absolute': '15.0'}, 
                                           {'Percent': '0.086', 'Parameter': 'MPV (fL)', 'Absolute': '0.6'}, 
                                           {'Percent': '0.1', 'Parameter': '%NRBC (/100WBC)', 'Absolute': '1.0'}, 
                                           {'Percent': '0.1', 'Parameter': '#NRBC (10/L)', 'Absolute': '1.0'}, 
                                           {'Percent': '0.027999999999999997', 'Parameter': '%NEUT (%)', 'Absolute': '1.6'}, 
                                           {'Percent': '0.071', 'Parameter': '%LYMPH (%)', 'Absolute': '1.4'}, 
                                           {'Percent': '0.152', 'Parameter': '%MONO (%)', 'Absolute': '1.4'}, 
                                           {'Percent': '0.157', 'Parameter': '%EO (%)', 'Absolute': '0.3'}, 
                                           {'Percent': '1.0', 'Parameter': '%BASO (%)', 'Absolute': '0.5'}, 
                                           {'Percent': '0.1', 'Parameter': '%UNCLASS (%)', 'Absolute': '1.0'}, 
                                           {'Percent': '0.153', 'Parameter': '#NEUT (10/L)', 'Absolute': '0.8'}, 
                                           {'Percent': '0.28', 'Parameter': '#LYMPH (10/L)', 'Absolute': '0.5'}, 
                                           {'Percent': '0.8', 'Parameter': '#MONO (10/L)', 'Absolute': '0.6'}, 
                                           {'Percent': '0.85', 'Parameter': '#EO (10/L)', 'Absolute': '0.1'}, 
                                           {'Percent': '1.0', 'Parameter': '#BASO (10/L)', 'Absolute': '0.2'}, 
                                           {'Percent': '0.1', 'Parameter': '#UNCLASS (10/L)', 'Absolute': '1.0'}, 
                                           {'Percent': '0.3', 'Parameter': '%RET (%)', 'Absolute': '0.5'}, 
                                           {'Percent': '1.0', 'Parameter': '#RET (10/L)', 'Absolute': '0.1'}, 
                                           {'Percent': '0.1', 'Parameter': 'HGBr (pg)', 'Absolute': '1.0'}
        
                                        ]
        #Again the single line test below is not defined above.
        self.confirmTableData(self.whole_blood_table_symbol,expected_whole_blood_table_data,"Whole Blood:")
        
        #Confirm the Preferred Reference table contains the following:
        #-Analyzer combobox with "Mean" as the default
        #-Analyzer combobox has the following values: "Mean", "Analyzer_name"
        #-Mode has 3 radio buttons "Open", "Rack or STAT", and "Either" (where "Either" is the default)
        #Confirm the Alert Level table contains the following options in the combobox:
        #-"Lockout"
        #-"Attention" 
        #-"Ignore" (default) 
        analyzer_combo_box = findObject(self.analyzer_combobox_symbol)
        mode_open_radio_button = findObject(self.mode_open_radio_button_symbol)
        mode_rack_or_stat_radio_button = findObject(self.mode_rack_or_stat_radio_button_symbol)
        mode_either_radio_button = findObject(self.mode_either_radio_button_sybmol)
        alert_level_combobox = findObject(self.alert_level_combobox_symbol)
        
        #-Analyzer combobox with "Mean" as the default
        self.confirmSelectedItem(analyzer_combo_box,"Mean", "Analyzer")
        #-Analyzer combobox has the following values: "Mean", "Analyzer_name"
        analyzer_items = {'Mean':0, 'Bloodhound 1':0, 'Bloodhound 2':0}
        self.confirmListBoxItems(analyzer_combo_box, analyzer_items, "Analyzer")
        
        #-Mode has 3 radio buttons "Open", "Rack or STAT", and "Either" (where "Either" is the default)
        test.verify(mode_open_radio_button.selected == False, "Confirm that the Open radio button is not seleted by default")
        test.verify(mode_rack_or_stat_radio_button.selected == False, "Confirm that the Rack or STAT radio button is not selected by default")
        test.verify(mode_either_radio_button.selected == True, "Confirm that the Either radio button is selected by default")
        
        #Confirm the Alert Level table contains the following options in the combobox:
        #-"Lockout"
        #-"Attention" 
        #-"Ignore" (default) 
        self.confirmSelectedItem(alert_level_combobox,"Ignore", "Alert Level")
        alert_level_items = {'Lockout':0, 'Attention':0, 'Ignore':0}
        self.confirmListBoxItems(alert_level_combobox, alert_level_items, "Analyzer")

