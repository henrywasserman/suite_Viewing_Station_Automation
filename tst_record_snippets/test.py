# -*- coding: utf-8 -*-

import shutil
import sys
import os
import __builtin__
import exceptions
import traceback


def main():
    source(findFile("scripts", "BasicFunctionality/startup.py"))
    shared = Startup("ATTACH_TO_RUNNING_STATION")
    version = shared.version

    step_counter = 10
    
    #10. Navigate to QC > Reproducibility subtab and review the toolbar for actions that can be performed.
    test.log("Step #" + str(step_counter)); step_counter += 1
    shared.reproducibilitytab.clickTab()        
    #"Confirm the following items are available on the toolbar:
    #-Analyzer selector combobox
    shared.qctab.confirmAnalyzerSelector()
    #-""Print"" button (currently grayed out disabled)
    #-""Export"" button
    #-""DigiCount"", ""Reproducibility"", and ""Whole Blood"" buttons
    #-Control selector combobox
    #-Control Details text under the Control selector combobox and the Control Status to the right of the combobox
    #-""Cancel"" button (grayed out if the control selected is completed/canceled already)
    #-""Exclude"" button ( disabled by default unless a table cell is selected)"        [VM 12.16.13]
    shared.reproducibilitytab.confirmQCButtons()
    #Confirm that the Reproducibility table is displayed properly (all parameters and results are displayed) by selecting each control under the Control selector combobox.
    shared.reproducibilitytab.confirmReproducibilityTable()
    
    #11. Navigate to QC > Whole Blood > Graph subtab
    test.log("Step #" + str(step_counter)); step_counter += 1
    shared.wholebloodtab.clickTab()    
    #"Confirm that the following buttons/functionality (click on each button and review the result) are available on the Whole Blood graph:
    #-Analyzer selector combobox
    shared.qctab.confirmAnalyzerSelector()
    #-""Print"" button (currently disabled)
    #-""DigiCount"", ""Reproducibility"", ""Whole Blood"", and ""Activate/Edit"" buttons
    #-""Exclude"" button (disabled if a point is not selected; enabled if a point is selected)
    #"        [VM 12.09.13]
    shared.wholebloodtab.confirmAllControls()
    #Confirm that the Whole Blood graph is displayed properly (all parameters and results are displayed).
    shared.wholebloodtab.confirmGraphResults("wholeblood_graph_01_00_1","wholeblood_table_01_00_1")
    #"Confirm that at the bottom of the page the following buttons/functionality (click on each button and review the result) are available:
    #-A checkbox for each Analyzer with its name labeled
    shared.wholebloodtab.confirmCheckboxForEachAnalyzer()
    #- A color box next to each Analyzer to indicate the color of the graph line
    shared.wholebloodtab.confirmColorBox()
    #-""Absolute"" and ""Percent"" radio buttons with ""Absolute"" being active by default
    shared.wholebloodtab.confirmAbsoluteAndPercentRadioButtons()
    #-A checkbox labeled ""Separate by Mode"" (unchecked by default)
    shared.wholebloodtab.confirmSeparateByModeCheckBox()
    #Confirm that clicking on the buttons or checkboxes changes the graph configurations.
    shared.wholebloodtab.confirmButtonsChangeGraphConfigurations()        
    
    #12. Navigate to QC > Whole Blood > Table tab and review the toolbar for actions that can be performed.
    test.log("Step #" + str(step_counter)); step_counter += 1
    shared.wholebloodtab.clickTableTab("Table")        
    #"Confirm that the following buttons/functionality (click on each button and review the result) are available on the Whole Blood > Table tab:
    #-Analyzer selector combobox
    shared.qctab.confirmAnalyzerSelector()
    #-""Print"" button (currently grayed out disabled)
    #-""Export"" button
    #-""DigiCount"", ""Reproducibility"", and ""Whole Blood"" buttons
    #-Control selector combobox
    #-Control Details text under the Control selector combobox and the Control Status to the right of the combobox
    #-""Close"" button (disabled if the control selected is not active)
    #-""Exclude"" button disabled by default unless a table cell is selected)"
    shared.wholebloodtab.confirmTableButtons()            
    #"Confirm that at the bottom of the page following buttons/functionality (click on each button and review the result) are available
    #-Combobox labeled ""Reference"" and defaulted to ""Mean""
    shared.wholebloodtab.confirmCombobox()
    #-""Save"" button (enabled when the selected control is active and disabled if otherwise)"
    shared.wholebloodtab.confirmSaveButton()
    
    #13. Below the Whole Blood Table click on the "Reference" combobox and select a different run in order to make it the Reference.
    test.log("Step #" + str(step_counter)); step_counter += 1
    shared.wholebloodtab.selectARun()        
    #Confirm that clicking on the combobox displays a list of choices based on the runs included in the table above.
    shared.wholebloodtab.confirmReferenceComboRuns()            
    #Confirm that selecting something other than "Mean" from the Reference selector list causes the values in the Target / Mean column to change to match the values from the Analyzer column selected.           
    #Confirm that if the user changes the reference, the table is immediately updated based on the new reference value.
    shared.wholebloodtab.confirmComboRunTargetReference()
