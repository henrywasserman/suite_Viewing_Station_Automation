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
        
        step_counter = 19
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
    
        #"19. Take the DigiCount™ Low sample and use the Open Port to run it through the analyzer
        #NOTE: You will need to follow the process for running a sample with the Open Port"            
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
        
        sample_2 = shared.newdigicountcontroldialog.sample_2
        
        low_accession_number = shared.newdigicountcontroldialog.scan_dictionary["low"]
        normal_accession_number = shared.newdigicountcontroldialog.scan_dictionary["normal"]
        high_accession_number = shared.newdigicountcontroldialog.scan_dictionary["high"]
        
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode(low_accession_number,sample_2)
    
        #20. Go to the In Process screen and watch the progress of the sample as it moves through the system and completes processing            
        #Confirm the sample completes processing without error            "(R) See above.
        #03/10/14 JJ - Leaving as is, see above."    
        test.log("Step #" + str(step_counter)); step_counter += 1  
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        shared.inprocess.waitForTableStatusReadyForRelease()        
    
        #21. Take the DigiCount™ Normal sample and use the Open Port to run it through the analyzer            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode(normal_accession_number,sample_2)
        
        #22. Go to the In Process screen and watch the progress of the sample as it moves through the system and completes processing            
        #Confirm the sample completes processing without error            "(R) See above.
        #03/10/14 JJ - Leaving as is, see above."
        test.log("Step #" + str(step_counter)); step_counter += 1
        #Confirm the sample completes processing without error
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        shared.inprocess.waitForTableStatusReadyForRelease()        
                
        #23. Take the DigiCount™ High sample and use the Open Port to run it through the analyzer
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.runSampleInOpenModeAndSimulateBarcode(high_accession_number,sample_2)
                
        #24. Go to the In Process screen and watch the progress of the sample as it moves through the system and completes processing            
        #Confirm the sample completes processing without error            "(R) See above.
        #03/10/14 JJ - Leaving as is, see above."
        test.log("Step #" + str(step_counter)); step_counter += 1        
        #Confirm the sample completes processing without error
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
