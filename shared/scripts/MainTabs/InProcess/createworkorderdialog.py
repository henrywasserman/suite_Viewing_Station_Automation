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
from controls import Controls

class CreateWorkOrderDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_4"
        self.accession_number_edit_box_symbol = ":Bloodhound™ Viewing Station " + version + ".Accession\nNumber_JTextField"
        self.recognize_sample_by_location_check_box_symbol = ":Bloodhound™ Viewing Station " + version + ".Recognize sample by location_JCheckBox"
        self.analyzer_combo_box_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.mode_combo_box_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox_2"
        self.rack_field_symbol = ":Bloodhound™ Viewing Station " + version + ".Rack:_JTextField"
        self.position_field_symbol = ":Bloodhound™ Viewing Station " + version + ".Position:_JTextField"
        self.save_custom_slides_check_box_symbol = ":Bloodhound™ Viewing Station " + version + ".Special Order:_JCheckBox"
        self.reviewable_field_symbol = ":Bloodhound™ Viewing Station " + version + ".Reviewable:_JTextField"
        self.repeat_count_field_symbol = ""
        self.stained_field_symbol = ":Bloodhound™ Viewing Station " + version + ".Stained:_JTextField"
        self.unstained_field_symbol = ":Bloodhound™ Viewing Station " + version + ".Unstained:_JTextField"
        self.isolate_sample_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Isolate sample_JCheckBox"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.edit_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Edit_JButton"
        self.save_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Save_JButton"
        self.undo_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↩_JButton"
        self.redo_button_symbol = ":Bloodhound™ Viewing Station " + version + ".↪_JButton"
        self.stained_normal_radio_button = ":Bloodhound™ Viewing Station v1.2.3.Normal_JRadioButton"
        self.stained_retic_radio_button = ":Bloodhound™ Viewing Station v1.2.3.Retic_JRadioButton"
        self.stained_paired_radio_button = ":Bloodhound™ Viewing Station v1.2.3.Paired_JRadioButton"
        self.unstained_normal_radio_button = ":Bloodhound™ Viewing Station v1.2.3.Normal_JRadioButton_2"
        self.unstained_retic_radio_button = ":Bloodhound™ Viewing Station v1.2.3.Retic_JRadioButton_2"
        self.unstained_paired_radio_button = ":Bloodhound™ Viewing Station v1.2.3.Paired_JRadioButton_2"

    def confirmStainedNormalRadioButton(self,enable, state):    
        Controls.confirmRadioButton(self,self.stained_normal_radio_button, enable, state,"Stained Normal")
        
    def confirmStainedReticRadioButton(self,enable, state):    
        Controls.confirmRadioButton(self,self.stained_retic_radio_button,enable, state,"Stained Retic")

    def confirmStainedPairedRadioButton(self, enable, state):
        Controls.confirmRadioButton(self,self.stained_paired_radio_button,enable, state,"Stained Paired")

    def confirmUnStainedNormalRadioButton(self,enable, state):
        Controls.confirmRadioButton(self,self.unstained_normal_radio_button,enable, state,"UnStained Normal")
        
    def confirmUnStainedReticRadioButton(self,enable, state):
        Controls.confirmRadioButton(self,self.unstained_retic_radio_button,enable, state,"UnStained Retic")

    def confirmUnStainedPairedRadioButton(self,enable, state):
        Controls.confirmRadioButton(self,self.unstained_paired_radio_button,enable, state,"UnStained Paired")
        
    def confirmAccessionNumberEditBox(self,status,data):
        self.confirmEditBox(self.accession_number_edit_box_symbol,status,"Accession Number Edit Box",data)
        
    def setAccessionNumberEditBox(self,accession_number):
        edit_box = squish.findObject(self.accession_number_edit_box_symbol)
        edit_box.text = accession_number
        
    def typeIntoAccessionNumberEditBox(self,accession_number):
        edit_box = squish.findObject(self.accession_number_edit_box_symbol)
        squish.mouseClick(edit_box, 19, 15, 0, squish.Button.Button1)
        squish.type(edit_box, accession_number)

    def deleteAccessionNumberAndEnterNewOne(self,accession_number):
        edit_box = squish.findObject(self.accession_number_edit_box_symbol)
        squish.mouseClick(edit_box, 39, 16, 0, squish.Button.Button1)
        squish.doubleClick(edit_box, 39, 16, 0, squish.Button.Button1)
        squish.type(edit_box, "<Backspace>")
        squish.type(edit_box, accession_number)

    def confirmRecognizeSampleByLocationCheckbox(self,status,state):
        self.confirmCheckBox(self.recognize_sample_by_location_check_box_symbol,status,"Recognize Sample By Location",state)
        
    def clickRecognizeSampleByLocationChecbox(self):
        Controls.clickCheckbox(self,self.recognize_sample_by_location_check_box_symbol)
    
    def confirmAnalyzerComboBox(self,status,items):
        self.confirmComboBox(self.analyzer_combo_box_symbol,status, "Analyzer", items)
    
    def confirmModeComboBox(self,status,items):
        self.confirmComboBox(self.mode_combo_box_symbol,status, "Mode", items)
    
    def confirmRackField(self,status,contents):
        self.confirmField(self.rack_field_symbol,status, "Rack", contents)
    
    def confirmPositionField(self,status,contents):
        self.confirmField(self.position_field_symbol,status, "Position", contents)
        
    def setPositionField(self,position):
        position_field = squish.findObject(self.position_field_symbol)
        position_field.text = position
    
    def confirmSaveCustomSlidesCheckbox(self,status,state):
        self.confirmCheckBox(self.save_custom_slides_check_box_symbol, status, "Save Custom Slides", state)
                
    def checkSaveCustonSlidesCheckbox(self):
        check_box = squish.findObject(self.save_custom_slides_check_box_symbol)
        if (check_box.selected == False):
             squish.mouseClick(check_box, 15, 12, 0, squish.Button.Button1)
    
    def confirmReviewableField(self,status,contents):
        self.confirmField(self.reviewable_field_symbol,status, "Reviewable",contents)
        
    def setReviewableField(self,reviewable_number):
        text_field = squish.findObject(self.reviewable_field_symbol)
        text_field.text = reviewable_number
    
    def confirmStainedField(self,status,contents):
        self.confirmField(self.stained_field_symbol,status, "Stained",contents)
    
    def confirmUnStainedField(self,status,contents):
        self.confirmField(self.unstained_field_symbol,status,"Unstained",contents)
    
    def confirmIsolateSampleCheckbox(self,status,state):
        self.confirmCheckBox(self.isolate_sample_checkbox_symbol,status,"Isolate Sample", state)
        
    def clickIsolateSampleCheckbox(self):
        checkbox = squish.findObject(self.isolate_sample_checkbox_symbol)
        checkbox.doClick()
                    
    def confirmUndoButton(self,status):
        self.confirmButton(self.undo_button_symbol,status,"Undo")
    
    def confirmRedoButton(self,status):
        self.confirmButton(self.redo_button_symbol,status,"Redo")
    
    def confirmCancelButton(self,status):
        self.confirmButton(self.cancel_button_symbol,status,"Cancel")
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
    
    def confirmEditButton(self,status):
        self.confirmButton(self.edit_button_symbol,status,"Edit")
    
    def confirmSaveButton(self,status):
        self.confirmButton(self.save_button_symbol,status,"Save")
        
    def clickSaveButton(self):
        squish.clickButton(self.save_button_symbol)
        
    def confirmEditBox(self,object_symbol,status,name,data = ''):
        edit_box = squish.findObject(object_symbol)
        
        if status == "enabled":
            test.verify(edit_box.enabled == True, "Confirm that the " + name + " is enabled")
        else:
            test.verify(edit_box.enabled == False,"Confirm that the " + name + " is disabled")
    
        test.verify(edit_box.text == data,"Confirm that the " + name + " contains " + data)
    
    def confirmCheckBox(self,object_symbol,status,name,state):
        check_box = squish.findObject(object_symbol)
        
        if status == "enabled":
            test.verify(check_box.enabled == True, "Confirm that the " + name + " checkbox is enabled")
        else:
            test.verify(check_box.enabled == False,"Confirm that the " + name + " checkbox is disabled")
            
        if state == "checked":
            test.verify(check_box.selected == True, "Confirm that the " + name + " checkbox is checked")
        else:
            test.verify(check_box.selected == False, "Confirm that the " + name + " checkbox is unchecked")
            
    
    def confirmComboBox(self,object_symbol,status,name, items):
        combo_box = squish.findObject(object_symbol)
        
        if status == "enabled":
            test.verify(combo_box.enabled == True, "Confirm that the " + name + " combobox is enabled")
        else:
            test.verify(combo_box.enabled == False, "Confirm that the " + name + " combobox is disabled")
            
        item_array = items.split(",")
        index = 0
        for item in item_array:
            test.verify(str(combo_box.getItemAt(index)) == item, "Confirm that the " + name + " combox_box contains " + item)
            index += 1
    
    def confirmField(self,object_symbol,status,name,contents=''):
        field = squish.findObject(object_symbol)
        
        if status == "editable":
            test.verify(field.editable == True,"Confirm that the " + name + " field is editable")
        else:
            test.verify(field.editable == False, "Confirm that the " + name + " field is not-editable")
            
        test.verify(field.text == contents, "Confirm that the " + name + " field contains " + contents)
        
    def confirmButton(self,object_symbol,status,name):
        button = squish.findObject(object_symbol)
        
        if status == "enabled":
            test.verify(button.enabled == True,"Confirm that the " + name + " Button is enabled")
        else:
            test.verify(button.enabled == False, "Confirm that the " + name + " Button is disabled")
            
