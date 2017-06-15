# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import os
import squishinfo
import squish

from controls import Controls
from config import Config

class InspectCellsDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_4"        
        self.combo_box_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.ok_button_symbol = ":Bloodhound™ Viewing Station " + version + ".OK_JButton"

    def confirmDialogAppears(self):
        snoopze(1.0)
        
    def getTitle(self):
        popup_not_found = True
        counter = 0
        while (popup_not_found):
            if "PopupHandler" in squish.findObject(self.object_symbol).toString():
                popup_not_found = False
            else:
                squish.snooze(1.0)
                counter += 1
                #wait 30 seconds
                if counter == 30:
                    break
        if (popup_not_found):
            title = "could not find popup"
        else:
        
            jpanel = squish.findObject(self.object_symbol)
            popup_handler = jpanel.getComponentAt(0,0)
        
            field = popup_handler.getClass().getDeclaredField("handler")
            field.setAccessible(True)
            handler = field.get(popup_handler)
            test.verify(handler.isPopupVisible() == True,"Confirm that the Inspect Popup is visible")
        
            field = handler.getClass().getDeclaredField("cells")
            field.setAccessible(True)
            cells = field.get(handler)
            title = cells.getTitle()
        
        return title
    
    def confirmTitle(self,expected_title):
        title = self.getTitle()
        test.verify(expected_title == title,"Confirm that the expected title: " + expected_title + " is the same as the current title " + title)
    
    def selectComboboxItem(self,item):
        Controls.selectComboboxItem(self,self.combo_box_symbol, item)

    def clickOKButton(self):
        squish.clickButton(self.ok_button_symbol)

    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
        