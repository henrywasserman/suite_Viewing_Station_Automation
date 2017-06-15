# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import re

from controls import Controls
from config import Config

class ExcludeDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JComponent"
        self.cancel_button_object = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.save_button_object = ":Bloodhound™ Viewing Station " + version + ".Save_JButton"
        self.left_button_object = ":Bloodhound™ Viewing Station " + version + ".↩_JButton"
        self.right_button_object = ":Bloodhound™ Viewing Station " + version + ".↪_JButton"
        self.exclude_checkbox_object = ":Result.Exclude Result_JCheckBox"
        self.exclude_population_checkbox_object = ":Bloodhound™ Viewing Station " + version + ".Exclude Population Batch_JCheckBox"
        self.comment_textbox_object = ":Result_PlaceholderOverlay"
        self.comment_population_textbox_object = ":Bloodhound™ Viewing Station " + version + "_PlaceholderOverlay"
        self.excluded_population_comment_textbox_object = ":Bloodhound™ Viewing Station " + version + ".Ilvolvsky, Vadim_JTextArea"
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_object)
        
    def clickSaveButton(self):
        squish.clickButton(self.save_button_object)
        
    def confirmDialogAppears(self):
        dialog = squish.findObject(self.object_symbol)
        #Verify that we have a JPanel
        test.verify("class javax.swing.JPanel" == dialog.getClass().toString(),"Confirm that the dialog box exists: class javax.swing.JPanel")
        
    def confirmDialogIsDismissed(self):
        dialog = squish.findObject(self.object_symbol)
        #Verify that we have a JPanel has been dismissed
        test.verify("class javax.swing.JTabbedPane" == dialog.getClass().toString(),"Confirm that the dialog box does not exist: class javax.swing.JTabbedPane")

    def clickExcludeResultCheckbox(self):
        checkbox = squish.findObject(self.exclude_checkbox_object)
        checkbox.doClick()
        
    def clickExcludePopulationBatchCheckbox(self):
        checkbox = squish.findObject(self.exclude_population_checkbox_object)
        checkbox.doClick()
        
    def enterCommentText(self,text):
        textbox = squish.findObject(self.comment_textbox_object)
        textbox.parent.setText(text)
        
    def enterPopulationCommentText(self,text):
        textbox = squish.findObject(self.comment_population_textbox_object)
        textbox.parent.setText(text)
        
    def confirmPopulationExcludeDialogStatus(self):
        test.verify(squish.findObject(self.save_button_object).enabled == False,"Confirm that Exclude Dialog Save button is disabled")
        test.verify(squish.findObject(self.excluded_population_comment_textbox_object).editable == False,"Confirm that the Comment is not editable")
        self.clickCancelButton()

        