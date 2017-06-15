# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from controls import Controls
from config import Config

class ConfigurationTab(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + ".Configuration_TabProxy"
        self.general_tab_symbol = ":Configuration.General_TabProxy"
        self.users_tab_symbol = ":Configuration.Users_TabProxy"
        self.parameters_tab_symbol = ":Configuration.Parameters_TabProxy"
        self.qc_tab_symbol = ":Configuration.QC_TabProxy"
        self.rules_tab_symbol = ":Configuration.Rules_TabProxy"
        self.analyzers_tab_symbol = ":Configuration.Analyzers_TabProxy"
        self.lis_tab_symbol = ":Configuration.LIS_TabProxy"
    
    def clickTab(self):
        squish.clickTab(self.object_symbol)
        
    def confirmGeneralTabIsSelected(self):
        general_tab = squish.findObject(self.general_tab_symbol)
        test.verify(general_tab.selected == True,"Confirm that the General Tab is selected")
        
    def confirmSubTabs(self):
        general_tab = squish.findObject(self.general_tab_symbol)
        users_tab = squish.findObject(self.users_tab_symbol)
        parameters_tab = squish.findObject(self.parameters_tab_symbol)
        qc_tab = squish.findObject(self.qc_tab_symbol)
        rules_tab = squish.findObject(self.rules_tab_symbol)
        analyzers_tab = squish.findObject(self.analyzers_tab_symbol)
        lis_tab = squish.findObject(self.lis_tab_symbol)
        
        test.verify(general_tab.text == "General","Confirm that the text on the General tab is General")
        test.verify(users_tab.text == "Users", "Confirm that the text on the Users tab is Users")
        test.verify(parameters_tab.text == "Parameters", "Confirm that the text on the Parameters tab is Parameters" )
        test.verify(qc_tab.text == "QC", "Confirm that the text on the QC tab is QC")
        test.verify(rules_tab.text == "Rules", "Confirm that the text on the Rules tab is Rules")
        test.verify(analyzers_tab.text == "Analyzers", "Confirm that the text on the Analyzers tab is Analyzers")
        test.verify(lis_tab.text == "LIS", "Confirm that the the text on the LIS tab is LIS")
        
    def confirmSelectedItem(self,object,expected_item,comment):
        Controls.confirmSelectedItem(self,object,expected_item,comment)
        
    def confirmTableHeaders(self,object_symbol,table_headers):
        Controls.confirmTableHeaders(self,object_symbol,table_headers)
            
    def confirmTableData(self,object_symbol,expected_table_data,comment):
        Controls.confirmTableData(self,object_symbol,expected_table_data,comment)

            
    def confirmListBoxItems(self,control_object,listbox_items,comment):
        Controls.confirmListBoxItems(self,control_object,listbox_items,comment)
