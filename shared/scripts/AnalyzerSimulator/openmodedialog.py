# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish

from config import Config

class OpenModeDialog():
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.accession_number_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ".Accession #:_JTextField"
        self.dilution_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Dilution factor: ×_JCheckBox"
        self.dilution_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ".Dilution factor: ×_JTextField"
        self.dilution_checkbox_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Dilution factor: ×_JCheckBox"
        self.undo_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Dilution: 1:_JTextField"
        self.redo_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↪_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.proceed_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Proceed_JButton"
        
    def confirmOpenModeDialogAppears(self,analyzer):
        dialog = squish.findObject(self.object_symbol)
        test.verify(dialog.name == "LayeredDialog-Open Mode - " + analyzer ,"Confirm that the Open Mode Dialog Appears")
    
    def confirmDilution1CheckboxTitle(self):
        checkbox = squish.findObject(self.dilution_checkbox_label_symbol)
        test.log("TODO: This particular x is ascii hex d7 decimal 215, I am leaving it out for now")
        test.verify("Dilution factor: " in checkbox.text ,"Confirm that the checkbox text contains Dilution factor: " + checkbox.text)
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def clickProceedButton(self):
        squish.clickButton(self.proceed_button_symbol)
        
    def clickRedoButton(self):
        squish.clickButton(self.redo_button_symbol)
        
    def clickUndoButton(self):
        squish.clickButton(self.undo_button_symbol)
        
    def clickDilutionCheckBox(self):
        checkbox = findObject(self.dilution_checkbox_symbol)
        checkbox.doClick()
        
    def setAccessionNumberEditBox(self,accession_number):
        text_field = squish.findObject(self.accession_number_textfield_symbol)
        text_field.text = accession_number
        
    def checkDilutionFactorCheckbox(self):
        checkbox = squish.findObject(self.dilution_checkbox_symbol)
        checkbox.doClick()
        
    def setDilutionField(self,amount):
        text_field = squish.findObject(self.dilution_textfield_symbol)
        text_field.text = amount