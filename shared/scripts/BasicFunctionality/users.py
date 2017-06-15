# -*- coding: utf-8 -*-
import test
import testData
import objectMap
import object
import squishinfo
import squish

from config import Config

class Users:

    def __init__(self, username="Vadim",password="and1lead"):
        version = Config().version
        self.username = username
        self.password = password
        self.username_edit_box_symbol = ":Bloodhound™ Viewing Station " + version + ".Username:_JTextField"
        self.password_edit_box_symbol = ":Bloodhound™ Viewing Station " + version + ".Password:_JPasswordField"
        self.logout_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Log Out_JButton"
        self.login_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Log In_JButton"
        self.bloodhound_window_symbol = ":Bloodhound™ Viewing Station " + version + "_JTabbedPane"
        self.ok_button_symbol = ":Bloodhound™ Viewing Station " + version + ".OK_JButton"
        
    def login(self):
        if object.exists(self.login_button_symbol):
            clickButton(waitForObject(self.login_button_symbol))
            self.enterUsernamePassword()
            
    def selectBloodhoundViewingStation(self):
        waitForObject(self.bloodhound_window_symbol).getTopLevelAncestor().toFront()
        
    def enterUsernamePassword(self):
        type(waitForObject(self.username_edit_box_symbol), self.username)
        mouseClick(waitForObject(self.password_edit_box_symbol), 68, 14, 0, Button.Button1)
        type(waitForObject(self.password_edit_box_symbol), self.password)
        clickButton(waitForObject(self.ok_button_symbol))
        
    def logout(self):
        clickButton(self.logout_button_symbol)

        