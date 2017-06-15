# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try:
    
        test.log("Register the DigiCount Low Control")
        
        step_counter = 1
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
    
        #1. Go to the QC > Overview tab (NOT the QC > DigiCount™ tab)            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        
        #2. Under the "New control on <analyzer>" header in the toolbar, click the "DigiCount™" button            
        #Register the DigiCount™ Low Control            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.confirmLevelComboBoxSelectedItem("Low DigiCount™ control")
    
        #3. In the "New DigiCount™ Control" dialog, scan the 2D barcode from the DigiCount™ Low assay sheet            03/10/14 JJ - This whole section has been rewritten to match the rewrites of the Normal and High sections.
        #Confirm the lot number from the assay sheet appears in the "Lot" entry field            
        #Confirm that the value in the "Level" combobox matches the Level value displayed at the header of the Assay sheet, in this case "Low"            
        #Confirm that the value in the "Analyzer" combobox matches the Analyzer that you are creating the control on            
        #Confirm that the value in the "Expires" date fields matches the value displayed next to the Lot value on the Assay sheet            
        #Confirm that the "Active" checkbox is NOT checked            
        #Confirm that all the data from the assay sheet is inserted with a single 2D scan            "(C) Including expiration date and manufacturer mean and range for all parameters.
        #03/10/14 JJ - Issues address in update tests."
        #4. Click the "New" button            
        #Confirm that the "Historical SD" column already has entries for all the rows            "(C) This is only visible in the dialog, so you want to check it before you hit New.
        #03/10/14 JJ - Issues address in update tests."
        #5. In the "Activate/Edit DigiCount™ Controls" dialog, scan the barcodes from the DigiCount™ Low assay sheet to fill in the values            "(R) Is this test based on an old version of the VS? There are no longer two dialogs involved in the process of registering a new DigiCount control, and there should be only a single barcode now to scan.
        #03/10/14 JJ - Issues address in update tests."
        #Confirm that the Manufacturer / Mean and Manufacturer / Range column of the dialog are filled in for all the rows except the %UNCLASS and #UNCLASS rows            
        #Confirm that the values in the Manufacturer / Mean column of the dialog match the values that are displayed in the "Manufacturer" column of the assay sheet            03/10/13 KK Word changed from Target to Manufacturer.
        #Confirm that the values in the Range column of the dialog are two values that are separated by a dash            
        #"Confirm that the 1st value in the Range column is the Manufacturer / Mean minus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the first value in the Range cell would be 2.05.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"            
        #"Confirm that the 2nd value in the Range column is the Manufacturer / Mean plus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the 2nd value in the Range cell would be 2.65.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.newdigicountcontroldialog.setLotNumber("S1401001L")
        shared.newdigicountcontroldialog.enterDigiCountTableData(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow.csv")
        #The method below, writes data from the DigiCount Dialog to a csv file. This data can be used later for loading the dilaog box. 
        #shared.newdigicountcontroldialog.digiCountTableDataToCSV(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow_output.csv")
        shared.newdigicountcontroldialog.setExpirationDate()
        #Confirm the lot number from the assay sheet appears in the "Lot" entry field
        shared.newdigicountcontroldialog.confirmLotNumber("S1401001L")
        #Confirm that the value in the "Level" combobox matches the Level value displayed at the header of the Assay sheet, in this case "Low"        
        shared.newdigicountcontroldialog.confirmLevelComboBoxSelectedItem("Low DigiCount™ control")
        #Confirm that the value in the "Analyzer" combobox matches the Analyzer that you are creating the control on
        shared.newdigicountcontroldialog.confirmAnalyzerComboBoxSelectedItem("Bloodhound 1")
        #Confirm that the value in the "Expires" date fields matches the value displayed next to the Lot value on the Assay sheet
        shared.newdigicountcontroldialog.confirmExpiresDate()
        #Confirm that the "Active" checkbox is NOT checked
        shared.newdigicountcontroldialog.confirmDefaultActiveCheckBox()
        #Confirm that all the data from the assay sheet is inserted with a single 2D scan
        shared.newdigicountcontroldialog.confirmDigiCountTableData(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow.csv")
        
        #4. Click the "New" button            
        #Confirm that the "Historical SD" column already has entries for all the rows            "(C) This is only visible in the dialog, so you want to check it before you hit New.
        #03/10/14 JJ - Issues address in update tests."
        shared.newdigicountcontroldialog.confirmDigiCountTableData(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow.csv")
        #New button here dismisses the dialog.  Hold off on clicking this for now.
    
        #5. In the "Activate/Edit DigiCount™ Controls" dialog, scan the barcodes from the DigiCount™ Low assay sheet to fill in the values            "(R) Is this test based on an old version of the VS? There are no longer two dialogs involved in the process of registering a new DigiCount control, and there should be only a single barcode now to scan.
        #03/10/14 JJ - Issues address in update tests."
        #Confirm that the Manufacturer / Mean and Manufacturer / Range column of the dialog are filled in for all the rows except the %UNCLASS and #UNCLASS rows            
        #Confirm that the values in the Manufacturer / Mean column of the dialog match the values that are displayed in the "Manufacturer" column of the assay sheet            03/10/13 KK Word changed from Target to Manufacturer.
        #Confirm that the values in the Range column of the dialog are two values that are separated by a dash            
        #"Confirm that the 1st value in the Range column is the Manufacturer / Mean minus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the first value in the Range cell would be 2.05.    
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"            
        #"Confirm that the 2nd value in the Range column is the Manufacturer / Mean plus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the 2nd value in the Range cell would be 2.65.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"
        #Confirm that the "Historical SD" column already has entries for all the rows            "(C) This is only visible in the dialog, so you want to check it before you hit New.            
        shared.newdigicountcontroldialog.confirmLotNumber("S1401001L")        
        #Confirm that the Manufacturer / Mean and Manufacturer / Range column of the dialog are filled in for all the rows except the %UNCLASS and #UNCLASS rows
        #Confirm that the values in the Manufacturer / Mean column of the dialog match the values that are displayed in the "Target" column of the assay sheet
        #Confirm that the values in the Manufacturer / Mean column of the dialog match the values that are displayed in the "Manufacturer" column of the assay sheet            03/10/13 KK Word changed from Target to Manufacturer.
        shared.newdigicountcontroldialog.confirmDigiCountTableData(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow.csv")          
        #Confirm that the values in the Range column of the dialog are two values that are separated by a dash        
        #"Confirm that the 1st value in the Range column is the Manufacturer / Mean minus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the first value in the Range cell would be 2.05.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"        
        #"Confirm that the 2nd value in the Range column is the Manufacturer / Mean plus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the 2nd value in the Range cell would be 2.65.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"
        #Confirm that the "Historical SD" column already has entries for all the rows            "(C) This is only visible in the dialog, so you want to check it before you hit New.
        #03/10/14 JJ - Issues address in update tests."
        #5. In the "Activate/Edit DigiCount™ Controls" dialog, scan the barcodes from the DigiCount™ Low assay sheet to fill in the values            "(R) Is this test based on an old version of the VS? There are no longer two dialogs involved in the process of registering a new DigiCount control, and there should be only a single barcode now to scan.
        #03/10/14 JJ - Issues address in update tests."
        #Confirm that the Manufacturer / Mean and Manufacturer / Range column of the dialog are filled in for all the rows except the %UNCLASS and #UNCLASS rows            
        #Confirm that the values in the Manufacturer / Mean column of the dialog match the values that are displayed in the "Manufacturer" column of the assay sheet            03/10/13 KK Word changed from Target to Manufacturer.
        #Confirm that the values in the Range column of the dialog are two values that are separated by a dash            
        #"Confirm that the 1st value in the Range column is the Manufacturer / Mean minus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the first value in the Range cell would be 2.05.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"            
        #"Confirm that the 2nd value in the Range column is the Manufacturer / Mean plus the Range value from the Assay sheet
        #NOTE: For example, if the Mean is 2.35 and the Range value on the Assay sheet is 0.3 then the 2nd value in the Range cell would be 2.65.
        #NOTE: You don't need to confirm that every Range value is correct, spot check a few throughout the list of parameters"            
        
        test.log("This method is no longer needed because range is displayed as a string now. Example: 2.20 - 2.80 instead of a number ie: 0.3")
        #shared.newdigicountcontroldialog.confirmDigiCountManufacturerRangeRenderer()
    
        #4. Click the "New" button            
        #Confirm the Activate/Edit DigiCount™ Controls dialog closes            
        #Confirm the DigiCount™ Low sample is registered            
        #Confirm the barcode is now displayed in the Control in the toolbar            
        #Confirm that upon leaving the "Activate/Edit DigiCount™ Controls" dialog you are now in the QC > DigiCount™ page NOT the QC > Overview page                        
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.newdigicountcontroldialog.clickNewButton()
        #Confirm the Activate/Edit DigiCount™ Controls dialog closes
        shared.newdigicountcontroldialog.confirmDialogWasDismissed()
        test.verify(shared.qctab.isSelected() == True, "Confirm that we went back to the QC page")        
        #Confirm the DigiCount™ Low sample is registered
        shared.qctab.confirmRegisteredLowLabel()        
        #Confirm the barcode is now displayed in the Control in the toolbar
        shared.qctab.confirmBarcode("S1401001L")        
        #Confirm that upon leaving the "Activate/Edit DigiCount™ Controls" dialog you are now in the QC > DigiCount™ page NOT the QC > Overview page
        test.verify(shared.digicounttab.isSelected() == True, "Confirm that the DigiCount tab is selected")
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()

      
