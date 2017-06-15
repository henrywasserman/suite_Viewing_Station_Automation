# -*- coding: utf-8 -*-
import shutil
import sys
import os
import re
import exceptions
import traceback

def main():
    
    try:
    
        step_counter = 29
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        shared.setConfigLisReleaseDelay(6)
        
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
        
        #"29. Run 2 samples via Open Port mode (note down the accession numbers) and go to the In Process list once sampling has started.
        #"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        for index in range(2):
            test.log("Click on the InProcess Tab")
            shared.selectBloodhoundViewingStation()
            shared.inprocess.clickTab()
            shared.inprocess.populateTableData()
            accession_number = shared.inprocess.getTableData()[index]['Accession #']
    
            shared.inprocess.clickCreateWorkOrderButton()
            shared.inprocess.createworkorderdialog.setAccessionNumberEditBox(accession_number)
            shared.inprocess.createworkorderdialog.clickSaveButton()
        
            shared.results.clickTab()
            shared.results.populateTableData()
            shared.results.clickOnTableRowIndex(0)
        
            accession_location = shared.spritecanvas.getSampleLocationByAccessionNumber(accession_number)
            shared.spritecanvas.runSampleInOpenMode(accession_location[0],accession_location[1])
    
        #Confirm the sample is displayed in the In Process list, and it is listed as Open under the "Mode" column. There is a message on the status sidebar that reads “Open-mode sample taken by [I] at [t].”,  where [I] is the analyzer name, and [t] is the time.            
        #NOTE: Confirm for Mechanical ONLY -1 cadence for 1st sample, then 1 cadence gap cycle occurs between runs with no sampling, then another 1 cadence sample is run. This is an Analyzer SW Integration test if this test does not pass  open an Analyzer bug - and Note down this portion failed.        11/18/13 VI - NOT VS TEST    
        #STAT Drawer
        test.log("Skipping mechanical only test for simulator")            
        shared.selectBloodhoundViewingStation()
        shared.inprocess.clickTab()
        table_data = shared.inprocess.populateTableData()
        
        test_pattern = "Open\-mode sample taken by Bloodhound 1 at \d+\:\d+ [AM|PM].*"
        pat = re.compile(test_pattern)
        
        counter = 1
        for index in range(len(table_data)):
            test.verify(shared.spritecanvas.accession_numbers[index] == table_data[len(table_data) - counter]['Accession #'], "Confirm that the expected accession number " + str(shared.spritecanvas.accession_numbers[index]) + " is the same as the accession number in the inprocess table " + str(table_data[len(table_data) - counter]['Accession #']))
            test.verify(table_data[index]['Mode'] == 'Open', "Confirm that the mode is Open")
            sidebar_text = shared.inprocess.getSideBarTextByIndex(2,"")
            test.verify(pat.match(sidebar_text) != None,"Confirm that " + test_pattern + " matches sidebar text " + sidebar_text)
            counter += 1
    
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
