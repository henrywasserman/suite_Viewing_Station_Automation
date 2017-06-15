# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

from configurationqctab import ConfigurationQCTab

class ConfigurationPopulationMeansTab(ConfigurationQCTab):
    
    def __init__(self):
        self.object_symbol = ":QC.Population Means_TabProxy"
        self.table_one_symbol = ":Population Means_JTable"
        self.table_top_right_symbol = ":Population Means_JTable_2"
        self.table_at_bottom_right_symbol = ""
        self.plus_button_symbol = ":Population Means.+_JButton"
        self.minus_button_symbol = ":Population Means.-_JButton"
        self.warn_at_textfield_symbol = ":Population Means_JTextField"
        self.fail_at_textfield_symbol = ":Population Means_JTextField_2"
        self.exclude_individual_results_radiobutton_symbol = ":Population Means.Exclude individual results_JRadioButton"
        self.exclude_entire_sample_radiobutton_sybmol = ":Population Means.Exclude entire sample_JRadioButton"
        self.batch_size_textfield_symbol = ":Population Means_JTextField_3"
        self.days_to_average_textfield_symbol = ":Population Means_JTextField_4"
        self.alert_level_listbox_symbol = ":Population Means. _JComboBox"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def confirmDefaultControlsAndValues(self):
        
        test.log("This screenshot is being take to confirm the basic location of controls on the PopulationMeans tab")
        test.vp("PopulationMeans")
        
        plus_button = findObject(self.plus_button_symbol)
        minus_button = findObject(self.minus_button_symbol)
        warn_at = findObject(self.warn_at_textfield_symbol)
        fail_at = findObject(self.fail_at_textfield_symbol)
        exclude_individual_results = findObject(self.exclude_individual_results_radiobutton_symbol)
        exclude_entire_sample = findObject(self.exclude_entire_sample_radiobutton_sybmol)
        batch_size = findObject(self.batch_size_textfield_symbol)
        days_to_average = findObject(self.days_to_average_textfield_symbol)
        alert_level = findObject(self.alert_level_listbox_symbol)
        #Confirm the table on the left contains the following columns for each Parameter type:
        #-Exclude (contains checkboxes for each listed parameter)
        #-Drift Control (contains checkboxes for each listed parameter)
        #-Parameter
        #-Exclude Low
        #-Exclude High
        #-Mean
        #-SD
        #Confirm the table at the top right contains the following columns:
        # -% Change
        #-Consecutive
        #-Level
        #Confirm that below the table the following is displayed:
        #-'+' and  '-' buttons ("-" button inactive)
        #Confirm the table at the bottom right corner contains the following Population settings:
        #-Warn at [value] SDs text field (set to NULL)
        #-Fail at [value] SDs text field (set to NULL)
        #-Exclusion Criteria section has two radio buttons
        #    -Exclude individual results 
        #    -Exclude entire sample (with Exclude entire sample selected)
        #-Batch Size text field where it is set to 20 sample
        #-Days to Average [value] text field (set to NULL)
        #-Alert Level set to "Ignore"
        #
        #Note: Those values are displayed if the Factory + Defaults have been selected. If another setting has been selected or manual updated have been done, these values might be different
        
        
        #Confirm the table on the left contains the following columns for each Parameter type:
        #-Exclude (contains checkboxes for each listed parameter)
        #-Drift Control (contains checkboxes for each listed parameter)
        #-Parameter
        #-Exclude Low
        #-Exclude High
        #-Mean
        #-SD
        table_one_headers = {'Exclude':0, 'Drift\nControl':0, 'Parameter':0, 'Exclude\nLow':0, 'Exclude\nHigh':0, 'Mean':0, 'SD':0}
        self.confirmTableHeaders(self.table_one_symbol, table_one_headers)
        
        #Confirm the table at the top right contains the following columns:
        # -% Change
        #-Consecutive
        #-Level
        table_top_right_headers = {'% Change':0, 'Consecutive':0, 'Level':0}
        self.confirmTableHeaders(self.table_top_right_symbol,table_top_right_headers)
        
        #Confirm that below the table the following is displayed:
        #-'+' and  '-' buttons ("-" button inactive)
        test.verify(plus_button.enabled == True, "Confirm that the plus button is enabled")
        test.verify(minus_button.enabled == False, "Confirm that the minus button is disabled")
        
       #Confirm the table at the bottom right corner contains the following Population settings:
        #-Warn at [value] SDs text field (set to NULL)
        #-Fail at [value] SDs text field (set to NULL)
        #-Exclusion Criteria section has two radio buttons
        #    -Exclude individual results 
        #    -Exclude entire sample (with Exclude entire sample selected)
        #-Batch Size text field where it is set to 20 sample
        #-Days to Average [value] text field (set to NULL)
        #-Alert Level set to "Ignore"
        #
        #Note: Those values are displayed if the Factory + Defaults have been selected. If another setting has been selected or manual updated have been done, these values might be different
        test.verify(warn_at.text == "","Confirm that the Warn at text field is blank by default")
        test.verify(fail_at.text == "", "Confirm that the Fail at text field is blank by default")
        test.verify(exclude_individual_results.selected == False,"Confirm that the Exclude individual results radio button is not selected by default")
        test.verify(exclude_entire_sample.selected == True, "Confirm that the Exclude entire sample radio button is selected by default")
        test.verify(batch_size.text == "20","Confirm that the Batch Size text field is set to 20 by default")
        test.verify(days_to_average.text == "", "Confirm that the Days to Average text field is blank by default")
        self.confirmSelectedItem(alert_level,"Ignore", "Alert Level")
        
