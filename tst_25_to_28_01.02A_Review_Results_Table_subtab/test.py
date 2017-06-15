# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try       

        test.log("Process The DigiCount Controls in Open Mode 1")
        
        step_counter = 25
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.simulateDigiCountScan("Low")
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.simulateDigiCountScan("Normal")
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.simulateDigiCountScan("High")
        shared.spritecanvas.selectAnalyzerSimulator()
        
        sample_2 = shared.newdigicountcontroldialog.sample_2
        
        low_accession_number = shared.newdigicountcontroldialog.scan_dictionary["low"]
        normal_accession_number = shared.newdigicountcontroldialog.scan_dictionary["normal"]
        high_accession_number = shared.newdigicountcontroldialog.scan_dictionary["high"]
        
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode(low_accession_number,sample_2)
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode(normal_accession_number,sample_2)
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode(high_accession_number,sample_2)
        
        #Review Results - Table subtab
    
        #25. Go to the QC > DigiCount™ > Table subtab            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.digicounttab.clickTab()
    
        #26. Click the Control combobox and select the Low control that was just processed            
        #Confirm the results are reported in the DigiCount™ Table            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.selectAccessionNumberComboBoxItem(low_accession_number)
        #Confirm the results are reported in the DigiCount™ Table
        shared.digicounttab.confirmMeasuredColumns(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow.csv")
    
        #27. Click the Control combobox and select the Normal control that was just processed            
        #Confirm the results are reported in the DigiCount™ Table            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.selectAccessionNumberComboBoxItem(normal_accession_number)
        #Confirm the results are reported in the DigiCount™ Table
        shared.digicounttab.confirmMeasuredColumns(getattr(shared.config,"expected_csv_result_dir") + "/digicountnormal.csv")
    
        #28. Click the Control combobox and select the High control that was just processed            
        #Confirm the results are reported in the DigiCount™ Table            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.selectAccessionNumberComboBoxItem(high_accession_number)        
        #Confirm the results are reported in the DigiCount™ Table
        shared.digicounttab.confirmMeasuredColumns(getattr(shared.config,"expected_csv_result_dir") + "/digicounthigh.csv")
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
