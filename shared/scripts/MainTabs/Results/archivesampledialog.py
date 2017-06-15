# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import os
import squishinfo
import squish

from config import Config

class ArchiveSampleDialog:
    
    def __init__(self):
        
        version = Config().version
        
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.username_symbol = ":Bloodhound™ Viewing Station " + version + ".Username:_JTextField"
        self.password_symbol = ":Bloodhound™ Viewing Station " + version + ".Password:_JPasswordField"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.archive_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Archive_JButton"

    def setUsername(self,username_text):
        squish.type(squish.waitForObject(self.username_symbol), username_text)
        
    def setPassword(self,password_text):
        squish.mouseClick(squish.waitForObject(self.password_symbol), 68, 14, 0, squish.Button.Button1)
        squish.type(squish.waitForObject(self.password_symbol), password_text)
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def clickArchiveButton(self):
        squish.clickButton(squish.waitForObject(self.archive_button_symbol))