# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish

from configurationtab import ConfigurationTab

class ConfigurationQCTab(ConfigurationTab):
    
    def __init__(self):
        self.object_symbol = ":Configuration.QC_TabProxy"
        
    def clickTab(self):
            squish.clickTab(self.object_symbol)