# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    try:
    
        test.log("Process The DigiCount Controls in Rack Mode")
        
        step_counter = 11
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
    
        #Process the DigiCount™ Controls - Rack mode
        #11. Put the DigiCount™ barcode labels on the corresponding DigiCount™ Low, Normal and High control tubes and put them in a rack            
        test.log("Step #" + str(step_counter)); step_counter += 1
        
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
                
        #"12. Put new barcode labels on 2 fresh blood samples and put them in the rack after the DigiCount™ samples.
        #NOTE: These blood samples will be used later for Reproducibility and Whole Blood tests"                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.resetAccessionNumbers()
        shared.spritecanvas.moveObjectAndSetAccessionNumber(957,18,330,255)
        shared.spritecanvas.moveObjectAndSetAccessionNumber(957,18,329,281)
        
        #13. Run the rack through the analyzer
        test.log("Step #" + str(step_counter)); step_counter += 1
        total_samples = shared.inprocess.getTotalNumberOfSamples()
        shared.spritecanvas.runSampleRack()
        
        #14. Go to the In Process screen and watch the progress of all the samples as they move through the system            
        #Confirm that when the DigiCount™ Low, Normal and High controls finish processing that they are removed from the In Process screen            
        #"Confirm that the fresh blood samples complete processing without error
        #NOTE: If the 2 blood samples have problems then run newer fresher samples through"            "(R) This isn't really a “confirm” here, since a processing error would not be a bug. It's more like another step of “If there is an error and rerun fails, run the sample again or try a different sample.”
        #03/10/14 JJ - Updated but leaving as a confirm."
        test.log("Step #" + str(step_counter)); step_counter += 1    
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        shared.inprocess.waitForTableStatusReadyForRelease()
        test.verify(shared.inprocess.confirmAccessionNumberExistsInTable(low_accession_number) == False,"Confirm that the low accession number " + low_accession_number + " does not exist in the in process table")
        test.verify(shared.inprocess.confirmAccessionNumberExistsInTable(normal_accession_number) == False, "Confirm that the the normal accession number " + normal_accession_number + " does not exist in the in process table")
        test.verify(shared.inprocess.confirmAccessionNumberExistsInTable(high_accession_number) == False, "Confirm that the high accession number " + high_accession_number + " does not exist in the in process table")
        #"Confirm all the samples complete processing without error
        #NOTE: If the 2 blood samples have problems then run newer fresher samples through"
        
        #15. Go to the QC > DigiCount™ > Table subtab
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.digicounttab.clickTab()
        
        #16. In the Control combobox, select each of the new Low, Normal and High Controls            
        #Confirm Measured column has been populated for the DigiCount™ Low sample            
        #Confirm Measured column has been populated for the DigiCount™ Normal sample            
        #Confirm Measured column has been populated for the DigiCount™ High sample                        
        test.log("Step #" + str(step_counter)); step_counter += 1
        #Confirm Measured column has been populated for the DigiCount™ Low sample  
        shared.digicounttab.selectAccessionNumberComboBoxItem(low_accession_number)
        shared.digicounttab.confirmMeasuredColumns(getattr(shared.config,"expected_csv_result_dir") + "/digicountlow.csv")     
        #Confirm Measured column has been populated for the DigiCount™ Normal sample
        shared.digicounttab.selectAccessionNumberComboBoxItem(normal_accession_number)
        shared.digicounttab.confirmMeasuredColumns(getattr(shared.config,"expected_csv_result_dir") + "/digicountnormal.csv")
        #Confirm Measured column has been populated for the DigiCount™ High sample
        shared.digicounttab.selectAccessionNumberComboBoxItem(high_accession_number)
        shared.digicounttab.confirmMeasuredColumns(getattr(shared.config,"expected_csv_result_dir") + "/digicounthigh.csv") 
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
