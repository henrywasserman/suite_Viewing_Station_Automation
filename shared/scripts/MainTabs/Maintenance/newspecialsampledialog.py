# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class NewSpecialSampleDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.barcode_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.profile_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.repeat_count_textfield_symbol = ":Bloodhound™ Viewing Station " + version + ".Repeat Count:_Box"
        self.isolate_sample_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Isolate sample_JCheckBox"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.save_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Save_JButton"
        self.ok_button_symbol = ":Bloodhound™ Viewing Station v1.2.3.OK_JButton"
        
        self.accession_number_types = {}
        self.accession_numbers = []
        
    #Need to update regression test here by adding Custom A, Custom B, Custom C, Custom D and Custom E - Done
    #209. Observe that the complete list of possible profiles will be: Default, DigiCount™, Supravital, Unstained, and Stained.
    def confirmNewSpecialSampleButton(self):
        profile = findObject(self.profile_combobox_symbol)
        
        profiles_items = {'Default':0, 
                          'DigiCount':0, 
                          'Apheresis':0, 
                          'Unstained':0, 
                          'Stained':0, 
                        }
        Controls.confirmListBoxItems(self,profile,profiles_items,"Profile")
        self.clickCancelButton()
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def clickSaveButton(self):
        clickButton(self.save_button_symbol)
        
    def selectProfileItem(self,item):
        Controls.selectComboboxItem(self,self.profile_combobox_symbol,item)
        
    def setAccessionNumber(self,accession_number):
        barcode_textfield = findObject(self.barcode_textfield_symbol)
        barcode_textfield.text = accession_number
        
    def runASampleAndSaveAProfile(self,shared,item,x,y):
        shared.selectBloodhoundViewingStation()
        
        self.selectProfileItem(item)        
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.runSampleInOpenModeAfterClickingOnMaintenanceTab(956,180)
        shared.selectBloodhoundViewingStation()
        self.clickSaveButton()
        squish.clickButton(waitForObject(self.ok_button_symbol))
        shared.spritecanvas.selectAnalyzerSimulator()
        accession_number = shared.spritecanvas.moveObjectAndSetAccessionNumber(253,372,x,y)
        
        if (item == ''):
            self.accession_number_types[accession_number] = 'Default'
        else:
            self.accession_number_types[accession_number] = item
            
        self.accession_numbers.append(accession_number)
        
    def setAccessionNumberType(self,accession_number,type):
        self.accession_number_types[accession_number] = type
        
    def appendAccessionNumber(self,accession_number):
        self.accession_numbers.append(accession_number)