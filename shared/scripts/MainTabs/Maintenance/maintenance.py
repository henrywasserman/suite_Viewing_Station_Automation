# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from datetime import datetime
from tables import Tables
from config import Config

class Maintenance(Tables):
        
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + ".Maintenance_TabProxy"
        self.new_special_sample_button_symbol = ":Maintenance.New Special Sample..._JButton"
        self.run_maintenance_action_button_symbol = ":Maintenance.Run Maintenance Action..._JButton"
        self.close_special_sample_button_symbol = ":Maintenance.Close Special Sample..._JButton"
        self.bootstrap_population_means_button_symbol = ":Maintenance.Bootstrap Population Means_JButton"

        self.newspecialsampledialog = NewSpecialSampleDialog()
        self.closespecialsampledialog = CloseSpecialSampleDialog()
        self.runmaintenanceactiondialog = RunMaintenanceActionDialog()
        self.bootstrappopulationmeansdialog = BootstrapPopulationMeansDialog()
        
        self.calibrationtab = CalibrationTab()
        self.calibrationrunstab = CalibrationRunsTab()
        self.consumablehistorytab = ConsumableHistoryTab()
        self.eventlogstab = EventLogsTab()
        self.usagehistorytab = UsageHistoryTab()
        self.consumablehistoryprintdialog = ConsumableHistoryPrintDialog()
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def clickNewSpecialSampleButton(self):
        clickButton(self.new_special_sample_button_symbol)
        
    def clickCloseSpecialSampleButton(self):
        clickButton(self.close_special_sample_button_symbol)
        
    def clickRunMaintenanceActionButton(self):
        clickButton(self.run_maintenance_action_button_symbol)
        
    def clickBootstrapPopulationMeansButton(self):
        clickButton(self.bootstrap_population_means_button_symbol)