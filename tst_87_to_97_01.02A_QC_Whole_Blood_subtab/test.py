# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():            
    try:
        step_counter = 87
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        shared.spritecanvas.selectAnalyzerSimulator()
        
        shared.spritecanvas.runSampleInOpenMode(957,20)
        accession_number = getattr(shared.spritecanvas,"accession_numbers")[0]
        
        shared.spritecanvas.scanSample(224,374,224,374)
        shared.selectBloodhoundViewingStation()
        shared.reproducibilitytab.newreproducibilitytestdialog.clickNewButton()        
        
        shared.selectBloodhoundViewingStation()
        
        #87. Under the "New control on <analyzer>" header in the toolbar, click the "Whole Blood" button            
        #Confirm that the "New Whole Blood Control" dialog is displayed            
        #Confirm that the "Barcode" field is empty            
        #Confirm that the "Run Profile" combobox has a default value of "Default"
                    
        #Confirm that the "Include retic slide" checkbox does NOT have a check in it            "(R) There's also an “include retic slide” option now.
        #03/10/14 JJ - Confirm added."
        #Confirm that there are "Cancel" and "New" buttons            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.reproducibilitytab.clickWholeBloodButton()        
        #Confirm that the "New Whole Blood Control" dialog is displayed
        shared.wholebloodtab.newwholebloodcontroldialog.confirmDialogIsDisplayed()        
        #Confirm that the "Barcode" field is empty
        shared.wholebloodtab.newwholebloodcontroldialog.confirmBarcodeFieldIsEmpty()        
        #Confirm that the "Run Profile" combobox has a default value of "Default"
        shared.wholebloodtab.newwholebloodcontroldialog.confirmComboSelectedItem("Default")
        #Confirm that the "Include retic slide" checkbox does NOT have a check in it            "(R) There's also an “include retic slide” option now.
        #03/10/14 JJ - Confirm added."
        shared.wholebloodtab.newwholebloodcontroldialog.confirmIncludeReticCheckbox("unchecked")
        #Confirm that there are "Cancel" and "New" buttons
        shared.wholebloodtab.newwholebloodcontroldialog.confirmCancelButtonExists()
        shared.wholebloodtab.newwholebloodcontroldialog.confirmNewButtonExists()
    
        #88. Scan the barcode of the other blood sample that was run through the analyzer previously    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.scanSample(254,374,224,374)
        shared.selectBloodhoundViewingStation()
    
        #89. Click the "New" button            
        #"Confirm that the ""Barcode Matches Active Control"" dialog is displayed with the following message:
        #Barcode ''<barcode>"" is an active sample in the In Process screen. Registering this barcode will cause any new runs of that sample to appear as a Whole Blood control. Are you sure you want to continue?"
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.reproducibilitytab.newreproducibilitytestdialog.clickNewButton()
        #"Confirm that the ""Barcode Matches Active Control"" dialog is displayed with the following message:
        #Barcode ''<barcode>"" is an active sample in the In Process screen. Registering this barcode will cause any new runs of that sample to appear as a Whole Blood control. Are you sure you want to continue?"
        shared.wholebloodtab.newwholebloodcontroldialog.confirmBarcodeMatchesActiveControlMessageBoxText(accession_number)
        
        #90. Click the "Cancel" button            
        #Confirm that the "Barcode Matches Active Control" dialog closes            
        #Confirm that the focus is back on the "New Whole Blood Control" dialog            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.newwholebloodcontroldialog.clickBarcodeMatchesActiveControlCancelButton()
        #Confirm that the "Barcode Matches Active Control" dialog closes
        shared.wholebloodtab.newwholebloodcontroldialog.confirmBarcodeMatchesActiveControlMessageBoxWasDismissed()        
        #Confirm that the focus is back on the "New Whole Blood Control" dialog
        shared.wholebloodtab.newwholebloodcontroldialog.confirmDialogIsDisplayed()

        #91. Click the "Cancel" button            
        #Confirm the "New Whole Blood Control" dialog closes            
        #Confirm the  scanned barcode is NOT displayed in the Control combobox
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.newwholebloodcontroldialog.clickCancelButton()
        #Confirm the "New Whole Blood Control" dialog closes
        shared.wholebloodtab.newwholebloodcontroldialog.confirmDialogWasDismissed()
        #Confirm the  scanned barcode is NOT displayed in the Control combobox
        shared.wholebloodtab.confirmControlComboBoxSelectedItem('<null>')   
        
        #92. Go to the In Process screen and highlight the record that triggered the Barcode Matches Active Control dialog in the previous test
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickTab()
        shared.inprocess.clickOnTableRowByName("Accession #",accession_number)

        #93. Click the "Delete Sample" button in the toolbar        
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickDeleteSampleButton()
        
        #94. In the Delete Sample dialog,  enter your Username and Password and click the "Delete" button            
        #Confirm the sample is no longer displayed
        test.log("Step #" + str(step_counter)); step_counter += 1        
        #Confirm the sample is no longer displayed
        shared.inprocess.deletesampledialog.enterUsername(shared.vadim.username)
        shared.inprocess.deletesampledialog.enterPassword(shared.vadim.password)
        shared.inprocess.deletesampledialog.clickDeleteButton()
        shared.inprocess.confirmRowIsNotInTable("Accession #",accession_number)

        #95. Go to the QC > Overview subtab and under the "New control on <analyzer>" header in the toolbar, click the "Whole Blood" button        
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.reproducibilitytab.clickWholeBloodButton()
        
        #96. Scan the barcode that triggered the Barcode Matches Active Control dialog previously and click on the "New" button            
        #Confirm that the "New Whole Blood Control" dialog closes
        #Confirm that the barcode is displayed in the Control Selector combobox
        #Confirm that the message "Started: [date/time]" is displayed to the right of the Control Selector combobox with [date/time] being the time the control was created
        #"Confirm that below the ""Started:"" message is “Active until: [date/time]” where 
        #[date/time] is the ""Started"" date / time plus 24 hours"            
        #Confirm that the "Active" message is displayed below the Control Selector combobox            
        #Confirm that below the "Active" message is “No runs on [Analyzer]” where [Analyzer] is the Analyzer name
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.scanSample(224,374,224,374)
        shared.selectBloodhoundViewingStation()
        shared.reproducibilitytab.newreproducibilitytestdialog.clickNewButton()    
        #Confirm that the "New Whole Blood Control" dialog closes
        shared.wholebloodtab.newwholebloodcontroldialog.confirmDialogWasDismissed()
        #Confirm that the barcode is displayed in the Control Selector combobox
        shared.qctab.confirmBarControlComboBoxItemSelected(accession_number)    
        #Confirm that the message "Started: [date/time]" is displayed to the right of the Control Selector combobox with [date/time] being the time the control was created
        shared.qctab.confirmStartedLabel()        
        #"Confirm that below the ""Started:"" message is “Active until: [date/time]” where 
        #[date/time] is the ""Started"" date / time plus 24 hours"
        shared.qctab.confirmActiveUntilLabel()        
        #Confirm that the "Active" message is displayed below the Control Selector combobox
        shared.qctab.confirmStatusLabel()        
        #Confirm that below the "Active" message is “No runs on [Analyzer]” where [Analyzer] is the Analyzer name
        shared.qctab.confirmRunsLabel()
        
        #97. Click the Control Selector combobox            
        #Confirm the barcode is displayed in bold and has a checkmark to the left        
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickControlComboBox()        
        #Confirm the barcode is displayed in bold and has a checkmark to the left
        test.vp("Control Combobox")
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
