# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try:
        test.log("Process the DigiCount Controls again (Rack mode)")
        
        step_counter = 50
        
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
        shared.inprocess.waitForTableStatusReadyForRelease()
        
        #50. Run  the 3 now active DigiCount™ samples through the analyzer again            
        #Confirm that the 3 controls complete processing without errors
        test.log("Step #" + str(step_counter)); step_counter += 1
    
        shared.spritecanvas.moveEmptyRackToTheBelt()    
        
        finishedrack_position_1_x = shared.spritecanvas.finishedrack_position_1[0]
        finishedrack_position_1_y = shared.spritecanvas.finishedrack_position_1[1]
        finishedrack_position_2_x = shared.spritecanvas.finishedrack_position_2[0]
        finishedrack_position_2_y = shared.spritecanvas.finishedrack_position_2[1]
        finishedrack_position_3_x = shared.spritecanvas.finishedrack_position_3[0]
        finishedrack_position_3_y = shared.spritecanvas.finishedrack_position_3[1]
        
        #Now Move the samples into the empty rack
        shared.spritecanvas.moveObject(finishedrack_position_1_x, finishedrack_position_1_y,pos1_x,pos1_y)
        shared.spritecanvas.moveObject(finishedrack_position_2_x, finishedrack_position_2_y,pos2_x,pos2_y)
        shared.spritecanvas.moveObject(finishedrack_position_3_x, finishedrack_position_3_y,pos3_x,pos3_y)
            
        #Run the rack through the analyzer
        #Confirm that the 3 controls complete processing without errors        
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.runSampleRack()
        shared.selectBloodhoundViewingStation()
        shared.inprocess.waitForTableStatusReadyForRelease()
        
        #51. Go to QC > DigiCount > Table and select the active Low control in the Control Selector combobox            "(R) Are you on the Low subtab or the Table subtab? Also, selecting a lot on one page does not automatically select it on the other (so the first confirm here is incorrect)
        #03/10/14 JJ - Updated."
        #Confirm results are displayed in the Table            
        #Confirm that lots in combobox are displayed hierarchically by day, week, month, or year if there are enough entries            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.digicounttab.clickTab()
        shared.digicounttab.selectAccessionNumberComboBoxItem(low_accession_number)
            
        #Confirm results are displayed in the Low and Table subtabs
        shared.selectBloodhoundViewingStation()
        shared.digicounttab.clickTableTab()
        shared.digicounttab.confirmTableTableData("digicount_low_table.csv")
        #Confirm that lots in combobox are displayed hierarchically by day, week, month, or year if there are enough entries
        test.log("Currently there only 3 entries.  Not enough to determine day, week, month or year")
        
        #52. Go to QC > DigiCount > Low and select the active Low control in the Control Selector combobox            
        #Confirm results are displayed in the Low Graph            
        shared.digicounttab.clickLowTab()
        shared.digicounttab.confirmResultsInLowGraph()
        
        #53. Go to QC > DigiCount > Table and select the active Normal control in the Control Selector combobox            
        #Confirm results are displayed in the Table            
        #Confirm that lots in combobox are displayed hierarchically by day, week, month, or year if there are enough entries            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.selectAccessionNumberComboBoxItem(normal_accession_number)        
        #Confirm results are displayed in the Normal and Table subtabs
        shared.digicounttab.clickTableTab()
        shared.digicounttab.confirmTableTableData("digicount_normal_table.csv")
        
        #Confirm that lots in combobox are displayed hierarchically by day, week, month, or year if there are enough entries
        test.log("TODO: Currently there only 3 entries.  Not enough to determine day, week, month or year")
        
        #54. Go to QC > DigiCount > Normal and select the active Normal control in the Control Selector combobox            
        #Confirm results are displayed in the Normal Graph
        shared.digicounttab.clickNormalTab()
        shared.digicounttab.confirmResultsInNormalGraph()
    
        #55. Go to QC > DigiCount > Table and select the active High control in the Control Selector combobox            
        #Confirm results are displayed in the Table            
        #Confirm that lots in combobox are displayed hierarchically by day, week, month, or year if there are enough entries
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.selectAccessionNumberComboBoxItem(high_accession_number)                
        #Confirm results are displayed in the High and Table subtabs
        shared.digicounttab.clickTableTab()
        shared.digicounttab.confirmTableTableData("digicount_high_table.csv")
        
        #56. Go to QC > DigiCount > High and select the active High control in the Control Selector combobox            
        #Confirm results are displayed in the High Graph
        shared.digicounttab.clickHighTab()
        shared.digicounttab.confirmResultsInHighGraph()            
    
        #Confirm that lots in combobox are displayed hierarchically by day, week, month, or year if there are enough entries        
        test.log("Currently there only 3 entries.  Not enough to determine day, week, month or year")
                
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
