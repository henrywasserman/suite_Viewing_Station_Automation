# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from controls import Controls

class ParamtersTab(Controls):
    
    def __init__(self):
        self.object_symbol = ":Parameters_JTable"
        self.table_object_symbol = ":Parameters_JTable"
        self.tab_symbol = ":Configuration.Parameters_TabProxy"
        self.cancel_button_symbol = ":Parameters.Cancel_JButton"
        
    def clickTab(self):
        clickTab(waitForObject(self.tab_symbol))
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def doubleClickRow(self,index):
        Tables.populateTableData(self,self.table_object_symbol)
        Tables.doubleClickOnTableRow(self,index)
        
    def populateTableData(self):
        table_data = Tables.populateTableData(self,self.table_object_symbol)
        return table_data
        
