# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    
    try: 
        test.log("QC Population SubTab")
    
        step_counter = 57
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup('QC_MEDIUM_DATA_SET')
        
        #QC > Population subtab
        
        #57. Go to QC > Population
        #Confirm only a graph page is displayed
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.populationtab.clickTab()
    
        #Confirm only a graph page is displayed
        shared.populationtab.confirmResultsInPopulationGraph()
        
        #58. Move the horizontal scrollbar at the bottom of the page to the right until you find diamond shape points            
        #Confirm all parameter graphs start with 10 unconnected diamond shaped bootstrap points            
        test.log("TODO: For now not confirming that the actual image is a diamond")
        test.log("TODO: For now I am only generating data that returns two points")
        shared.populationtab.confirmTotalGraphPoints(2)
    
        #59. For each parameter, mouse over each diamond point            
        #Confirm that the tooltip stipulates "Bootstrap 1 of 10", "Bootstrap 2 of 10", etc… up to "Bootstrap 10 of 10            
        #TODO: For now only testing with 2 data points 10 data points will still pass here.        
        #Confirm that the tooltip stipulates "Bootstrap 1 of 10", "Bootstrap 2 of 10", etc… up to "Bootstrap 10 of 10
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.populationtab.confirmBootstrapText()
        
        #60. Click the "+" button at the bottom of the page under the graph            
        #Confirm the scale of the graph increases in size
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.populationtab.confirmPlusButtonIncreasesGraphScale()
    
        #61. Click the "-" button at the bottom of the page under the graph            
        #Confirm the scale of the graph decreases in size            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.populationtab.confirmMinusButtonDecreasesGraphScale()
    
        #62. Double-click any point on the graph            
        #Confirm the Exclude dialog is displayed for that point                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.populationtab.doubleClickGraphPoint('RBC',0)
        shared.populationtab.excludedialog.confirmDialogAppears()
        
        #63. Click the "Cancel" button in the Exclude dialog            
        #Confirm the Exclude dialog closes
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.populationtab.excludedialog.clickCancelButton()
        shared.populationtab.excludedialog.confirmDialogIsDismissed()
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
