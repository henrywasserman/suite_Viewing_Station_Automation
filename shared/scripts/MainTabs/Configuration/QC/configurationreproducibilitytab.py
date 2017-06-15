# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from configurationqctab import ConfigurationQCTab

class ConfigurationReproducibilityTab(ConfigurationQCTab):
    
    def __init__(self):
        self.object_symbol = ":QC.Reproducibility_TabProxy_2"
        self.reproducibility_test_label = ":Reproducibility.Reproducibility Test_JLabel"
        self.number_of_runs_reproducibility_symbol_textfield = ":Reproducibility_JTextField"
        self.alert_level_listbox = ":Reproducibility. _JComboBox"
        
    def clickTab(self):
        clickTab(self.object_symbol)

    #Confirm there is a Reproducibility Test section
    #Confirm this section has the following controls:
    #-Number of runs in Reproducibility test <editable field> Runs
    #-<editable field> defaults to 20
    #-Alert Level combobox has "Ignore" selection as default
    #-Alert Level combobox has the following values: "Lockout", "Attention", and "Ignore"
    def confirmDefaultControlsAndValues(self):
        test.log("Take a screenshot for a sanity check of the location of all objects on this tab")
        test.vp("Reproducibility")
        
        reproducibility_test_label = findObject(self.reproducibility_test_label)
        number_of_runs = findObject(self.number_of_runs_reproducibility_symbol_textfield)
        alert_level = findObject(self.alert_level_listbox)
        
        test.verify(reproducibility_test_label.text == "Reproducibility Test", "Confirm there is a Reproducibility Test section")
        test.verify(number_of_runs.text == "20","Confirm Number of runs in Reproducibility test <editable field> Runs -<editable field> defaults to 20")
        ConfigurationQCTab.confirmSelectedItem(self,alert_level,"Ignore","Alert Level")
        
        alert_level_items = {'Lockout':0, 'Attention':0, 'Ignore':0}
        ConfigurationQCTab.confirmListBoxItems(self,alert_level,alert_level_items,"Alert Level")
        