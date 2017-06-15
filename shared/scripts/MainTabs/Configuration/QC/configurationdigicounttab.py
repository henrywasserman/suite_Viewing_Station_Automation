# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from configurationqctab import ConfigurationQCTab

class ConfigurationDigicountTab(ConfigurationQCTab):
    
    def __init__(self):
        #Flagging warnings:
        self.object_symbol = ":Configuration.QC_TabProxy"
        self.on_failure_listbox_symbol = ":DigiCount™ Controls.Failed results:_JComboBox"
        self.time_to_run_control_checkbox_symbol = ":DigiCount™ Controls.Time to run control (_JCheckBox"
        self.time_to_run_control_textbox_symbol = ":DigiCount™ Controls.) after _JTextField"
        self.control_run_overdue_checkbox_symbol = ":DigiCount™ Controls.Control run overdue (_JCheckBox"
        self.control_run_overdue_textbox_symbol = ":DigiCount™ Controls.) after _JTextField_2"
        self.ready_to_activate_checkbox_symbol = ":DigiCount™ Controls.Ready to activate (_JCheckBox"
        self.ready_to_activate_textbox_symbol = ":DigiCount™ Controls.) after _JTextField_3"
        self.hold_results_for_approval_checkbox_symbol= ":DigiCount™ Controls.Hold results for approval_JCheckBox"
        self.mean_checkbox_symbol = ":DigiCount™ Controls.Mean_JCheckBox"
        self.sd_checkbox_symbol = ":DigiCount™ Controls.SD_JCheckBox"
        self.cv_checkbox_symbol = ":DigiCount™ Controls.CV_JCheckBox"
        self.percent_rmsd_checkbox_symbol = ":DigiCount™ Controls.%RMSD_JCheckBox"
        self.n_checkbox_symbol = ":DigiCount™ Controls.n_JCheckBox"
        self.flagging_warnings_label_symbol = ":DigiCount™ Controls.Flagging Warnings:_JLabel"
        self.specification_label_symbol = ":DigiCount™ Controls.Historical SD Specification:_JLabel"
        
        #Flagging Ranges:
        self.flagging_ranges_label_symbol = ":DigiCount™ Controls.Flagging Ranges:_JLabel"
        self.lab_target_range_type_listbox_symbol = ":DigiCount™ Controls.Lab target range type:_JComboBox"
        self.outside_manufacturers_range_listbox_symbol = ":DigiCount™ Controls.Outside manufacturer's range:_JComboBox"
        self.westgard_rules_table_symbol = ":DigiCount™ Controls_JTable"
        self.plus_button_symbol = ":DigiCount™ Controls.+_JButton"
        self.minus_button_symbol = ":DigiCount™ Controls.-_JButton"
        
        #%RMSD Flagging Ranges:
        self.outside_lab_range_listbox_symbol = ":DigiCount™ Controls.Outside lab range:_JComboBox"
        self.outside_percent_of_lab_range_textbox_symbol = ":DigiCount™ Controls.Outside_JTextField"
        self.outside_percent_of_lab_range_listbox_symbol = ":DigiCount™ Controls.% of lab range:_JComboBox"
        self.restrospective_percent_rmsd_check_listbox_symbol = ":DigiCount™ Controls.Retrospective %RMSD check:_JComboBox"
        self.lab_observerd_specification_range_size_textbox_symbol= ":DigiCount™ Controls.Lab observed specification range size:_JTextField"
        
        #%RMSD Table
        self.rmsd_table_symbol = ":DigiCount™ Controls_JTable_2"
        
        #Historical SD Specification:
        self.level_listbox_symbol = ":DigiCount™ Controls.Level:_JComboBox"
        self.analyzer_listbox_symbol = ":DigiCount™ Controls.Analyzer:_JComboBox"
        self.calculate_button_symbol = ":DigiCount™ Controls.Calculate_JButton"
        self.historical_table_symbol = ":DigiCount™ Controls.Historical SD Specification:_JTable"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    #Confirm the table contains the following:
    #-The first section in the first table is labeled as "Flagging warnings"
    #- "On failure" combobox with the options "Ignore", "Attention", and "Lockout"
    def confirmDefaultFlaggingWarningsSection(self):
        on_failure = findObject(self.on_failure_listbox_symbol)
        flagging_warnings_label = findObject(self.flagging_warnings_label_symbol)
        
        test.verify(flagging_warnings_label.text == "Flagging warnings:" , "Confirm The first section in the first table is labeled as 'Flagging warnings'")
        
        flagging_items = {'Ignore':0, 'Attention':0, 'Lockout':0}
        
        self.confirmListBoxItems(on_failure,flagging_items,"on failure")        
        self.confirmSelectedItem(on_failure,"Ignore", "default")

    #-Next, there is a section labeled in here as "Run interval warnings" with three  checkboxes for "Time to run control", "Control run overdue", and "Ready to activate" 
    #-All the checkboxes in "Run interval warnings" section are checked and "Time to run control" has "7" filled in the hours edit field, "Control run overdue" has "8" filled in the hours edit field, and "Ready to activate" has "20" filled in the runs edit field    
    def confirmDefaultRunIntervalWarningsSection(self):
        time_to_run_control_checkbox = findObject(self.time_to_run_control_checkbox_symbol)
        control_run_overdue_checkbox = findObject(self.control_run_overdue_checkbox_symbol)
        ready_to_activate_checkbox = findObject(self.ready_to_activate_checkbox_symbol)


        time_to_run_control_textbox = findObject(self.time_to_run_control_textbox_symbol)
        control_run_overdue_textbox = findObject(self.control_run_overdue_textbox_symbol)
        ready_to_activate_textbox = findObject(self.ready_to_activate_textbox_symbol)
        
        test.verify(time_to_run_control_checkbox.selected == True, "Confirm that the Time to run control checkbox is checked by default")
        test.verify(time_to_run_control_textbox.text == "7", "Confirm that the Time to run control hours text box is set to 7 by default")
        
        test.verify(control_run_overdue_checkbox.selected == True, "Confirm that the Control run overdue checkbox is checked by default")
        test.verify(control_run_overdue_textbox.text == "8", "Confirm that the Control run overdue text box is set to 8 by default")
        
        test.verify(ready_to_activate_checkbox.selected == True, "Confirm that the Ready to activate check box is checked by default")
        test.verify(ready_to_activate_textbox.text == "20", "Confirm that the Ready to activate text box is set to 20 by default")

    #-Next, there is a section labeled "Review" with the checkbox "Hold results for approval" that is unchecked        
    def confirmDefaultReviewSection(self):
        hold_results = findObject(self.hold_results_for_approval_checkbox_symbol)
        test.verify(hold_results.selected == False, "Confirm that the Hold results for approval checkbox is not checked by default")

    #-The last section in this table is labeled "Measured statistics" with "Mean", "SD", "CV", "%RMSD", and "n" checkbox that are all unchecked
    def confirmDefaultMeasuredStatisticsSection(self):
        mean = findObject(self.mean_checkbox_symbol)
        sd = findObject(self.sd_checkbox_symbol)
        cv = findObject(self.cv_checkbox_symbol)
        rmsd = findObject(self.percent_rmsd_checkbox_symbol)
        n = findObject(self.n_checkbox_symbol)
        
        test.verify(mean.selected == False, "Confirm that the Mean checkbox is not checked by default")
        test.verify(sd.selected == False, "Confirm that the SD checkbox is not checked by default")
        test.verify(cv.selected == False, "Confirm that the CV checkbox is not checked by default")
        test.verify(rmsd.selected == False, "Confirm that the %RMSD checkbox is not checked by default")
        test.verify(n.selected == False, "Confirm that the n checkbox is not checked by default")
        
    #193. The middle section of the DigiCount subtab should be labeled "Flagging Ranges".
    #Confirm the section contains the following:
    #-"Lab target range type:" combobox with "SD" selected by default.
    #-"Lab target range type;" combobox contains the following values: "SD", "CV", and "%RMSD"
    #-"Outside manufacturer's:" range combobox with "Ignore" selected by default.
    #-"Outside manufacturer's:" range combobox contains the following values: "Ignore", "Warning", and "Failure".
    def confirmDefaultFlaggingRanges(self):
        flagging_ranges_label = findObject(self.flagging_ranges_label_symbol)
        lab_target_range = findObject(self.lab_target_range_type_listbox_symbol)
        outside_manufacturer_range = findObject(self.outside_manufacturers_range_listbox_symbol)
        
        test.verify(flagging_ranges_label.text == "Flagging Ranges:", "Confirm that this section is labeled Flagging Ranges")
        #test.verify(str(lab_target_range.selecteditem) == "SD", "Confirm that the Lab target range type list box has SD selected by default")
        self.confirmSelectedItem(lab_target_range,"SD", "Lab target range type")
        
        flagging_range_items = {'SD':0, 'CV':0, '%RMSD':0}
        self.confirmListBoxItems(lab_target_range,flagging_range_items,"Lab target range type")
                
        #Note that the value of the Ignore item is '<null'>    
        outside_manufacturer_items = {'<null>':0, 'Warning':0, 'Failure':0}
        
        self.confirmListBoxItems(outside_manufacturer_range,outside_manufacturer_items,"Outside manufacturer's range")
        
    #-Table "Westgard Rules" underneath the comboboxes.
    #-Table "Westgard Rules" contains "Symbol", "Description", and "Level" columns.
    #-The "Symbol" column has the following values from top to bottom: "13s", "22s", "12s"
    #-The "Description" column has the following values from top to bottom: "1 at 3 SD", "2 at 2 SD", and "1 at 2 SD"
    #-The "Level" column has the following values from top to bottom: "Failure", "Failure", and "Warning"
    #-There are "+" and "-" buttons under the table.
    #-The "+" button is enabled and the "-" button is disabled.
    def confirmDefaultWestgardRules(self):
        plus_button = findObject(self.plus_button_symbol)
        minus_button = findObject(self.minus_button_symbol)
        
        westward_rules_columns = {'Symbol':0, 'Description':0, 'Level':0}
        self.confirmTableHeaders(self.westgard_rules_table_symbol,westward_rules_columns)
                    
        #TODO - In the current automation table access setup - Symbol is currently being represented as a string - so 13s is presented as '1 at 3 SD'
        # The actual graphic representation is either an image or some kind of scientific font.
        # If necessary I will go back and make this compare these images or fonts.
        expected_westward_table_data = [{'Symbol': '1 at 3 times target SD', 'Description': '1 at 3 times target SD', 'Level': 'Failure'}, {'Symbol': '2 at 2 times target SD', 'Description': '2 at 2 times target SD', 'Level': 'Failure'}, {'Symbol': '1 at 2 times target SD', 'Description': '1 at 2 times target SD', 'Level': 'Warning'}]
        self.confirmTableData(self.westgard_rules_table_symbol,expected_westward_table_data,"Westgard Rules:")
                
        test.verify(plus_button.enabled == True, "Confirm that the plus button exists and is enabled")
        test.verify(minus_button.enabled == False, "Confirm that the minus button exists and is disabled")
        
    #The section on the right should be labeled "Historical SD Specification:"
    #Confirm this section has the following:
    #-Level combobox with "Default" selection as default value
    #-Level combobox contans values: "Default", "Low", "Normal", and "High"
    #-Analyzer combobox with "Default" selection as default value
    #-Analyzer combobox contains values "<Analyzer_name_1>", "<Analyzer_name_2>"
    #-Calculate button to the right of comboboxes
    #-Table with two columns: "Parameter" and "Historical SD"
    def confirmDefaultHistoricalSD(self):
        historical_sd_spec_label = findObject(self.specification_label_symbol)
        level = findObject(self.level_listbox_symbol)
        analyzer = findObject(self.analyzer_listbox_symbol)
        calculate_button = findObject(self.calculate_button_symbol)
        table = findObject(self.historical_table_symbol)

        test.verify(historical_sd_spec_label.text == "Historical SD Specification:","Confirm the section on the right is labeled Historical SD Specification")
        self.confirmSelectedItem(level,"DigiCount™ control", "Level listbox")
        
        level_items = {'DigiCount control':0, 'Low DigiCount control':0, 'Normal DigiCount control':0, 'High DigiCount control':0}
        analyzer_items = {'Default':0, 'Bloodhound 1':0, 'Bloodhound 2':0}
        
        self.confirmListBoxItems(level,level_items,"level")
        self.confirmListBoxItems(analyzer, analyzer_items, "Analyzer")    
            
        test.verify(calculate_button.enabled == True, "Confirm that the Calculate button exists and is enabled")
                
        table_columns = {'Parameter':0, 'Historical\nSD':0}
        self.confirmTableHeaders(self.historical_table_symbol, table_columns)

    def setLabTargetRangeItem(self,item_text):
        self.setListBoxItem(self.lab_target_range_type_listbox_symbol, item_text)
        
    def setListBoxItem(self,symbol,item_text):
        list_box = findObject(symbol)
        for index in range(list_box.getItemCount()):
            if str(list_box.getItemAt(index)) == item_text:
                list_box.setSelectedIndex(index)
                break
            
    def confirmHistoricalLabel(self,expected_text):
        historical_label = findObject(self.specification_label_symbol)
        test.verify(historical_label.text == expected_text,"Confirm that the Historical label is equal to the expected text " + expected_text)
        
    def confirmHistoricalTableColumnChange(self,expected_column_name):
        table_columns = {'Parameter':0, expected_column_name:0}
        self.confirmTableHeaders(self.historical_table_symbol, table_columns)
                    
    #Confirm the Flagging ranges section gets the following changes:
    #-Another section with multiple controls appears
    #-Outside lab range combobox with "Ignore" selection as default value
    #-Outside lab range combobox has the following values: "Ignore", "Warning", and "Failure"
    #-Outside <editable field> % of lab range: combobox with "Warning" selection as default value
    #-<editable field> has "200" as default value
    #-Outside <editable field> % of lab range: combobox has the following values: "Ignore", "Warning", and "Failure"
    #-Retrospective %RMSD check: combobox has "Ignore" selection as default value
    #- Retrospective %RMSD check: combobox has the following values "Attention", "Ignore", and "Lockout"
    #-Lab observed specification range size: <editable field> SD
    #-<editable field> is defauled to 3.0
    #Confirm the Westgard Rules table now has one fewer row
    #Confirm the section on the right changes to "Standardized %RMSD Specification:"
    #Confirm the table in that section also changes and has now the following columns:
    #-Parameter
    #-Low
    #-Normal
    #-High
    #Confirm all fields in that table except "Parameter" are editable            
    def confirmRMSDDefaultControlsAndValues(self):
        outside_lab_range = findObject(self.outside_lab_range_listbox_symbol)
        outside_percent_textbox = findObject(self.outside_percent_of_lab_range_textbox_symbol)
        outside_percent_listbox = findObject(self.outside_percent_of_lab_range_listbox_symbol)
        retrospective = findObject(self.restrospective_percent_rmsd_check_listbox_symbol)
        lab_observed = findObject(self.lab_observerd_specification_range_size_textbox_symbol)
        specification_table = findObject(self.historical_table_symbol)
        
        #-Outside lab range combobox with "Ignore" selection as default value
        #-Outside lab range combobox has the following values: "Ignore", "Warning", and "Failure"
        self.confirmSelectedItem(outside_lab_range, "<null>", "Outside lab range list box")
        
        #The value of the Ignore item is <null>
        outside_lab_range_items = {'<null>':0, 'Warning':0, 'Failure':0}
        self.confirmListBoxItems(outside_lab_range, outside_lab_range_items, "")
        
        #-Outside <editable field> % of lab range: combobox with "Warning" selection as default value
        #-<editable field> has "200" as default value
        #-Outside <editable field> % of lab range: combobox has the following values: "Ignore", "Warning", and "Failure"
        self.confirmSelectedItem(outside_percent_listbox, "Warning", "Outside % of lab range")
        test.verify(outside_percent_textbox.text == "200", "Confirm that the Outside % of lab range text box contains 200 by default")
        
        outside_percent_items = {'<null>':0, 'Warning':0, 'Failure':0}
        self.confirmListBoxItems(outside_percent_listbox, outside_percent_items, "Outside percent of lab range") 
        
        #-Retrospective %RMSD check: combobox has "Ignore" selection as default value
        #- Retrospective %RMSD check: combobox has the following values "Attention", "Ignore", and "Lockout"
        self.confirmSelectedItem(retrospective, "Ignore", "Retrospective %RMSD check:")
        retrospective_items = {'Ignore':0, 'Attention':0, 'Lockout':0}
        self.confirmListBoxItems(retrospective, retrospective_items, "Retrospective %RMSD check:")
        
        #-Lab observed specification range size: <editable field> SD
        #-<editable field> is defaulted to 0.0
        test.verify(lab_observed.text == "3.0","Confirm that the Lab observed specification range size is set to 3.0 by default")
        
        #Confirm the Westgard Rules table now has one fewer row
        westgard_rules_table_data = [{'Symbol': '1 at 3 times target SD', 'Description': '1 at 3 times target %RMSD', 'Level': 'Failure'}, {'Symbol': '2 at 2 times target SD', 'Description': '2 at 2 times target %RMSD', 'Level': 'Failure'}]
        self.confirmTableData(self.westgard_rules_table_symbol, westgard_rules_table_data, "Westgard Rules:")
        
        #Confirm the section on the right changes to "Standardized %RMSD Specification:"
        test.verify(self.specification_label_symbol,"Standardized %RMSD Specification:")
        #Confirm the table in that section also changes and has now the following columns:
        #-Parameter
        #-Low
        #-Normal
        #-High
        specification_columns = {'Parameter':0, 'Low':0, 'Normal':0, 'High':0}
        self.confirmTableHeaders(self.historical_table_symbol, specification_columns)
        #Confirm all fields in that table except "Parameter" are editable
        historical_table = findObject(self.historical_table_symbol)

        for row in range(historical_table.getRowCount()):
                for column in range(historical_table.getColumnCount()):
                    #For now - column 0 is the Parameter Row
                    if column != 0:
                        test.verify(historical_table.isCellEditable(row,column) == True, "Confirm that row " + str(row) + " and column " + str(column) + " is editable")
