# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import os
import squishinfo
import squish

from config import Config

class CreateFolderDialog:
    
    def __init__(self):
        version = Config().version
        self.create_folder_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.name_edit_box_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.name_label_symbol =    ":Bloodhound™ Viewing Station " + version + ".Name:_JLabel"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.create_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Create_JButton"
        
    def getFolderName(self):
        return squish.findObject(name_edit_box_symbol).text
    
    def confirmDefaultFolderName(self):
        name = squish.findObject(self.name_edit_box_symbol)
        test.verify(str(name.text) == "New Folder", "Confirm that the Create Folder Edit Box contains \"New Folder\" by default")
    
    def confirmLabelName(self):
        name = squish.findObject(self.name_label_symbol)
        test.verify(name.text == "Name:","Confirm that the Create Folder Dialog has a Name: label")
        
    def confirmCancelButton(self,status):
        cancel = squish.findObject(self.cancel_button_symbol)
        if status == "enabled":
            test.verify(cancel.enabled == True, "Confirm that the Cancel Button is enabled")
        else:
            test.verify(cancel.enabled == False, "Confirm that the Cancel Button is disabled")
            
    def clickCancelButton(self):
        cancel = squish.findObject(self.cancel_button_symbol)
        squish.clickButton(cancel)
    
    def clickCreateButton(self):
        create = squish.findObject(self.create_button_symbol)
        squish.clickButton(create)
        
    def confirmNewFolderCreated(self,new_folder):
        test.verify(os.path.exists(new_folder) == True,"Confirm that the New Folder has been created")
        test.log("Then delete it.")
        os.rmdir(new_folder)
    
    def confirmCreateButton(self,status):
        create = squish.findObject(self.create_button_symbol)
        if status == "enabled":
            test.verify(create.enabled == True, "Confirm that the Create Button is enabled")
        else:
            test.verify(created.enabled == False,"Confirm that the Create Button is disabled")