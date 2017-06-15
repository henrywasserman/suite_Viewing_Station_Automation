# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables
from config import Config

class ReleaseActionDialog(Tables):
    
    def __init__(self):
        version = Config().version
        self.release_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Release_JButton" 
        self.release_button2_symbol = ":Bloodhound™ Viewing Station " + version + ".Release_JButton_2"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.diff_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".Diff_JCheckBox"
        self.cbc_checkbox_symbol = ":Bloodhound™ Viewing Station " + version + ".CBC_JCheckBox"
        self.bloodhound_table_symbol = ":Bloodhound™ Viewing Station " + version + "_JTable"
        
        super(ReleaseActionDialog, self).__init__()
        
                        #Parameter:          CheckBox    Enabled
        self.EXPECTED_RESULTS = {
                         #CBC expected Results
                         'WBC (×10³/μL)'      :['true', 0],
                         'RBC (×10⁶/μL)'      :['true', 0],
                         'HGB (g/dL)'         :['true', 0],
                         'HCT (%)'            :['true', 0],
                         'MCV (fL)'           :['true', 0],
                         'MCH (pg)'           :['true', 0],
                         'MCHC (g/dL)'        :['true', 0],
                         'RDW (%)'            :['true', 0],
                         'RDW-SD (fL)'        :['true', 0],
                         'PLT (×10³/μL)'      :['true', 0],
                         'MPV (fL)'           :['true', 0],
                         '%NRBC (/100WBC)'    :['true', 0],
                         '#NRBC (×10³/μL)'    :['true', 0],
                         #Diff expected Results 
                         '%NEUT (%)'         :['false', 1],
                         '%LYMPH (%)'        :['false', 1],
                         '%MONO (%)'         :['false', 1],
                         '%EO (%)'           :['false', 1],
                         '%BASO (%)'         :['false', 1],
                         '%UNCLASS (%)'      :['false', 1],
                         '#NEUT (×10³/μL)'   :['false', 1],
                         '#LYMPH (×10³/μL)'  :['false', 1],
                         '#MONO (×10³/μL)'   :['false', 1],
                         '#EO (×10³/μL)'     :['false', 1],
                         '#BASO (×10³/μL)'   :['false', 1],
                         '#UNCLASS (×10³/μL)':['false', 1]
        }
        
        self.cbc_parameters = [                         
                               'WBC (×10³/μL)',
                               'RBC (×10⁶/μL)',
                               'HGB (g/dL)',
                               'HCT (%)',
                               'MCV (fL)',
                               'MCH (pg)',
                               'MCHC (g/dL)',
                               'RDW (%)',
                               'RDW-SD (fL)',
                               'PLT (×10³/μL)',
                               'MPV (fL)',
                               '%NRBC (/100WBC)',
                               '#NRBC (×10³/μL)'
        ]
        
        self.diff_parameters = [
                                '%NEUT (%)',         
                                '%LYMPH (%)',        
                                '%MONO (%)',         
                                '%EO (%)',           
                                '%BASO (%)',         
                                '%UNCLASS (%)',      
                                '#NEUT (×10³/μL)',   
                                '#LYMPH (×10³/μL)',  
                                '#MONO (×10³/μL)',   
                                '#EO (×10³/μL)',     
                                '#BASO (×10³/μL)',   
                                '#UNCLASS (×10³/μL)'
        ]
        

    def setupDiffDeselectedExpectedResults(self):
        for parameter in self.cbc_parameters:
            self.EXPECTED_RESULTS[parameter] = ['true', 0]
            
        for parameter in self.diff_parameters:
            self.EXPECTED_RESULTS[parameter] = ['false', 1]
            
    def setupCBCDeselectedExpectedResults(self):
        for parameter in self.cbc_parameters:
            self.EXPECTED_RESULTS[parameter] = ['false', 1]
        
        for parameter in self.diff_parameters:
            self.EXPECTED_RESULTS[parameter] = ['true', 0]
        
    def clickReleaseButton(self):
        clickButton(self.release_button_symbol)
        
    def clickReleaseButton2(self):
        clickButton(self.release_button2_symbol)
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def uncheckDiff(self):
        mouseClick(self.diff_checkbox_symbol)
        counter = 0
        while (findObject(self.diff_checkbox_symbol).selected == 1):
            mouseClick(self.diff_checkbox_symbol)
            counter += 1
            
            if counter == 10:
                break
            
    def uncheckCBC(self):
        #Click on the CBC checkbox if it is checked.
        if findObject(self.cbc_checkbox_symbol).selected:
            mouseClick(self.cbc_checkbox_symbol)
            
    def populateTableData(self):
        Tables.populateTableData(self, self.bloodhound_table_symbol)
        
    def confirmReleaseResultsCheckedAndDisabled(self):
        for row in range(self.table.getRowCount()):
            #TODO need to set these values when I set them in the dialog box earlier
            parameter = str(self.table.getComponentAt(0, 0).getValueAt(row, 1)).strip()
            checked = self.EXPECTED_RESULTS[parameter][0]
            editable = self.EXPECTED_RESULTS[parameter][1]
            
            self.confirmCellIsChecked(row, parameter, checked)
            self.confirmCellIsEditable(row, parameter, editable)

    def confirmCellIsEditable(self, row, parameter, editable):
        if editable == 0:
            test.verify(self.table.getComponentAt(0, 0).isCellEditable(row, 0) == 0, "Confirm that the " + parameter + " checkbox is disabled")
        else:
            test.verify(self.table.getComponentAt(0, 0).isCellEditable(row, 0) == 1, "Confirm that the " + parameter + " checkbox is enabled")
        
    def confirmCellIsChecked(self, row, parameter, checked):
        check = str(self.table_data[row]['']).strip()
        if checked == 'true':
            test.verify(check == 'true', "Confirm that the parameter " + parameter + " is checked")
        else:
            test.verify(check == 'false', "Confirm that the paramter " + parameter + " is not checked")
            