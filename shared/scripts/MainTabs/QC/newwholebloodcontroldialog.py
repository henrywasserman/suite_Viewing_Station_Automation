# -*- coding: utf-8 -*-
import __builtin__
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from datetime import datetime, date, time, timedelta
from spritecanvas import SpriteCanvas
from config import Config

class NewWholeBloodControlDialog(Controls,SpriteCanvas):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.barcode_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ".Barcode:_JTextField"
        self.run_profile_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.new_button_symbol = ":Bloodhound™ Viewing Station " + version + ".New_JButton_2"
        self.barcode_matches_messagebox_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.barcode_matches_active_control_messagebox_text_symbol = ":Bloodhound™ Viewing Station " + version + ".3 runs_JLabel"
        self.include_retic_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Include retic_JCheckBox"
        

    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def clickNewButton(self):
        squish.clickButton(self.new_button_symbol)
        
    def confirmDialogIsDisplayed(self):
        dialog = squish.findObject(self.object_symbol)
        test.verify("LayeredDialog-New Whole Blood Control" == dialog.name, "Confirm that the current dialog name is LayeredDialog-New Whole Blood Control")
        
    def confirmDialogWasDismissed(self):
        dialog = squish.findObject(self.object_symbol)
        test.verify("null.contentPane" == dialog.name, "Confirm that the current dialog name is null.contentPane which means that it has been dismissed")
        
    def confirmBarcodeFieldIsEmpty(self):
        textfield = squish.findObject(self.barcode_textfield_symbol)
        test.verify('' == textfield.text,"Confirm that the barcode text field is empty")
            
    def confirmComboSelectedItem(self,expected_item):
        combobox = squish.findObject(self.run_profile_combobox_symbol)
        Controls.confirmSelectedItem(self,combobox,expected_item,"Run Profile")
        
    def confirmCancelButtonExists(self):
        button = squish.findObject(self.cancel_button_symbol)
        test.verify("Cancel" == button.text,"Confirm that the Cancel Button exists")
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def confirmIncludeReticCheckbox(self,state):
        Controls.confirmCheckboxState(self,self.include_retic_checkbox_symbol,state,"Include retic")
        
    def confirmNewButtonExists(self):
        button = squish.findObject(self.new_button_symbol)
        test.verify("New" == button.text,"Confirm that the New Button exists")

    def clickBarcodeMatchesActiveControlCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def confirmBarcodeMatchesActiveControlMessageBoxWasDismissed(self):
        messagebox = squish.findObject(self.barcode_matches_messagebox_symbol)
        test.verify("LayeredDialog-New Whole Blood Control" == messagebox.name,"Confirm that the Barcode Matches Active Control Messagebox was dismissed")
        
    def confirmBarcodeMatchesActiveControlMessageBoxText(self,accession_number):
        text_object = squish.findObject(self.barcode_matches_active_control_messagebox_text_symbol)        
        test.verify('Barcode “' + accession_number + '” is an active sample in the In Process tab. Registering this barcode will cause any\nnew runs of that sample to appear as a Whole Blood Control.\nAre you sure you want to continue?' == str(text_object.text),"Confirm message box text: " + str(text_object.text))
