# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class AnalyzerEventsDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.hide_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Hide_JButton_2" 
        self.viewing_station_jpanel = ":Bloodhound™ Viewing Station " + version + "_JPanel"
        self.acknowlege_button = ":Bloodhound™ Viewing Station " + version + ".Acknowledge_JButton"
        
        
    def clickCancelButton(self):
        squish.clickButton(squish.waitForObject(self.cancel_button_symbol))
        
    def clickHideButton(self):
        squish.clickButton(squish.waitForObject(self.hide_button_symbol))
                        
    def dismissAnalyzerEvents(self):
        if (object.exists(self.viewing_station_jpanel)):
            if(object.exists(self.acknowlege_button)):
                squish.clickButton(squish.findObject(self.acknowlege_button))
            if(object.exists(self.hide_button_symbol)):
                squish.clickButton(squish.findObject(self.hide_button_symbol))
        if(object.exists(self.object_symbol)):
            if(object.exists(self.hide_button_symbol)):
                squish.clickButton(squish.findObject(self.hide_button_symbol))