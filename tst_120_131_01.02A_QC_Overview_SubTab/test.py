# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    try:

        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        test.log("QC > Overview subtab")
    
        step_counter = 120
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        #shared = Startup("QC_MEDIUM_LARGE_DATA_SET")
        #shared = Startup("QC_MEDIUM_DATA_SET_ATTACH")
        #shared = Startup("ATTACH_TO_RUNNING_STATION")
        shared.populateFactoryDefaultTable()
                
        #120. Go to QC > Overview subtab            
        #Confirm the Overview table is displayed            
        #Confirm the table has the following column main headers; -"Analyzer", -"DigiCount™", "Population". "Reproducibility" and "Whole Blood"            
        #Confirm that under the "DigiCount™" main header are 3 column with the headers; "Low", "Normal" and "High"            
        #Confirm that if any of the cells in a row are red than the row header is red            
        #Confirm that if none of the cells in a row are red and one of them is yellow than the row header is yellow            
        #Confirm that if none of the cells in a row are red or yellow and one of them is green than the row header is green            
        #Confirm that if none of the cells in a row are red, yellow or green (that all of them are gray, meaning there is no data for that analyzer) than the row header will be gray            
        #Confirm that if one of the cells in a row displays the "Lockout" icon than the row header will have the "Lockout" icon            
        #Confirm that if none of the cells in a row displays the "Lockout" icon and one of the cells displays the "Attention" icon  than the row header will have the "Attention" icon            
        #Confirm that if none of the cells in a row displays the "Lockout" or "Attention" icon than the row header will have no icon in it            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.inprocess.clickTab()
        shared.qctab.clickTab()
        shared.qcoverview.clickTab()
        #shared.system.terminateViewingStation()
    #    test.log("Before we can start this test. We need to confirm that all colors appear in the table")
    #    while not shared.qcoverview.confirmAllColorsAreInCurrentTable():
    #        test.log("All Colors were not present, restart the test")
    #        shared.system.terminateViewingStation()
    #        shared.system.startViewingStation()
    #        shared.dismissMessageBoxes()
    #        shared.vadim.login()
    #        shared.qctab.clickTab()
    #        shared.qcoverview.clickTab()
    #        shared.waitForQCDataToFinish()
            
        #Confirm the Overview table is displayed
        shared.qcoverview.confirmTableIsDisplayed()
        #Confirm the table has the following column main headers; -"Analyzer", -"DigiCount™", "Population". "Reproducibility" and "Whole Blood"
        shared.qcoverview.confirmTableHeaders(['Analyzers','DigiCount™','Population','Reproducibility','Whole Blood'])        
        #Confirm that under the "DigiCount™" main header are 3 column with the headers; "Low", "Normal" and "High"
        shared.qcoverview.confirmDigiCountMainHeader(["Low","Normal","High"])     
        #Confirm that if any of the cells in a row are red than the row header is red
        shared.qcoverview.confirmRedRowHeader()
        #Confirm that if none of the cells in a row are red and one of them is yellow than the row header is yellow
        test.log("TODO: Going to wait until we have more control over input data before finishing this functionality.")
        #shared.qcoverview.confirmYellowRowHeader()
        #Confirm that if none of the cells in a row are red or yellow and one of them is green than the row header is green
        test.log("TODO: Going to wait until we have more control over input data before finishing this functionality.")        
        #Confirm that if none of the cells in a row are red, yellow or green (that all of them are gray, meaning there is no data for that analyzer) than the row header will be gray
        test.log("TODO: Going to wait until we have more control over input data before finishing this functionality.")        
        #Confirm that if one of the cells in a row displays the "Lockout" icon than the row header will have the "Lockout" icon
        test.log("TODO: Going to wait until we have more control over input data before finishing this functionality.")        
        #Confirm that if none of the cells in a row displays the "Lockout" icon and one of the cells displays the "Attention" icon  than the row header will have the "Attention" icon
        test.log("TODO: Going to wait until we have more control over input data before finishing this functionality.")        
        #Confirm that if none of the cells in a row displays the "Lockout" or "Attention" icon than the row header will have no icon in it
        test.log("TODO: Going to wait until we have more control over input data before finishing this functionality.")
        
        #121. Write down the number of Failure(s) and Warning(s) displayed in the cells for DigiCount™ Low, Normal, High, Population, Reproducibility and Whole Blood
        test.log("Step #" + str(step_counter)); step_counter += 1
        overview_failures_and_warnings = shared.qcoverview.recordFailuresAndWarnings()
        
        #122. Click the DigiCount™ Low cell in the Overview table for one of the analyzers
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qcoverview.clickOverviewCell(0,"low")        
        #Confirm QC > DigiCount™ > Table page is displayed for that control
        shared.digicounttab.confirmDigiCountTabIsSelected()        
        #Confirm Control combobox displays the active DigiCount Low Control
        shared.digicounttab.confirmActiveLowLabelExists()
        
        #123. Count the cells with a red background (Failures)            
        #Confirm Failure number on the Table page match the number on the Overview page
        test.log("Step #" + str(step_counter)); step_counter += 1
        digicount_failures_and_warnings = shared.digicounttab.countFailuresAndWarnings(shared.factory_defaults)
        test.verify(str(overview_failures_and_warnings[0]["Low"]["failures"]) == str(digicount_failures_and_warnings["failures"]))
        
        #124. Count the cells with a yellow background (Warnings)            
        #Confirm Warning number on the Table page match the number on the Overview page            
        #Confirm Failure and Warning numbers are displayed in the toolbar under Fail and Warn respectively. The numbers match the Overview page.            
        
        #125. Count the cells with a red and yellow background in the most recent run only            
        #Confirm that if there is at least 1 red cell in the run than the cell in the Overview table is also red            
        #Confirm that if there if NO cells in the run are red and at least 1 cell is yellow than the cell in the Overview table is also yellow            
        #Confirm that if there if NO cells in the run are red or yellow than the cell in the Overview table is green
        
        #126. Click the QC > Overview subtab            
        
        #127. Click the DigiCount™ Normal cell in the Overview table for one of the analyzers            
        #Confirm QC > DigiCount™ > Table page is displayed for that control            
        #Confirm Control combobox displays the active DigiCount Normal Control            
        #Count how many cells have a red background (Failures)            
        #Confirm Failure number on the Table page match the number on the Overview page            
        #Count how many cells have a yellow background (Warnings)            
        #Confirm Warning number on the Table page match the number on the Overview page            
        #Confirm Failure and Warning numbers are displayed in the toolbar under Fail and Warn respectively. The numbers match the Overview page.            
        
        #128. Count the cells with a red and yellow background in the most recent run only            
        #Confirm that if there is at least 1 red cell in the run than the cell in the Overview table is also red            
        #Confirm that if there if NONE cell in the run are red and at least 1 cell is yellow than the cell in the Overview table is also yellow            
        #Confirm that if there if NONE cell in the run are red or yellow than the cell in the Overview table is green            
        
        #129. Click the Overview side tab            
        
        #130. Click the DigiCount™ High cell in the Overview table for one of the analyzers            
        #Confirm QC > DigiCount™ > Table page is displayed for that control            
        #Confirm Control combobox displays the active DigiCount High Control            
        #Count how many cells have a red background (Failures)            
        #Confirm Failure number on the Table page match the number on the Overview page            
        #Count how many cells have a yellow background (Warnings)            
        #Confirm Warning number on the Table page match the number on the Overview page            
        #Confirm Failure and Warning numbers are displayed in the toolbar under Fail and Warn respectively. The numbers match the Overview page.            
        
        #131. Count the cells with a red and yellow background in the most recent run only            
        #Confirm that if there is at least 1 red cell in the run than the cell in the Overview table is also red            
        #Confirm that if there if NONE cell in the run are red and at least 1 cell is yellow than the cell in the Overview table is also yellow            
        #Confirm that if there if NONE cell in the run are red or yellow than the cell in the Overview table is green
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
    