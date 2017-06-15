# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from config import Config

class BootstrapPopulationMeansDialog(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.analyzer_combobox_symbol = ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.number_of_batches_textfield_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.reasons_textarea_symbol = ":Bloodhound™ Viewing Station " + version + "_JTextArea"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.bootstrap_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Bootstrap_JButton"
        self.parameter_panel_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel"
        
    def setNumberOfBatchesText(self,text):
        number_of_batches = findObject(self.number_of_batches_textfield_symbol)
        number_of_batches.text = text
        
    def clickCancelButton(self):
        clickButton(self.cancel_button_symbol)
        
    def clickBootstrapButton(self):
        clickButton(self.bootstrap_button_symbol)
        
    def selectAnalyzerItem(self,item):
        Controls.selectComboboxItem(self,self.analyzer_combobox_symbol, item_name)
        
    def confirmDialogName(self,name):
        dialog = findObject(self.object_symbol)
        test.verify(dialog.name.__contains__(name),"Confirm that the Dialog name contains: " + name)

    #226. Observe the dialog has a Analyzer selector combobox, a "Number of batches" text field with "10" 
    #filled by default, and a Reason comment box on the left section of the dialog.
    def confirmDefaultControls(self):
        analyzer = findObject(self.analyzer_combobox_symbol)
        number_of_batches = findObject(self.number_of_batches_textfield_symbol)
        reason = findObject(self.reasons_textarea_symbol)
        
        test.verify(analyzer.enabled == True,"Confirm that the analyzer combobox exists and is enabled by default")
        test.verify(number_of_batches.text == "10", "Confirm that the number of batches text field contains '10' by default")
        test.verify(reason.enabled == True, "Confirm that the Reason text area exists and is enabled by default")
        
    def setParameterCheckBox(self,name,check):
        parameters = findObject(self.parameter_panel_symbol)

        components = parameters.getComponents()
        for index in range(components.length):
            if components.at(index).text == name:
                if(check):
                    components.at(index).selected = True
                else:
                    components.at(index).selected = False
                break
        
    def setReasonsTextArea(self,text):
        reasons = findObject(self.reasons_textarea_symbol)
        reasons.text = text
        
    def confirmBootstrapButtonEnabled(self):
        bootstrap_button = findObject(self.bootstrap_button_symbol)
        test.verify(bootstrap_button.enabled == True,"Confirm that the bootstrap button is now enabled")
        
        