# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import re
import sys

from controls import Controls
from config import Config

class DigiCountExcludeDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.cancel_button_object = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton" 
        self.save_button_object = ":Bloodhound™ Viewing Station " + version + ".Save_JButton"
        self.right_button_object = ":Bloodhound™ Viewing Station " + version + ".↪_JButton"
        self.left_button_object = ":Bloodhound™ Viewing Station " + version + ".↩_JButton"
        self.exclude_checkbox_object = ":Result.Exclude Result_JCheckBox"
        self.comment_textbox_object = ":Result_PlaceholderOverlay" 
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_object)
        
    def clickSaveButton(self):
        squish.clickButton(self.save_button_object)
        
    def enterComment(self,text):
        comment = squish.findObject(self.comment_textbox_object)
        comment.parent.setText(text)
        
    def clickCheckbox(self):
        Controls.clickCheckbox(self,self.exclude_checkbox_object)