# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class CleaningSolutionDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.run_now_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Run Now_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.replace_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Replace_JButton"

    def clickReplaceButton(self):
        clickButton(self.replace_button_symbol)