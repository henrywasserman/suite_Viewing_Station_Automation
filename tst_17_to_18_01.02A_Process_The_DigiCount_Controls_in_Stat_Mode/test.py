# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try:
    
        test.log("Process The DigiCount Controls in Stat Mode")
        
        step_counter = 17
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
    
        #Process the DigiCount™ Controls in STAT mode
    
        #"17. Put the DigiCount™ Low, Normal and High tubes in the STAT rack and close the drawer to start them processing in the analyzer
        #
        #NOTE: If the tester does not have access to STAT or Open Port then they should run the controls through the analyzer in the rack again to generate at least 3 total runs before going on to the ""Review Results - Table subtab"" section"                
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
            
        locations = [low_x,low_y,normal_x,normal_y,high_x,high_y]
        
        shared.spritecanvas.runSamplesInStatDrawer(locations)
    
        #18. Go to the In Process screen and watch the progress of the DigiCount™ samples            
        #Confirm all the samples complete processing without error            "(R) See above.
        #03/10/14 JJ - Leaving as is, see above."
        #Process the DigiCount™ Controls in Open Port mode            
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        shared.inprocess.waitForTableStatusReadyForRelease()        

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
