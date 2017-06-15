# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables

class CalibrationRunsTab(Tables):
    
    def __init__(self):
        self.object_symbol = ":Bloodhound 1.Calibration Runs_TabProxy"
        self.print_button_symbol = ":Calibration Runs.Print_JButton"
        self.export_button_symbol = ":Calibration Runs.Export_JButton"
        self.set_up_run_button_symbol = ":Calibration Runs.Set up run..._JButton"
        self.apply_and_close_button_symbol = ":Calibration Runs.Apply and close_JButton"
        self.discard_button_symbol = ":Calibration Runs.Discard_JButton"
        self.exclude_button_symbol = ":Calibration Runs.Exclude_JButton"
        self.blank_combobox_symbol = ":Calibration Runs_JComboBox"
        self.table_symbol = ":Calibration Runs.Print_QCTable_2"
        self.table_header_symbol = ":Calibration Runs.Print_JTableHeader"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    #234. Click to the Calibration Runs sub-subtab and observe a combobox appears at the top left of the page listing the 
    #barcode and date of every calibrator run on this Analyzer, including the active run if there is one.
    #Note: If there is no run, the combobox is grayed out.        
    def confirmBlankComboBoxIsDisabled(self):
        blank_combobox = findObject(self.blank_combobox_symbol)
        test.verify(str(blank_combobox.selecteditem) == '<null>', "Confirm that the blank combo box exists and does not contain a selected item")
        
    def confirmPrintAndExportButtons(self):
        print_button = findObject(self.print_button_symbol)
        export_button = findObject(self.export_button_symbol)
        
        test.verify(print_button.enabled == True, "Confirm that the Print button exists and is enabled by default")
        test.verify(export_button.enabled == True, "Confirm that the Export button exists and is enabled by default")
        
    #236. Observe that there are buttons labeled “Apply and close” and “Discard” on the right side of the Calibration 
    #Runs sub-subtab, which are disabled if there are no calibrator run.
    def confirmDefaultButtonsOnTheRightSide(self):
        apply_and_close_button = findObject(self.apply_and_close_button_symbol)
        discard_button = findObject(self.discard_button_symbol)
        
        test.verify(apply_and_close_button.enabled == False,"Confirm that the apply and close button is disabled by default")
        test.verify(discard_button.enabled == False, "Confirm that the discard button is disabled by default")

    def confirmDefaultSetupRunAndExludeButtons(self):
        set_up_run_button = findObject(self.set_up_run_button_symbol)
        exclude_button = findObject(self.exclude_button_symbol)
        
        test.verify(set_up_run_button.enabled == True, "Confirm that the Set up run... button exists and is enabled by default")
        test.verify(exclude_button.enabled == False, "Confirm that the Exclude button exists and is disabled by default")
        
    def confirmDefaultRunTable(self):
        parameters = ['WBC','RBC','HGB','MCV','PLT','MPV']
        
        Tables.populateTableData(self, self.table_symbol)
        table_data = Tables.getTableData(self)
        
        counter = 0
        for row in table_data:
            test.verify(row['Parameter'] == parameters[counter],"Verify that we are looking at the expected parameter: " + parameters[counter]) 
            counter += 1        