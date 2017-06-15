# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():      
    
    try:      

        test.log("Process The DigiCount Controls in Open Mode 1")
        
        step_counter = 29
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        #Setup some data
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.simulateDigiCountScan("Low")
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.simulateDigiCountScan("Normal")
        shared.qcoverview.clickDigiCountButton()
        shared.newdigicountcontroldialog.simulateDigiCountScan("High")
        shared.spritecanvas.selectAnalyzerSimulator()
        shared.spritecanvas.moveEmptyRackToTheBelt()
        
        #Now Move the samples into the empty rack    
        low_accession_number = getattr(shared.newdigicountcontroldialog,"scan_dictionary")["low"]
        normal_accession_number = getattr(shared.newdigicountcontroldialog,"scan_dictionary")["normal"]
        high_accession_number = getattr(shared.newdigicountcontroldialog,"scan_dictionary")["high"]
        
        low_location = shared.spritecanvas.getSampleLocationByAccessionNumber(low_accession_number)
        normal_location = shared.spritecanvas.getSampleLocationByAccessionNumber(normal_accession_number)
        high_location = shared.spritecanvas.getSampleLocationByAccessionNumber(high_accession_number)
        
        low_x = low_location[0]
        low_y = low_location[1]
        
        normal_x = normal_location[0]
        normal_y = normal_location[1]
        
        high_x = high_location[0]
        high_y = high_location[1]
        
        pos1_x = shared.spritecanvas.emptyrack_position_1[0]
        pos1_y = shared.spritecanvas.emptyrack_position_1[1]
        
        pos2_x = shared.spritecanvas.emptyrack_position_2[0]
        pos2_y = shared.spritecanvas.emptyrack_position_2[1]
        
        pos3_x = shared.spritecanvas.emptyrack_position_3[0]
        pos3_y = shared.spritecanvas.emptyrack_position_3[1]
        
        shared.spritecanvas.moveObject(low_x, low_y,pos1_x,pos1_y)
        shared.spritecanvas.moveObject(normal_x, normal_y,pos2_x,pos2_y)
        shared.spritecanvas.moveObject(high_x, high_y,pos3_x,pos3_y)
    
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.runSampleRack()
    
        #Review Results - Low, Normal, High and All graph subtabs
        
        low_accession_number = getattr(shared.newdigicountcontroldialog,"scan_dictionary")["low"]
        normal_accession_number = getattr(shared.newdigicountcontroldialog,"scan_dictionary")["normal"]
        high_accession_number = getattr(shared.newdigicountcontroldialog,"scan_dictionary")["high"]
        
        #29. Go to the QC > DigiCount™ > Low subtab            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.selectBloodhoundViewingStation()
        shared.qctab.clickTab()
        shared.digicounttab.clickTab()
        shared.digicounttab.clickLowTab()
    
        #30. Click the Control combobox and select the Low control that was just processed            
        #Confirm the results are reported in the DigiCount™ Low graph            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.selectAccessionNumberComboBoxItem(low_accession_number)
        #Confirm the results are reported in the DigiCount™ Low graph
        shared.digicounttab.confirmResultsInLowGraph()
    
        #31. Go to the QC > DigiCount™ > Normal subtab    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.clickNormalTab()
    
        #32. Click the Control  combobox and select the Normal control            
        #Confirm the results are reported in the DigiCount™ Normal graph            
        test.log("Step #" + str(step_counter)); step_counter += 1       
        shared.digicounttab.selectAccessionNumberComboBoxItem(low_accession_number)
        shared.digicounttab.confirmResultsInNormalGraph()
    
        #33. Go to the QC > DigiCount™ > High subtab
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.clickHighTab()
    
        #34. Click the Control  combobox. Select the High control            
        #Confirm the results are reported in the DigiCount™ High graph                
        test.log("Step #" + str(step_counter)); step_counter += 1       
        shared.digicounttab.selectAccessionNumberComboBoxItem(low_accession_number)
        shared.digicounttab.confirmResultsInHighGraph()
    
        #35. Go to the QC > DigiCount™ > All subtab        
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.clickTab()
        shared.digicounttab.clickAllTab()
        
        #36. Click the Control combobox. Select the control that was just run (barcode value without an L, N or H suffix)            
        #Confirm the results are reported in the DigiCount™ All graph            
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("In this case starting as QC chooses one of two medical records so we need to grab the accession number")
        test.log("From the list box")
        accession_number = shared.digicounttab.getListBoxItems()[0]
    
        shared.digicounttab.selectAccessionNumberComboBoxItem(accession_number)
        shared.digicounttab.confirmResultsInAllGraph()
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
    