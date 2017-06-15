# -*- coding: utf-8 -*-
import shutil
import sys
import os
import re
import exceptions
import traceback

def main():
    
    try:
        
        step_counter = 30
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        version = shared.version
        shared.setConfigLisReleaseDelay(6)
        
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
        
        #30. Run 3 samples in STAT drawer twice.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.resetAccessionNumbers()
        shared.spritecanvas.runSamplesInStatDrawer()
        shared.spritecanvas.runSamplesInStatDrawer()
        
        test.log("Bring Viewing Station To The Front")
        waitForObject(":Bloodhound™ Viewing Station " + version + "_JPanel").getTopLevelAncestor().toFront()
    
        #Confirm samples run without errors and results are available in the In Process and Results Queue list.
        shared.inprocess.confirmSTATSamples(shared.spritecanvas,6)
        shared.results.confirmSTATSamples(shared.spritecanvas,6)
                
        #Confirm the Sample location, Slide Location of runs, and Sample Status are displayed correctly in the In Process sidebar.
        shared.inprocess.clickTab()
        shared.inprocess.clickOnFirstRowOfTable()
        
        test_pattern = '.*Sample output by Bloodhound\\s+\\d+\\s\(STAT position \\d+\) at \\d+\:\d+.*'
        pat = re.compile(test_pattern)
    
        sidebar_text = shared.inprocess.getSideBarTextByIndex(2,"")
        test.verify(pat.match(sidebar_text) != None,"Confirm that " + test_pattern + " matches sidebar text " + sidebar_text)
    
        test_pattern = '.*\d+\:\d+ [AM|PM]+\: In Bloodhound \d slide rack \d+\, slot \d+\.'
        pat = re.compile(test_pattern)
        
        sidebar_text = shared.inprocess.getSideBarTextByIndex(4,"")
        test.verify(pat.match(sidebar_text) != None,"Confirm that the test pattern " + test_pattern + "matches the sidebar text " + sidebar_text)
                
        #Confirm results detail are displayed correctly in Results sidebar.
        shared.results.clickTab()
        shared.results.clickOnFirstRowOfTable()
        test.log("For now just getting the accession number from the sidebar for Results")
        test.log("Confirming that the sidebar Accession Number is the same as the first row Accession Number.")
        shared.results.confirmSideBarAccessionNumber(shared.results.table_data[0]["Accession #"])
        
        #31. Double-click on one of the STAT samples in the Results Queue list for review.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.doubleClickReleasedSampleRow()        
        #Confirm the Review page displays.            
        shared.results.confirmReviewPage()

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
