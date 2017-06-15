# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class RunMaintenanceActionDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.analyzer_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.profile_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox_2"
        self.repeat_count_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.run_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Run_JButton"
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def clickRunButton(self):
        clickButton(self.run_button_symbol)
        
    def selectAnalyzerItem(self,item):
        Controls.selectComboboxItem(self,self.analyzer_combobox_symbol, item)
        
    def selectProfileItem(self,item):
        Controls.selectComboboxItem(self,self.profile_combobox_symbol, item)
        
    def setRepeatCountText(self,text):
        repeat_count = findObject(repeat_count_textfield_symbol)
        repeat_count.text = text
        
    def confirmProfileSelected(self,item):
        profile = findObject(self.profile_combobox_symbol)
        test.verify(str(profile.selecteditem) == item, "Confirm that the Profile Combo Box has " + item + " selected by default")