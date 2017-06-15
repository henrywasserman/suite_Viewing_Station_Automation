# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try:
        test.log("Process The DigiCount Controls in Open Mode 2")
        
        step_counter = 39
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup('QC_SMALL_DATA_SET')
    
        #39. Go to the QC > DigiCount™ > All subtab        
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.clickTab()
        shared.digicounttab.clickAllTab()
        
        #40. Click the Control combobox. Select the control that was just run (barcode value without an L, N or H suffix)        
        #Confirm the results are reported in the DigiCount™ All graph        
        #Activate DigiCount™ Low Control
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("In this case starting as QC chooses one of two medical records so we need to grab the accession number")
        test.log("From the list box")
        accession_number = shared.digicounttab.getListBoxItems()[0]
        #Kinda redundant to select what is already selected but we may need this step later.
        shared.digicounttab.selectAccessionNumberComboBoxItem(accession_number)
        shared.digicounttab.confirmResultsInAllGraph()
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
