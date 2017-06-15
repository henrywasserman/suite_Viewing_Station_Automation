# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables

class CalibrationTab(Tables):
    
    def __init__(self):
        self.object_symbol = ":Bloodhound 1.Calibration_TabProxy"
        self.calibration_save_table_symbol = ":Calibration.Save_JTable"
        self.calibration_table_symbol = ":Calibration_JTable"
        self.export_button_symbol = ":Calibration_JTable"
        self.print_button_symbol = ":Calibration.Print_JButton"
        self.save_button_symbol = ":Calibration.Save_JButton"
        self.revert_button_symbol = ":Calibration.Revert_JButton"
        self.left_button_symbol = ":Calibration.↩_JButton"
        self.right_button_symbol = ":Calibration.↪_JButton"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def populateLeftTableData(self):
        Tables.populateTableData(self,self.calibration_save_table_symbol)
        
    def populateRightTableData(self):
        Tables.populateTableData(self,self.calibration_table_symbol)
    
    #230. Click to the Calibration sub-subtab and observe that at the left is a table of the current 
    #calibration factors with the Calibration Factor column set to "1" by default for 
    #WBC, RBC, HGB, MCV, PLT, and MPV parameter.
    def confirmDefaultCalibrationFactors(self):
        parameters = ['WBC (10/L)','RBC (10/L)','HGB (g/dL)','MCV (fL)','PLT (10/L)','MPV (fL)']
        self.populateLeftTableData()
        table_data = Tables.getTableData(self)
        
        counter = 0
        for row in table_data:
            test.verify(row['Parameter'] == parameters[counter],"expected parameter: " + parameters[counter] + " actual parameter: " + row['Parameter'])
            test.verify(row['Calibration\nFactor'] == '1.000',"Confirm that by default the calibration factor is set to 1.000") 
            counter += 1
            
    #Observe that there is Save, Revert, Undo and Redo button that are disabled by default unless the calibration factor is changed.    
    def confirmDefaultButtons(self):
        save_button = findObject(self.save_button_symbol)
        revert_button = findObject(self.revert_button_symbol)
        left_button = findObject(self.left_button_symbol)
        right_button = findObject(self.right_button_symbol)
        
        test.verify(save_button.enabled == False,"Confirm that the Save button is disabled by default")
        test.verify(revert_button.enabled == False,"Confirm that the Save button is disabled by default")
        test.verify(left_button.enabled == False,"Confirm that the Save button is disabled by default")
        test.verify(right_button.enabled == False,"Confirm that the Save button is disabled by default")

    #232. Observe that at the right of the Calibration tab is a table showing the history of how these calibration factors have been 
    #updated with the column "Date/Time", "Lot number", "Tech ID", "WBC", "RBC", "HGB", "MCV", "PLT", and "MPV".
    def confirmRightTableHeaders(self):
        headers = ['Date/Time','Lot number','Tech ID','WBC','RBC','HGB','MCV','PLT','MPV']
        self.populateRightTableData()
        table_data = Tables.getTableData(self)
        
        for header in headers:
            test.verify(table_data[0][header],"Confirm that the " + header + " header exists")
            
    def confirmExportAndPrintButton(self):
        export_button = findObject(self.export_button_symbol)
        print_button = findObject(self.print_button_symbol)
        
        test.verify(export_button.enabled == True,"Confirm that the Export Button exists and is enabled")
        test.verify(print_button.enabled == True,"Confirm that the Print Button exists and is enabled")


        
        
        