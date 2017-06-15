# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish

from configurationtab import ConfigurationTab

class ConfigurationRulesTab(ConfigurationTab):
    
    def __init__(self):
        self.object_symbol = ":Configuration.Rules_TabProxy"
        self.top_left_rules_table_symbol = ":Rules_JTable"
        self.bottom_left_rules_table_symbol = ":Rules_JTable_2"
        self.duplicate_button_symbol = ":Rules.Duplicate_JButton"
        self.up_button_symbol = ":Rules.^_JButton"
        self.down_button_symbol = ":Rules.v_JButton"
        self.minus_button_symbol = ":Rules.-_JButton"
        self.plus_button_symbol = ":Rules.+_JButton"
        
        self.messages_tab_symbol = ":Rules.Messages_TabProxy"
        self.flags_tab_symbol = ":Rules.Flags_TabProxy"
        self.morphology_tab_symbol = ":Rules.Morphology_TabProxy"
        self.deltas_tab_symbol = ":Rules.Deltas_TabProxy"
        self.limits_tab_symbol = ":Rules.Limits_TabProxy"
        self.actions_tab_symbol = ":Rules.Actions_TabProxy"
        
        self.rollback_listbox_symbol = ":Rules_JComboBox"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    #Confirm the table at the left corner contains the following columns:
    #-ID
    #-Description
    #-Modified
    #Confirm that below the table the following is displayed:
    #-Duplicate button
    #Confirm the table at the left corner contains the following columns:
    #-ID
    #-Condition
    #Confirm that below the table the following is displayed:
    #-“↑” and “↓” buttons to move the selected rule set up or down
    #-"+" and "-" buttons
    #Confirm the section on right side of the Rules tab contains the following subtabs: 
    #-Messages
    #-Flags
    #-Morphology
    #-Deltas
    #-Limits 
    #-Actions
    #Confirm the tab bar will also contain a combobox whose text displays “Rollback…”.
    def confirmDefaultControlsAndValues(self):
        duplicate_button = findObject(self.duplicate_button_symbol)
        
        up_button = findObject(self.up_button_symbol)
        down_button = findObject(self.down_button_symbol)
        minus_button = findObject(self.minus_button_symbol)
        plus_button = findObject(self.plus_button_symbol)
        
        
        messages_tab = findObject(self.messages_tab_symbol)
        flags_tab = findObject(self.flags_tab_symbol)
        morphology_tab = findObject(self.morphology_tab_symbol)
        deltas_tab = findObject(self.deltas_tab_symbol)
        limits_tab = findObject(self.limits_tab_symbol)
        actions_tab = findObject(self.actions_tab_symbol)
        
        rollback_listbox = findObject(self.rollback_listbox_symbol)
        
        top_left_table_columns = {'ID':0, 'Description ':0, 'Modified':0}
        self.confirmTableHeaders(self.top_left_rules_table_symbol,top_left_table_columns)
        
        test.verify(duplicate_button.enabled == True, "Confirm that the Duplicate Button exists and is enabled by default")
        
        #Confirm the table at the left corner contains the following columns:
        #-ID
        #-Condition
        bottom_left_table_columns = {'ID':0, 'Condition':0}
        self.confirmTableHeaders(self.bottom_left_rules_table_symbol, bottom_left_table_columns)
        
        #Confirm that below the table the following is displayed:
        #-“↑” and “↓” buttons to move the selected rule set up or down
        #-"+" and "-" buttons
        test.verify(up_button.enabled == False, "Confirm that the up button is disabled by default.")
        test.verify(down_button.enabled == False, "Confirm that the down button is disabled by default.")
        test.verify(minus_button.enabled == False, "Confirm that the minus button is disabled by default.")
        test.verify(plus_button.enabled == True, "Confirm that the plus button is enabled by default.")
        
        
        #Confirm the section on right side of the Rules tab contains the following subtabs: 
        #-Messages
        #-Flags
        #-Morphology
        #-Deltas
        #-Limits 
        #-Actions
        #Confirm the tab bar will also contain a combobox whose text displays “Rollback…”.
        test.verify(messages_tab.text == "Messages","Confirm that the messages tab exists by default.")
        test.verify(flags_tab.text == "Flags","Confirm that the flags tab exists by default.")
        test.verify(morphology_tab.text == "Morphology", "Confirm the morphology exists by default")
        test.verify(deltas_tab.text == "Deltas","Confirm that the deltas tab exists by default")
        test.verify(limits_tab.text == "Limits","Confirm that the limits tab exists by default")
        test.verify(actions_tab.text == "Actions","Confirm that the actions tab exists by default")
        
        self.confirmSelectedItem(rollback_listbox, "Rollback...","Rollback")