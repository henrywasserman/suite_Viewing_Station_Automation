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

class ActivateEditDigicountControlDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.table_object_symbol = ":Bloodhound™ Viewing Station " + version + "_JViewport"
        self.active_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Active_JCheckBox"
        self.copy1_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Copy_JButton"
        self.copy2_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Copy_JButton_2"
        self.clear1_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Clear_JButton"
        self.clear2_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Clear_JButton_2"
        self.copy3_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Copy_JButton_3"
        self.left_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↩_JButton"
        self.right_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↪_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.save_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Save_JButton"
        
        #For now Assuming this label will start with a capital C (C*)
        self.lot_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Lot_JLabel"
        self.level_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Low_JLabel"
        self.analyzer_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Bloodhound 1_JLabel"
        self.expires_label_symbol = ":Bloodhound™ Viewing Station " + version + ".3/5/14 6:26 AM_JLabel"
        self.usage_label_symbol = ":Bloodhound™ Viewing Station " + version + ".3 runs_JLabel"
        self.startdate_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Start:_JLabel_2"
        self.enddate_label_symbol = ":Bloodhound™ Viewing Station " + version + ".End:_JLabel_2"
        
        self.activated_label_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextArea"
        self.dialog_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2" 
        
    def checkActiveCheckBox(self):
        checkbox = findObject(self.active_checkbox_symbol)
        if checkbox.selected == False:
            checkbox.doClick()
            
    def confirmActiveCheckBox(self,state):
        checkbox = findObject(self.active_checkbox_symbol)
        if state.lower() == "checked":
            test.verify(checkbox.selected == True,"Confirm that the Active Check Box is selected")
        else:
            test.verify(checkbox.selected == False, "Confirm that the Active Check Box is not selected")
            
    def confirmWillBeActivatedMessage(self):
        label = findObject(self.activated_label_symbol)
        test.verify(label.text == "This lot will be activated","Confirm that the label text is 'This lot will be activated'")
        
    def confirmUsageText(self,text):
        label = findObject(self.usage_label_symbol)
        test.verify(label.text == text, "Confirm that the expected usage text: " + text + " is equal to the actual usage text: " + label.text)
        
    def confirmStartDateExists(self):
        label = findObject(self.startdate_label_symbol)
        test.verify(label.text == '',"TODO: Start date does not exist this is currently an open bug.  Waiting for Jeff to enter this in and send me the Mantis number")

    def confirmEndDateDoesNotExist(self):
        label = findObject(self.enddate_label_symbol)
        test.verify(label.text == '',"Confirm that the end date does not exist")

    def clickCopy1Button(self):
        clickButton(self.copy1_button_symbol)
        
    def clickCopy2Button(self):
        clickButton(self.copy2_button_symbol)
        
    def clickClear1Button(self):
        clickButton(self.clear1_button_symbol)
        
    def clickClear2Button(self):
        clickButton(self.clear2_button_symbol)
        
    def clickCopy3Button(self):
        clickButton(self.copy3_button_symbol)
        
    def clickLeftButton(self):
        clickButton(self.left_button_symbol)
        
    def clickRightButton(self):
        clickButton(self.right_button_symbol)
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
    
    def clickSaveButton(self):
        clickButton(self.save_button_symbol)
        
    def populateTableData(self):
        Tables.populateTableData(self,self.table_object_symbol)
        
    def confirmDialogClosed(self):
        dialog = findObject(self.dialog_symbol)
        test.verify("null.contentPane"  == dialog.name,"Confirm that the dialog name is null.contentPane, meaning that the dialog has closed.")
        
    def confirmDialogOpens(self):
        dialog = findObject(self.dialog_symbol)
        test.verify("LayeredDialog-Activate/Edit DigiCount™ Control"  == dialog.name,"Confirm that the dialog name is LayeredDialog-Activate/Edit DigiCount™ Control, meaning that the dialog has opened.")
        
        