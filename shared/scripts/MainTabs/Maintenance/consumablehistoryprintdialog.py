# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class ConsumableHistoryPrintDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.format_combobox_symbol = ":Bloodhound™ Viewing Station " + version + ".Format:_JComboBox"
        self.printer_combobox_symbol = ":Bloodhound™ Viewing Station " + version + ".Printer:_JComboBox"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.print_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Print_JButton"
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def clickPrintButton(self):
        clickButton(self.print_button_symbol)
        
    def selectPrinterItem(self,item):
        Controls.selectComboboxItem(self,self.printer_combobox_symbol, item)