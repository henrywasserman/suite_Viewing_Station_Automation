# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls

class ConsumableWasteManagementDialog(Controls):
    
    def __init__(self):
        self.object_symbol = ":Analyzers_JPanel"
        self.revert_item_button_symbol = ":Analyzers.Revert Item_JButton"
        self.replace_item_button_symbol = ":Analyzers.Replace Item_JButton"
        self.ok_button_symbol = ":Analyzers.OK_JButton"
        self.table_symbol = ":Analyzers.(Drawer open on Bloodhound 1)_JTable"
        
    def clickRevertItemButton(self):
        clickButton(self.revert_item_button_symbol)
        
    def clickReplaceItemButton(self):
        clickButton(self.replace_item_button_symbol)
        
    def clickOKButton(self):
        clickButton(self.ok_button_symbol)
        
    def confirmConsumableWasteManagementDialogExists(self):
        consumable_waste_management_dialog = waitForObject(self.object_symbol)
        test.verify(consumable_waste_management_dialog.name == "LayeredDialog-Consumable/Waste Management", "Confirm that the Consumable Waste Management Dialog exists")
        
    def confirmBackgroundColorIsRed(self,cell_value):
        table = findObject(self.table_symbol)
        Tables.populateTableData(self,self.table_symbol)
        Tables.clickOnTableRowByName(self, self.table_symbol, "Name", cell_value)
        cell_renderer = table.getCellRenderer(0,0)
        base_renderer = cell_renderer.getBaseRenderer(table)
        test.log(base_renderer.text)
        color = base_renderer.background
        test.log(str(color))
        #Tables.doubleClickOnTableRowByName(self, self.table_symbol, "Name", cell_value)
        #See this website to view java color mapping
        #http://www.ringthis.com/java/colortest/
        #You will have to be able to load the applet
        test.verify(str(color) == "java.awt.Color[r=177,g=88,b=88]","Confirm that the color of the selected cell " + str(color) + " is equal to the expected string java.awt.Color[r=177,g=88,b=88]")
        snooze(1.0)
