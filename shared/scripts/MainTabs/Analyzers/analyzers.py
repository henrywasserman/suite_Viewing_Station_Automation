# -*- coding: utf-8 -*-
import ast
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

class Analyzers():
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + ".Analyzers_TabProxy"
        self.consumable_volumes_symbol = ":Analyzers_JPanel_2"
        self.sample_image_symbol =  ":Analyzers_JLabel"
        self.sample_image2_symbol = ":Analyzers_JLabel_2"
        self.cleaning_solution_button_symbol = ":Analyzers.Cleaning Solution_JButton"
        
        self.images = Images()
        self.cleaningsolutiondialog = CleaningSolutionDialog()
        self.analyzereventsdialog = AnalyzerEventsDialog()
        self.consumablewastemanagementdialog = ConsumableWasteManagementDialog()
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def getConsumableVolumesData(self,label):
        data = ""
        consumable_volumes = findObject(self.consumable_volumes_symbol)
        for index in range(consumable_volumes.getComponentCount()):
            if label in consumable_volumes.getComponent(index).toString():
                data = consumable_volumes.getComponent(index - 1).text
                break
        
        return data
    
    def waitForSampleImageToChange(self):
        result = self.images.waitForImageToChange("sample_image.png", self.sample_image_symbol, self.sample_image2_symbol)
        return result
    
    def clickCleaningSolutionButton(self):
        clickButton(self.cleaning_solution_button_symbol)
        