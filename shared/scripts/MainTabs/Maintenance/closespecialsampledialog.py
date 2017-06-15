# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class CloseSpecialSampleDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.barcode_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.close_sample_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Close Sample_JButton"
        
    def clickBarcodeComboBox(self):
        mouseClick(self.barcode_combobox_symbol)
        
    def clickCloseSampleButton(self):
        clickButton(self.close_sample_button_symbol)
        
    def selectComboBoxItem(self,item):
        Controls.selectComboboxItem(self,self.barcode_combobox_symbol,item)
        
    def confirmItemDoesNotExist(self,item):
        exists = Controls.selectComboboxItem(self,self.barcode_combobox_symbol,item)
        test.verify(exists == False, "Confirm that the item: " + item + " does not exist in the Barcode Combobox")