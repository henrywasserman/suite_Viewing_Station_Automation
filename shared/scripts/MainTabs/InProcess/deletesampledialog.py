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

class DeleteSampleDialog():
    
    def __init__(self):
        version = Config().version
        self.username_symbol = ":Bloodhound™ Viewing Station " + version + ".Username:_JTextField"
        self.password_symbol = ":Bloodhound™ Viewing Station " + version + ".Password:_JPasswordField"
        self.delete_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Delete_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        
    def enterUsername(self,username):
        squish.findObject(self.username_symbol).setText(username)
        
    def enterPassword(self,password):
        squish.findObject(self.password_symbol).setText(password)
        
    def clickDeleteButton(self):
        squish.clickButton(self.delete_button_symbol)
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def confirmDialogIsNoLongerDisplayed(self):
        dialog = squish.findObject(self.object_symbol)
        test.verify('null.contentPane' == dialog.name, "Confirm that the dialog name is now null.contentPane which means that the dialog has been dismissed.")
        