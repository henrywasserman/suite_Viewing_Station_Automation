# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish
import string
import __builtin__

from config import Config

class PatientInformationDialog():
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_5"
        self.check_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Check_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.order_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Special sample with 2 repetitions of the “Prime Stainer” profile._JLabel"        
        
    def clickCheckButton(self):
        squish.clickButton(self.check_button_symbol)
    
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def confirmOrderLabelText(self,text):
        order_label = squish.findObject(self.order_label_symbol)
        test.verify(order_label.text == text, "Confirm that expected text " + text + " is the same as the actual text " + order_label.text)
    