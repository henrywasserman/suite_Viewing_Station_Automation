# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    try:
        test.log("Whole Blood Graph SubTab")
    
        step_counter = 110
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup("QC_SMALL_DATA_SET")
        
        test.log("QC > Whole Blood - Graph Subtab")
        
        #"110. Go to the QC > Whole Blood > Graph, in the Analyzer Selector combobox select the appropriate Analyzer
        #NOTE: If the ""Separate by Mode"" checkbox is checked, click on it to disable it for this test"            
        #Confirm all the runs are displayed on the graph            
        #Confirm that the "+" and "-" buttons under the graph are active            
        #Confirm that there is a different colored square next to each analyzer listed            
        #Confirm that to the right of each colored square for each analyzer is a checkbox that is checked default            
        #Confirm that to the right of each checkbox is each analyzer name            
        #Confirm that to the right of the analyzer names are 2 radio buttons with the names "Absolute" and "Percent" with "Absolute" selected by default            
        #Confirm that to the right of the  "Absolute" and "Percent" radio buttons is the "Separate by Mode" checkbox with the checkbox unchecked by default            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.qctab.clickTab()
        shared.wholebloodtab.clickTab()
        shared.wholebloodtab.clickTableTab("Graph")
        #NOTE: If the ""Separate by Mode"" checkbox is checked, click on it to disable it for this test"
        shared.wholebloodtab.confirmSeparateByModeCheckBox()
        #Confirm all the runs are displayed on the graph
        shared.wholebloodtab.confirmGraphResults("wholeblood_graph_results.csv","wholeblood_table_results.csv")
        #Confirm that the "+" and "-" buttons under the graph are active
        shared.wholebloodtab.confirmPlusAndMinusButtons()        
        #Confirm that there is a different colored square next to each analyzer listed
        shared.wholebloodtab.confirmColoredSquaresAreDifferent()
        #Confirm that to the right of each colored square for each analyzer is a checkbox that is checked default
        shared.wholebloodtab.confirmCheckboxesAreCheckedByDefault()        
        #Confirm that to the right of each checkbox is each analyzer name
        shared.wholebloodtab.confirmAnalzyerNames()
        #Confirm that to the right of the analyzer names are 2 radio buttons with the names "Absolute" and "Percent" with "Absolute" selected by default
        shared.wholebloodtab.confirmRadioButtonsExist()        
        #Confirm that to the right of the  "Absolute" and "Percent" radio buttons is the "Separate by Mode" checkbox with the checkbox unchecked by default
        shared.wholebloodtab.confirmDefaultRadioButtonSelection()

        #111. Click on the "Separate by Mode" checkbox to check it            
        #Confirm that for each analyzer listed below the graph an additional line is displayed below it            
        #Confirm that the top line displays the analyzer name with “Rack and STAT” to the right of it            "(R) This should now be called “Rack and STAT”, not “Closed”
        #03/10/14 JJ - Confirm updated."
        #Confirm that the line below displays the analyzer name with "Open" to the right of it which represents the "Open Port" runs            
        #Confirm that all of the analyzer lines still have colored boxes and checkboxes next to them            
        #Confirm that the analyzer lines colored boxes are a slightly different shade from the one above it            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickSeparateByModeCheckbox()        
        #Confirm that for each analyzer listed below the graph an additional line is displayed below it
        shared.wholebloodtab.confirmAdditionalLineAdded()         
        #Confirm that the top line displays the analyzer name with “Rack and STAT” to the right of it            "(R) This should now be called “Rack and STAT”, not “Closed”
        #03/10/14 JJ - Confirm updated."
        shared.wholebloodtab.confirmTopLineDisplaysAnalizerNameWithClosed()        
        #Confirm that the line below displays the analyzer name with "Open" to the right of it which represents the "Open Port" runs
        shared.wholebloodtab.confirmBelowLineDisplaysAnalizerNameWithOpen()        
        #Confirm that all of the analyzer lines still have colored boxes and checkboxes next to them
        shared.wholebloodtab.confirmAnalyzerColoredBoxesAndCheckBoxes()   
        #Confirm that the analyzer lines colored boxes are a slightly different shade from the one above it
        shared.wholebloodtab.confirmColoredBoxColors() 

        #112. Click on all the "<Analyzer name> Closed" checkboxes to disable them            
        #Confirm only the points for the Open Port run are displayed in the graph
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickOnAllClosedCheckboxesTo("Disable") 
        #Confirm only the points for the Open Port run are displayed in the graph
        shared.wholebloodtab.confirmAllVisiblePointsAreFor("Open")
        
        #113. Click on the "<Analyzer name> Closed" checkboxes to enable them again and click on the "<Analyzer name> Open" checkboxes to disable them            
        #Confirm that only the points for the Rack and STAT runs are displayed in the graph
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickOnAllClosedCheckboxesTo("Enable")   
        shared.wholebloodtab.clickOnAllOpenCheckboxesTo("Disable")     
        #Confirm that only the points for the Rack and STAT runs are displayed in the graph
        shared.wholebloodtab.confirmAllVisiblePointsAreFor("Rack or STAT")
        
        #114. Click on the "<Analyzer name> Closed" checkboxes to disable them            
        #Confirm that no points are displayed in the graph
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickOnAllClosedCheckboxesTo("Disable")        
        #Confirm that no points are displayed in the graph
        shared.wholebloodtab.confirmAllVisiblePointsAreFor("no points")
        
        #115. Click on the "Separate by Mode" checkbox to disable it            
        #Confirm the data for each Analyzer is displayed again (no longer by Analyzer/Mode)
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickSeparateByModeCheckbox()        
        #Confirm the data for each Analyzer is displayed again (no longer by Analyzer/Mode)
        test.log("False here is so that we use the previously recorded data, nothing should have changed at this point in the data")
        shared.wholebloodtab.confirmGraphResults("wholeblood_graph_results.csv","wholeblood_table_results.csv",False)
        
        #116. Click on the checkboxes for all the analyzers to disable them            
        #Confirm the graph is blank (data and points have been removed)
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickOnAllCheckboxesTo("Disable")        
        #Confirm the graph is blank (data and points have been removed)
        shared.wholebloodtab.confirmAllVisiblePointsAreFor("no points")
        
        #117. Click on the checkbox for both Analyzer to enable them            
        #Confirm data and points are once again displayed
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickOnAllCheckboxesTo("Enable")        
        #Confirm data and points are once again displayed
        shared.wholebloodtab.confirmAllVisiblePointsAreFor("all points")
        
        #118. Click the "Percent" radio button            
        #Confirm the "Percent" radio button becomes active and the "Absolute" radio button becomes inactive            
        #Confirm the values in the row headers change from absolute to percentages            "(C) Presumably meaning the values on the y axis labels?
        #03/10/14 JJ - Updated."
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.wholebloodtab.clickPercentRadioButton()        
        #Confirm the "Percent" radio button becomes active and the "Absolute" radio button becomes inactive
        shared.wholebloodtab.confirmPercentRadioButtonIsActive()
        shared.wholebloodtab.confirmAbsoluteRadioButtonIsInactive()        
        #Confirm the values change from absolute to percentages
        shared.wholebloodtab.confirmGraphResults("wholeblood_percent_graph_results.csv","wholeblood_percent_table_results.csv")

        #119. Click the "Absolute" radio button            
        #Confirm the "Absolute" radio button becomes active and the "Percent" radio button becomes inactive            
        #Confirm the values in the row headers change from percentages to absolute            03/10/14 JJ - Updated.
        test.log("Step #" + str(step_counter)); step_counter += 1        
        shared.wholebloodtab.clickAbsoluteRadioButton()
        #Confirm the "Absolute" radio button becomes active and the "Percent" radio button becomes inactive
        shared.wholebloodtab.confirmAbsoluteRadioButtonIsActive()
        shared.wholebloodtab.confirmPercentRadioButtonIsInactive()
        #Confirm the values change from percentages to absolute
        test.log("The last parameter is a boolean for turning recording on or off")
        shared.wholebloodtab.confirmGraphResults("wholeblood_graph_results.csv","wholeblood_table_results.csv",False)        

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()


