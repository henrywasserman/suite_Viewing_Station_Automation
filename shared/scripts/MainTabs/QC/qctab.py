# -*- coding: utf-8 -*-
import datetime
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from datetime import datetime, timedelta
from config import Config

class QCTab(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Bloodhound™ Viewing Station " + version + ".QC_TabProxy"
        self.barcode_read_failure_label_symbol = ":Bloodhound™ Viewing Station " + version + ".Barcode Read Failure_JLabel"
        self.anlalyzer_events_dialog_acknowledge_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Acknowledge_JButton"
        self.registered_label_symbol = ":QC.Inactive: Inactive_JLabel"
        self.qc_combobox_symbol = ":QC.New control on Bloodhound 1:_JComboBox"
        self.awaiting_first_run_label_symbol = ":QC.Awaiting first run_JLabel"
        self.pending_label_symbol = ":QC.Pending_JLabel"
        self.failure_label_symbol = ":QC.Fail 5; Warn 34_JLabel"
        self.started_label_symbol = ":QC.Started: 2/11/14 1:50 PM_JLabel"
        self.closed_label_symbol = ":QC.Closed: 2/12/14 1:50 PM_JLabel"
        self.active_until_label_symbol = ":QC.Active until: AM_JLabel"
        self.status_label_symbol = ":QC.Active_JLabel"
        self.runs_label_symbol = ":QC.No runs on Bloodhound 1._JLabel"
        self.analyzer_selector_symbol = ":QC_JComboBox"
        self.reflag_all_button_symbol = ":QC.Reflag all_JButton"
        self.export_data_text_field = ":Bloodhound™ Viewing Station " + version + ".Save As:_JTextField"
        
        self.digicount_button_symbol = ":QC.DigiCount™_JButton"
        self.reproducibility_button_symbol = ":QC.Reproducibility_JButton"
        self.wholeblood_button_symbol = ":QC.Whole Blood_JButton"
        self.export_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Export_JButton"
        self.cancel_button_symbol = ":QC.Cancel_JButton"
        self.in_progress_label_symbol = ":QC.InProgress_JLabel"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
        
    def confirmQCTabIsSelected(self):
        tab = findObject(self.object_symbol)
        test.verify("QC" == tab.text,"Confirm that the QC tab is selected")
        
    def waitForInProgressLabelToEqualThree(self):
        #Setting counter to 10,000 here. we can throttle this back or forward by adding a snooze if we need to.
        counter = 0
        while (True):
            text = ""
            if object.exists(self.in_progress_label_symbol):
                in_progress = squish.findObject(self.in_progress_label_symbol)
                text = in_progress.text
            if ("In Progress (3" in text):
                break
            counter += 1
            if (counter == 10000):
                break
        
    def confirmBarControlComboBoxItemSelected(self,item):
        combo_box = findObject(self.qc_combobox_symbol)
        test.verify(item == str(combo_box.getSelectedItem()), "Confirm that the expected item " + item + " is the selected item " + str(combo_box.getSelectedItem()))
        
    def clickControlComboBox(self):
       mouseClick(findObject(self.qc_combobox_symbol), 59, 23, 0, Button.Button1) 
        
    def confirmAwaitingFirstRunLabel(self,text):
        label = findObject(self.awaiting_first_run_label_symbol)
        test.verify(text == label.text,"Confirm that the expected text " + text + " is equal to the actual label text " + label.text)
    
    def confirmPendingLabel(self,text):
        label = findObject(self.pending_label_symbol)
        test.verify(text == label.text, "Confirm that the expected text " + text + " is equal to the actual label text " + label.text)    
            
    def confirmFailureLabel(self,text):
        label = findObject(self.failure_label_symbol)
        test.verify(text == label.text, "Confirm that the expected text " + text + " is equal to the actual label text " + label.text)
     
     #TODO get function working in the child classes in python   
    def confirmQCButtons(self):
        #Confirm the DigiCount, Reproducibility and Whole Blood Buttons are enabled.
        test.verify(findObject(self.digicount_button_symbol).enabled == True, "Confirm that the DigiCount button is enabled")
        test.verify(findObject(self.reproducibility_button_symbol).enabled == True, "Confirm that the Reproducibility button is enabled")
        test.verify(findObject(self.wholeblood_button_symbol).enabled == True, "Confirm that the Whole Blood button is enabled")
        
    def confirmReFlagButtonEnabled(self):
        test.verify(findObject(self.reflag_all_button_symbol).enabled == True,"Confirm that the Reflag all button is enabled")
        
    def confirmAnalyzerSelector(self):
        test.verify(findObject(self.analyzer_selector_symbol).enabled == True, "Confirm there is an Analyzer selector combobox and it is enabled")
        
    def getControlDropdownListItems(self):
        list = []
        for item in range(findObject(self.qc_combobox_symbol).getItemCount()):
            list.append(item)
        return list
    
    def confirmComboBoxItemIsSelected(self,item):
        combobox = findObject(self.qc_combobox_symbol)
        test.verify(item == str(combobox.getSelectedItem()),"Confirm")
            
    def getAnalyzerDropdownListItems(self):
        list = []
        for item in range(findObject(self.analyzer_selector_symbol).getItemCount()):
            list.append(item)
        return list
    
    def exportData(self,tab):
        clickButton(findObject(":QC.Export_JButton"))
        #Get the Filename from the text field
        textfield = findObject(self.export_data_text_field)
        filename = textfield.getText()
        
        
        #First delete the file if it already exists
        
        if tab == "reproducibility":
            exportfile = "/Volumes/SmokeTest/data/reproducibility/" + filename
            save_as_name = "data/reproducibility/" + filename
            tempfile = "/Volumes/SmokeTest/tempfile/" + filename
        elif tab == "wholeblood":
            exportfile = "/Volumes/SmokeTest/data/wholeblood/" + filename
            save_as_name = "data/wholeblood/" + filename
            tempfile = "/Volumes/SmokeTest/tempfile/" + filename

        if os.path.exists(exportfile):
            os.remove(exportfile)
    
        #Now set the edit box to the full pathname to the file
        textfield.setText(save_as_name)
        clickButton(findObject(self.export_button_symbol))
    
        self.unicodeToAscii(exportfile,tempfile)
        #Now move the ascii file over the original file.
        shutil.move(tempfile,exportfile)
        
        return exportfile
    
    def unicodeToAscii(self,inputfile,outputfile):
        infile = codecs.open(inputfile,'r', encoding='utf-16-le')

        newlines = []
        for line in infile:
            newlines.append(line)

        outfile = codecs.open(outputfile, 'w', encoding='utf-8')
        outfile.writelines(newlines)
        infile.close()
        outfile.close()
        
    def confirmBarcodeReadFailure(self):
        counter = 0
        while(True):
            if object.exists(self.barcode_read_failure_label_symbol):
                barcode_label = findObject(self.barcode_read_failure_label_symbol)
                
                if str(barcode_label.text) == "Barcode Read Failure":
                    barcode_label = findObject(self.barcode_read_failure_label_symbol)
                    test.verify(True,"Found Barcode Read Failure Error in Analyzer Events Dialog")
                    break
            
            snooze(1.0)
            counter += 1
            
            if counter == 30:
                test.verify(False,"Did not find Barcode Read Failure Error in Analyzer Events Dialog")
                break
            
    def clickAcknowledgeButton(self):
        squish.clickButton(self.anlalyzer_events_dialog_acknowledge_button_symbol)
        
    def isSelected(self):
        return findObject(self.object_symbol).selected == 1
    
    def confirmQCTabIsSelected(self):
        test.verify(self.isSelected() == True, "Confirm that the QCTab is selected")
    
    def confirmRegisteredLowLabel(self):
        label = findObject(self.registered_label_symbol)
        test.verify("Inactive: Low" == str(label.text), "Confirm that the Inactive: Low label is present")
        
    def confirmRegisteredNormalLabel(self):
        label = findObject(self.registered_label_symbol)
        test.verify("Inactive: Normal" == str(label.text), "Confirm that the Inactive: Normal label is present")

    def confirmRegisteredHighLabel(self):
        label = findObject(self.registered_label_symbol)
        test.verify("Inactive: High" == str(label.text), "Confirm that the Inactive: High label is present")
        
    def confirmBarcode(self,expected_item):
        combo_box = findObject(self.qc_combobox_symbol)
        Controls.confirmSelectedItem(self,combo_box,expected_item,"Barcode")
        
    def confirmStartedLabel(self):
        label = squish.findObject(self.started_label_symbol)
        now = datetime.now()
        date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)[2:]
        test.verify("Started: " + date in label.text,"Confirm that the the Started: label contains " + date)
        
    def confirmActiveUntilLabel(self):
        label = squish.findObject(self.active_until_label_symbol)
        tomorrow = datetime.now() + timedelta(hours=24)
        date = str(tomorrow.month) + "/" + str(tomorrow.day) + "/" + str(tomorrow.year)[2:]
        test.verify("Active until: " + date in label.text, "Confirm that the Active Until: label contains " + date)
        
    def confirmClosedLabel(self):
        label = squish.findObject(self.closed_label_symbol)
        tomorrow = datetime.now() + timedelta(hours=24)
        date = str(tomorrow.month) + "/" + str(tomorrow.day) + "/" + str(tomorrow.year)[2:]
        test.verify("Closed: " + date in label.text, "Confirm that the Closed: label contains " + date)
        
    def confirmStatusLabel(self):
        label = squish.findObject(self.status_label_symbol)
        test.verify("Active" == label.text, "Confirm that the Status label is Active")
        
    def confirmRunsLabel(self):
        label = squish.findObject(self.runs_label_symbol)
        test.log("This is a closed Mantis bug #0012286: [QC Whole Blood] New QC WB control displays STATUS_NO_RUNS message in toolbar")
        test.verify("No runs on Bloodhound 1." == label.text,"Confirm that No runs on Bloodhound 1. label is displayed")
                