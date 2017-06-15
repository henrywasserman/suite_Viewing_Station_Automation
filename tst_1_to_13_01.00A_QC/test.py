# -*- coding: utf-8 -*-
import shutil
import sys
import os
import exceptions
import traceback

def main():
    
    try:
        step_counter = 1
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        
    #1. Log out of and exit out of the Viewing Station, bring it up again and login with a username with admin rights and navigate to the QC tab
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared = Startup("QC_LARGE_DATA_SET_ATTACH")
        
    #    shared = Startup("ATTACH_TO_RUNNING_STATION")
    #    shared.qcoverview.clickTab()
        
        shared.system.mountUSBDrive()
        #shared.setConfigLisReleaseDelay(6)
    
    #Confirm the QC tab is defaulted to the "Overview" subtab
        shared.qcoverview.overviewDefaultTest()        
    #"Confirm there are 5 subtabs down the left hand side: 
    #- ""Overview""
    #- ""DigiCount™""
    #- ""Population""
    #- ""Reproducibility""
    #- ""Whole Blood"""
        shared.qcoverview.confirm5SubTabs()        
    #Confirm there is an Analyzer Selector combobox in the toolbar
        shared.qctab.confirmAnalyzerSelector()        
    #Confirm there is a "Print" button (grayed out disabled) in the toolbar        [VM 12.16.13]
        shared.qcoverview.confirmPrintGrayedOut()
    #Confirm that under the "New control on <analyzer>" header in the toolbar the following buttons are displayed; "DigiCount™", "Reproducibility" and "Whole Blood"
        shared.qctab.confirmQCButtons()        
    #"Confirm that on the right side of the toolbar is the ""Reflag all"" button
        shared.qcoverview.confirmReflagAllButton()
    #NOTE: This button only is displayed in the QC > Overview page"        
         
        #Confirm the following buttons are displayed in the Overview toolbar: 
        #-"DigiCount™ "
        #-"Reproducibility"
        #-"Whole Blood"
        #-"Reflag all"
        shared.qctab.confirmQCButtons()
        shared.qctab.confirmReFlagButtonEnabled()
        
        #2. Navigate to QC > DigiCount™  subtab and view the tab across the top of the screen
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.clickTab()
        
        #"Confirm there are 5 tabs across the top of the DigiCount™ tab:
        #-“Low”
        #-“Normal”
        #-“High"
        #-“All” 
        #-“Table”
        shared.digicounttab.confirm5SubTabs()
        
        #"3. Click on following tabs and view the toolbar; “Low”, “Normal”, “High”, “All”
        test.log("Step #" + str(step_counter)); step_counter += 1
        #NOTE: The following toolbar elements listed are in addition to the ones already specified in the previous test"        
        #Confirm that each tab goes to the “Low”, “Normal”, “High” and “All” graph pages        
        #Confirm that the toolbar has a "Control Selector" combobox        
        #Confirm that the toolbar has Control Details text under the Control selector combobox and Control Status text to the right of the combobox        
        #Confirm that the toolbar has an unchecked "Include History" checkbox        
        #Confirm that the toolbar has an active "Exclude" button        
        #"Confirm that there are ""+"" and ""-"" zoom buttons under the graphs
        #NOTE: These buttons should only appear under graphs"
        shared.digicounttab.confirmButtonFunctionality(["Low","Normal","High","All"])        
    
        #4. In any of the graph pages click on the "Exclude" button, when the exclude dialog is displayed (with the pointer focusing on one point on the graph) click on the "Exclude Result" checkbox, enter a comment in the comment field and click on the "Save" button        
        #Confirm that the exclude dialog closes and the point that was highlighted is excluded
        test.log("Step #" + str(step_counter)); step_counter += 1
        control = shared.digicounttab.getSelectedControlItem()
        shared.digicounttab.clickExcludeButton()
        shared.digicounttab.excludedialog.clickExcludeResultCheckbox()
        shared.digicounttab.excludedialog.enterCommentText("A comment in the comment field")
        shared.digicounttab.excludedialog.clickSaveButton()
        graph_data = shared.digicounttab.getAllGraphData("WBC")
        total_points_on_line = len(graph_data[control + "L"]["WBC"]["Low"])
        test.verify(graph_data[control + "L"]["WBC"]["Low"][total_points_on_line - 1]["excluded"] == True, "Confirm that the last data point in the WBC Low graph has been excluded")
        
        #5. In any of the graph pages click on the "Include History" checkbox to put a check in it and then click on the checkbox again to uncheck it        
        #Confirm that, when checked, all the points for all the controls for that level are displayed in one graph        
        #Confirm that when unchecked it goes back to displaying the set of points from the selected control
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.confirmHistoryCheckboxFunctionality()
        
        #6. In any of these graph pages click on the Control Selector combobox and select a several different controls        
        #Confirm that a graph is displayed for any control selected
        test.log("Step #" + str(step_counter)); step_counter += 1   
        shared.digicounttab.confirmAllControlsIncludedOnGraphOrTable()
        shared.digicounttab.confirmChangingControlChangesData()
        
        #"7. Click on the ""Table"" tab and view the toolbar
        #NOTE: The following toolbar elements listed are in addition to the ones already specified in the previous tests"        
        #Confirm that it goes to the "Table" page        
        #Confirm that the toolbar has an active "Export" button        
        #Confirm that the toolbar has an active "Activate/Edit" button        
        #Confirm that the toolbar has an inactive "Exclude" button        
        #Confirm that there are NO "+" and "-" zoom buttons under the table
        test.log("Step #" + str(step_counter)); step_counter += 1        
        shared.digicounttab.confirmButtonFunctionality(["Table"])
    
        #8. In any of the DigiCount™ tabs (“Low”, “Normal”, “High”, “All” or Table) view the messages next to and below the Control Selector combobox        
        #"Confirm there are existing messages on the toolbar, reporting the Active or Inactive status of the control sample and date and time of its status.
        #Note: The text that appears in these places is specific to the control type."        
        #Confirm that the Analyzer selector combobox list includes only all the analyzers connected to the Control Viewing Station you are logged on.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.digicounttab.confirmLabelFunctionality(["Low","Normal","High","All","Table"])
        shared.digicounttab.confirmAnalyzerSelector(shared.qc_server)
    
        #9. Navigate to QC > Population subtab and review the toolbar for actions that can be performed.
        test.log("Step #" + str(step_counter)); step_counter += 1    
        #"Confirm that the following buttons/functionality (click on each button and review the result) are available on the Population tab:
        shared.populationtab.clickTab() 
        #-Analyzer selector combobox
        shared.qctab.confirmAnalyzerSelector()
        #-""Print"" button (currently  disabled)
        #-""DigiCount"", ""Reproducibility"", and ""Whole Blood"" buttons
        #-""Exclude"" button
        shared.populationtab.confirmButtonFunctionality()
        #-""Zoom"" buttons at the bottom of the graph that adjusts the scrollbar when pressed"        [VM 12.16.13]
        shared.populationtab.confirmPlusButtonIncreasesGraphScale()
        shared.populationtab.confirmMinusButtonDecreasesGraphScale()
        #Confirm that the Population graph is displayed properly by running a sample to completion and verifying the new data points on the graph.
        shared.populationtab.confirmGraphHasPoints()        
        #Confirm that the "Exclude" button is active ( disabled unless a data point is selected). Test its functionality by pressing the button to display the Exclude dialog. Check the Exclude Population Batch checkbox. Enter a reason in the text field and press the "Save" button.        [VM 12.16.13]
        shared.populationtab.excludeButtonClick()
        shared.populationtab.excludedialog.confirmDialogAppears()
        shared.populationtab.excludedialog.clickExcludePopulationBatchCheckbox()
        shared.populationtab.excludedialog.enterPopulationCommentText("exclude population comments")
        shared.populationtab.excludedialog.clickSaveButton()
        #Confirm upon reopening the Exclude dialog that the display is unchanged, the "Save" button is disabled, and the entered reason text is uneditable. Click Cancel button in Exclude Dialog box.        [VM 12.16.13]
        shared.populationtab.excludeButtonClick()
        shared.populationtab.excludedialog.confirmPopulationExcludeDialogStatus()
        
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
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
        