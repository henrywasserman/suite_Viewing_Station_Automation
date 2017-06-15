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

class NewReproducibilityTestDialog(Controls,SpriteCanvas):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.analyzer_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.barcode_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ".Barcode:_JTextField"
        self.repeat_count_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField_2"
        self.isolate_sample_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Isolate sample_JCheckBox"
        self.runprofile_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.new_button_symbol = ":Bloodhound™ Viewing Station " + version + ".New_JButton_2"
        self.barcode_matches_active_control_ok_button_symbol = ":Bloodhound™ Viewing Station " + version + ".OK_JButton"
        self.barcode_matches_active_control_messagebox_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.barcode_matches_active_control_messagebox_text_symbol = ":Bloodhound™ Viewing Station " + version + ".3 runs_JLabel"
        self.include_retic_slide_checkbox_symbol = ":Bloodhound™ Viewing Station v1.2.3.Include retic slide_JCheckBox"
        self.barcode_textfield_symbol = ":Bloodhound™ Viewing Station v1.2.3.Barcode:_JTextField"
        self.barcode_matches_active_control_ok_button_symbol = ":Bloodhound™ Viewing Station v1.2.3.OK_JButton"
        
    def clickNewButton(self):
        squish.clickButton(self.new_button_symbol)
        
    def setBarcodeTextField(self,text):
        text_field = squish.findObject(self.barcode_textfield_symbol)
        text_field.text = text
        
    def clickBarcodeMatchesActiveControlOKButton(self):
        squish.buttonClick(squish.waitForObject(self.barcode_matches_active_control_ok_button_symbol))

    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def confirmDialogAppears(self):
        dialog = squish.findObject(self.object_symbol)
        test.verify("LayeredDialog-New Reproducibility Test" == dialog.name, "Confirm that the dialog with the name LayeredDialog-New Reproducibility Test appears " + dialog.name)
        
    def confirmDialogCloses(self):
        dialog = squish.findObject(self.object_symbol)
        test.verify('null.contentPane' == dialog.name, "Confirm that the New Reproducibility Test Dialog Box has closed")
        
    def confirmAnalyzerField(self):
        textfield = squish.findObject(self.analyzer_textfield_symbol)
        test.verify("Bloodhound 1" == textfield.text, "Confirm that Bloodhound 1 appears in the text field: " + textfield.text)

        self.object_symbol
        self.analyzer_textfield_symbol
                
    def confirmBarcodeFieldIsEmpty(self):
        textfield = squish.findObject(self.barcode_textfield_symbol)
        test.verify("" == textfield.text, "Confirm that the Barcode textfield is empty: " + textfield.text)
        
    def confirmRepeatCountField(self,count):
        textfield = squish.findObject(self.repeat_count_textfield_symbol)
        test.verify(str(count) == textfield.text,"Confirm that the expected textfield number " + str(count) + " is equal to the actual text field number " + textfield.text)
        
    def setRepeatCountField(self,text):
        textfield = squish.findObject(self.repeat_count_textfield_symbol)
        textfield.text = text
        
    def confirmIsolateSampleCheckBox(self,state):
        checkbox = squish.findObject(self.isolate_sample_checkbox_symbol)
        test.verify(checkbox.selected == True, "Confirm that the IsolateSampleCheckBox is selected")
        
    def confirmRunProfileComboBox(self,item):
        combobox = squish.findObject(self.runprofile_combobox_symbol)
        test.verify(item == str(combobox.getSelectedItem()), "Confirm that the expected item " + item + " is equal to the actual combobox item " + str(combobox.getSelectedItem()))
        squish.snooze(1.0)
        
    def confirmCancelAndNewButtonsExist(self):
        cancel_button = squish.findObject(self.cancel_button_symbol)
        new_button = squish.findObject(self.new_button_symbol) 
        test.verify("Cancel" == str(cancel_button.getText()), "Confirm that the cancel button exists")
        test.verify("New" == str(new_button.getText()), "Confirm that the new button exists")
        
    def clickBarcodeMatchesActiveControlOKButton(self):
        squish.clickButton(squish.waitForObject(self.barcode_matches_active_control_ok_button_symbol))
        
    def confirmBarcodeMatchesActiveControlMessageBoxText(self,accession_number):
        messagebox = squish.findObject(self.barcode_matches_active_control_messagebox_symbol)
        text_object = squish.findObject(self.barcode_matches_active_control_messagebox_text_symbol)
        
        test.verify("LayeredDialog-Barcode Matches Active Control" == messagebox.name, "Confirm that the Barcode Matches Active Control Message Box appears.")
        test.verify('Barcode “' + accession_number + '” is an active sample in the In Process tab. Registering this barcode will cause any\nnew runs of that sample to appear as a Reproducibility test.\nAre you sure you want to continue?' == str(text_object.text))
        
        return messagebox
    
    def confirmBarcodeMatchesActiveControlMessageBoxCloses(self):
        messagebox = squish.findObject(self.barcode_matches_active_control_messagebox_symbol)
        test.verify('null.contentPane' == messagebox.name, "Confirm that the Barcode Matches Active Control Message Box is dismissed.")
        
        
    def confirmIncludeReticSlideCheckbox(self,state,description):
        Controls.confirmCheckboxState(self,self.include_retic_slide_checkbox_symbol,state,description)
        
        
        
