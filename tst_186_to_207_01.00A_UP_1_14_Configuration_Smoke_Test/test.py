# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    try:
        step_counter = 186
        
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        shared = Startup()
        
        #186. Click on Configuration main tab. The General subtab is the default display (only when you first log on to the Control Viewing Station)            
        #"Confirm Configuration tab is displayed with the following subtabs:
        #-General
        #-Users
        #-Parameters
        #-QC
        #-Rules
        #-Analyzers
        #-LIS
        #"            
        #"Confirm the following sections exist under the General tab:
        #-Region
        #-System
        #-Results
        #-Upgrade Differential Level
        #-Slides
        #-Print Reports"            
    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationtab.clickTab()
        shared.configurationtab.confirmGeneralTabIsSelected()
        
        #Confirm Configuration tab is displayed with the following subtabs:
        #-General
        #-Users
        #-Parameters
        #-QC
        #-Rules
        #-Analyzers
        #-LIS
        shared.configurationtab.confirmSubTabs()
        
        #Confirm the following sections exist under the General tab:
        #-Region
        #-System
        #-Results
        #-Upgrade Differential Level
        #-Slides
        #-Print Reports
        shared.configurationgeneraltab.confirmSections()
        
        #187. Review the default settings under the Region section            
        #"Confirm each parameters in the Region section are defaulted as so: 
        #-Language: English
        #-Date Format: 6/15/11 - English (United States)
        #-Time Format: AM/PM
        #-Daylight Savings Time: (checked)
        #-Number Format: 1,234.56"        [VM 02.27.14]    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationgeneraltab.confirmDefaultRegionSection()
        
        #188. Review the default settings under the System section            
        #"Confirm each parameters in the System section are defaulted as so: 
        #-Auto Logout Time: 0 Minutes
        #-LIS Release Delay: 15 Seconds
        #-Screensaver Timeout: 0 Minutes
        #-Turn-around Time Warning: 999 Minutes"        [VM 02.27.14]    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationgeneraltab.confirmDefaultSystemSection()
    
        #189. Review the default settings under the Results section            
        #"Confirm each parameters in the Results section are defaulted as so: 
        #-Show Unordered Results checkbox: (unchecked)
        #-Auto-release Unflagged Samples combobox: None
        #-Allow Viewing Unreportable Results checkbox: (unchecked) Enabled
        #-For Samples with many unclassified cells, require the reviewers to classify...: All (selected by default)
        #                              -Partial (shown in uneditable box): 200 Cells
        #-Discard Images from Unflagged Samples After: 730 Days
        #-Discard Images from Flagged Samples After: 730 Days
        #-Maximum Number of Historic Results Displayed: 2 Results
        #-Require Authentication for Release false checkbox: (unchecked) Enabled"        03/03-KK-Updated    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationgeneraltab.confirmDefaultResultsSection()
        
        #190. Review the default settings under the Upgrade Differential Level section            
        #"Confirm each parameters in the Upgrade Differential Level section are defaulted as so: 
        #-When Cells are Viewed: None
        #-When Morphology is Entered: None"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationgeneraltab.confirmDefaultUpgradeDifferentialLevelSection()
    
        #191. Review the default settings under the Slides section            
        #"Confirm each parameters in the Slides section are defaulted as so: 
        #-Slide Text combobox 1: Accession Number selected by default
        #-Slide Text combobox 2: Slide ID selected by default
        #-Slide Text combobox 3: Test Date/Time selected by default
        #-Slide Text combobox 4: (Blank) selected by default
        #-Retain Slides radio button group: All Samples (selected by default), Only Flagged Samples
        #-Slides Per Sample: 1
        #-Print Slide Index Sheet checkbox: (unchecked)
        #-Display slide label corrections checkbox: (unchecked)"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationgeneraltab.confirmDefaultSlidesSection()
        
        #192. Review the default settings under the Print Reports section            
        #"Confirm each parameters in the Print Reports section are defaulted as so: 
        #-Lab Report: Print None
        #-Patient Report: Print None
        #-Daily QC Report: Print None"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationgeneraltab.confirmDefaultPrintReportsSection()
    
        
        #192. Click on the QC subtab, open the DigiCount Controls sub-subtab, and look at the first table on the left side.
        #Confirm the table contains the following:
        #-The first section in the first table is labeled as "Flagging warnings"
        #- "On failure" combobox with the options "Ignore", "Attention", and "Lockout"
        #-Next, there is a section labeled in here as "Run interval warnings" with three  checkboxes for "Time to run control", "Control run overdue", and "Ready to activate" 
        #-All the checkboxes in "Run interval warnings" section are checked and "Time to run control" has "7" filled in the hours edit field, "Control run overdue" has "8" filled in the hours edit field, and "Ready to activate" has "20" filled in the runs edit field
        #-Next, there is a section labeled "Review" with the checkbox "Hold results for approval" that is unchecked
        #-The last section in this table is labeled "Measured statistics" with "Mean", "SD", "CV", "%RMSD", and "n" checkbox that are all unchecked
        
        #193. Click on the QC subtab, open the DigiCount Controls sub-subtab, and look at the first table on the left side.            
        #"Confirm the table contains the following:
        #-The first section in the first table is labeled as ""Flagging warnings""
        #- ""On failure"" combobox with the options ""Ignore"", ""Attention"", and ""Lockout"", with ""Ignore"" selected by default.
        #-Next, there is a section labeled in here as ""Run interval warnings"" with three  checkboxes for ""Time to run control"", ""Control run overdue"", and ""Ready to activate"" 
        #-All the checkboxes in ""Run interval warnings"" section are checked and ""Time to run control after"" has ""7"" filled in the hours edit field, ""Control run overdue after"" has ""8"" filled in the hours edit field, and ""Ready to activate after"" has ""20"" filled in the runs edit field
        #-Next, there is a section labeled ""Review"" with the checkbox ""Hold results for approval"" that is unchecked
        #-The last section in this table is labeled ""Measured statistics"" with ""Mean"", ""SD"", ""CV"", ""%RMSD"", and ""n"" checkbox that are all unchecked
        #"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationqctab.clickTab()
        shared.configurationdigicounttab.confirmDefaultFlaggingWarningsSection()
        shared.configurationdigicounttab.confirmDefaultRunIntervalWarningsSection()
        shared.configurationdigicounttab.confirmDefaultReviewSection()
        shared.configurationdigicounttab.confirmDefaultMeasuredStatisticsSection()
        
        #"194. The middle section of the DigiCount subtab should be labeled ""Flagging Ranges"".
        #"            
        #"Confirm the section contains the following:
        #-""Lab target range type:"" combobox with ""SD"" selected by default.
        #-""Lab target range type:"" combobox contains the following values: ""SD"", ""CV"", and ""%RMSD""
        #-""Outside manufacturer's range:"" combobox with ""Ignore"" selected by default.
        #-""Outside manufacturer's range:"" combobox contains the following values: ""Ignore"", ""Warning"", and ""Failure"".
        #-Table ""Westgard Rules"" underneath the comboboxes.
        #-Table ""Westgard Rules"" contains ""Symbol"", ""Description"", and ""Level"" columns.
        #-The ""Symbol"" column has the following values from top to bottom: ""13s"", ""22s"", ""12s""
        #-The ""Description"" column has the following values from top to bottom: ""1 at 3 times target SD"", ""2 at 2 times target SD"", and ""1 at 2 times target SD""
        #-The ""Level"" column has the following values from top to bottom: ""Failure"", ""Failure"", and ""Warning""
        #-There are ""+"" and ""-"" buttons under the table.
        #-The ""+"" button is enabled and the ""-"" button is disabled."            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationdigicounttab.confirmDefaultFlaggingRanges()
        shared.configurationdigicounttab.confirmDefaultWestgardRules()
        
        #195. The section on the right should be labeled "Historical SD Specification:"            
        #"Confirm this section has the following:
        #-Level combobox with ""Default"" selection as default value
        #-Level combobox contans values: ""Default"", ""Low"", ""Normal"", and ""High""
        #-Analyzer combobox with ""Default"" selection as default value
        #-Analyzer combobox contains values ""<Analyzer_name_1>"", ""<Analyzer_name_2>""
        #-Calculate button to the right of comboboxes
        #-Table with two columns: ""Parameter"" and ""Historical SD"" "            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationdigicounttab.confirmDefaultHistoricalSD()
    
        #196. Change the value in "Lab target range type" combobox from "SD" to "CV" in Flagging Ranges section            
        #Confirm the "Historical SD Specification:" label changes to "Historical CV Specification:"            
        #Confirm the "Historical SD" column changes to "Historical CV"            
        #Confirm the "Description" column entries change to "1 at 3 times target CV", "2 at 2 times target CV", and "1 at 2 times target CV"                
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationdigicounttab.setLabTargetRangeItem("CV")
        shared.configurationdigicounttab.confirmHistoricalLabel("Historical CV Specification:")
        shared.configurationdigicounttab.confirmHistoricalTableColumnChange('Historical\nCV')
        
        #197. Change the value in "Lab target range type" to "%RMSD"            
        #"Confirm the Flagging ranges section gets the following changes:
        #-Another section with multiple controls appears
        #-Outside lab range combobox with ""Ignore"" selection as default value
        #-Outside lab range combobox has the following values: ""Ignore"", ""Warning"", and ""Failure""
        #-Outside <editable field> % of lab range: combobox with ""Warning"" selection as default value
        #-<editable field> has ""200"" as default value
        #-Outside <editable field> % of lab range: combobox has the following values: ""Ignore"", ""Warning"", and ""Failure""
        #-Retrospective %RMSD check: combobox has ""Ignore"" selection as default value
        #- Retrospective %RMSD check: combobox has the following values ""Attention"", ""Ignore"", and ""Lockout""
        #-Lab observed specification range size: <editable field> SDs
        #-<editable field> is defaulted to 3.0
        #"        03/03-KK- 0.0 Changed to 3.0    
        #Confirm the Wetgard Rules table now has one fewer row            
        #Confirm the section on the right changes to "Standardized %RMSD Specification:"            
        #"Confirm the table in that section also changes and has now the following columns:
        #-Parameter
        #-Low
        #-Normal
        #-High"            
        #Confirm all fields in that table except "Parameter" are editable            
        #Confirm the Description column entries in Westgard Rules table changed to '1 at 2 times target %RMSD' and '2 at 3 times target %RMSD'
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationdigicounttab.setLabTargetRangeItem("%RMSD")
        shared.configurationdigicounttab.confirmRMSDDefaultControlsAndValues()
        
        #198.Navigate to Population Means sub-subtab            
        #"Confirm the table on the left contains the following columns for each Parameter type:
        #-Exclude (contains checkboxes for each listed parameter)
        #-Drift Control (contains checkboxes for each listed parameter)
        #-Parameter
        #-Exclude Low
        #-Exclude High
        #-Mean
        #-SD"            
        #"Confirm the table at the top right contains the following columns:
        # -% Change
        #-Consecutive
        #-Level"            
        #"Confirm that below the table the following is displayed:
        #-'+' and  '-' buttons (""-"" button inactive)"            
        #"Confirm the table at the bottom right corner contains the following Population settings:
        #-Warn at [value] SDs text field (set to NULL)
        #-Fail at [value] SDs text field (set to NULL)
        #-Exclusion Criteria section has two radio buttons
        #    -Exclude individual results 
        #    -Exclude entire sample (with Exclude entire sample selected)
        #-Batch Size text field where it is set to 20 sample
        #-Days to Average [value] text field (set to NULL)
        #-Alert Level set to ""Ignore""
    
        #-Alert Level has ""Lockout"", ""Attention"", ""Ignore"" options
    
        #Note: Those values are displayed if the Factory + Defaults have been selected. If another setting has been selected or manual updated have been done, these values might be different
        #
        #"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationpopulationmeanstab.clickTab()
        shared.configurationpopulationmeanstab.confirmDefaultControlsAndValues()
        
        #199. Navigate to Reproducibility tab            
        #Confirm there is a Reproducibility Test section            
        #"Confirm this section has the following controls:
        #-Number of runs in Reproducibility test <editable field> Runs
        #-<editable field> defaults to 20
        #-Alert Level combobox has ""Ignore"" selection as default
        #-Alert Level combobox has the following values: ""Lockout"", ""Attention"", and ""Ignore"""            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationreproducibilitytab.clickTab()
        shared.configurationreproducibilitytab.confirmDefaultControlsAndValues()
    
        #200. Navigate to Whole Blood tab            
        #"Confirm the table contains the following columns:
        #-Parameter
        #-Absolute
        #-Percent"            
        #"Confirm the Preferred Reference table contains the following:
        #-Analyzer combobox with ""Mean"" as the default
        #-Analyzer combobox has the following values: ""Mean"", ""Analyzer name""
        #-Mode has 3 radio buttons ""Open"", ""Rack or STAT"", and ""Either"" (where ""Either"" is the default)"            
        #"Confirm the Alert Level table contains the following options in the combobox:
        #-""Lockout""
        #-""Attention"" 
        #-""Ignore"" (default)"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationwholebloodtab.clickTab()
        shared.configurationwholebloodtab.confirmDefaultControlsAndValues()
        
        #201. Click on the Rules sub tab            
        #"Confirm the table at the left corner contains the following columns:
        #-ID
        #-Description
        #-Modified"            
        #"Confirm that below the table the following is displayed:
        #-Duplicate button"            
        #"Confirm the table at the left corner contains the following columns:
        #-ID
        #-Condition"            
        #"Confirm that below the table the following is displayed:
        #-“↑” and “↓” buttons to move the selected rule set up or down
        #-""+"" and ""-"" buttons"            
        #"Confirm the section on right side of the Rules tab contains the following sub tabs: 
        #-Messages
        #-Flags
        #-Morphology
        #-Deltas
        #-Limits 
        #-Actions"            
        #Confirm the tab bar will also contain a combobox whose text displays “Rollback…”.            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.configurationrulestab.clickTab()
        shared.configurationrulestab.confirmDefaultControlsAndValues()
    
        #202. Click on the Analyzers subtab            
        #"Confirm the table contains the following columns:
        #-Analyzer Name
        #-Control Viewing Station
        #-LIS Viewing Station"            
        #"Confirm that below the table the following is displayed:
        #-""Delete"" button (inactive)
        #-""Viewing Station's name"" text field"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.analyzerstab.clickTab()
        shared.analyzerstab.confirmDefaultControlsAndValues()
        
        #203. Click on the LIS sub tab            
        #"Confirm that the following sections are displayed:
        #-LIS General
        #-LIS ASTM
        #-LIS HL7
        #-LIS TCP / IP Connection"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.listab.clickTab()
        shared.listab.confirmDefaultControlsAndValues()
        
        #204. Review the default settings under the LIS General section            
        #"Confirm each parameters in the LIS General section are defaulted as so: 
        #-LIS Enabled checkbox: (checked)
        #-LIS Encoding combobox: NONE (selected by default)
        #-LIS Encoding combobox has the following values: NONE, ASTM, HL7
        #-LIS Download Mode checkbox: ORDER_ DOWNLOAD
        #-LIS Download Mode checkbox has the following values: ORDER_DOWNLOAD, HOST_QUERY
        #-LIS Historical Lookup checkbox: (checked)
        #-Purge Pending Orders text field: 999 days
        #-Sender ID text field: Bloodhound
        #-Receiver ID text field: LIS
        #-Mode combobox: DEBUG
        #-Mode combobox has the following values: DEBUG, PRODUCTION, TRAINING
        #"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.listab.confirmLISGeneralSectionForDefaultControlsAndValues()
    
        #205. Review the default settings under the LIS ASTM section            
        #"Confirm each parameters in the LIS ASTM section are defaulted as so: 
        #-Query Wait Time text field: 30000 milliseconds (disabled)
        #-Message Retry Count text field: 6 (disabled)
        #-Message Retry Delay text field: 1000 milliseconds (disabled)
        #-Socket Retry Count text field: 6 (disabled)
        #-Socket Retry Delay text field: 3000 milliseconds (disabled)"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.listab.confirmLIS_AST_SectionForDefaultControlsAndValues()
    
        #206. Review the default settings under the LIS HL7 section            
        #"Confirm each parameters in the LIS HL7 section are defaulted as so: 
        #-Reverse AE and AR Meanings checkbox: (checked and disabled)
        #-Retransmit on Receiver Reject checkbox: (checked and disabled)
        #-Retry Count text field: 1 (disabled)
        #-Retry Delay text field: 5000 milliseconds (disabled)
        #"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.listab.confirmLIS_HL7_SectionForDefaultControlsAndValues()
    
        #207. Review the default settings under the LIS TCP/IP Connection section            
        #"Confirm each parameters in the LIS TCP/IP Connection section are defaulted as so: 
        #-Remote address text field: local host
        #-Port text field: 3000
        #-Listen on Port text field: 2000
        #-Timeout text field: 60000 milliseconds"            
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.listab.confirmLIS_TCP_IP_Connection_SectionForDefaultControlsAndValues()
        
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()

    