# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import string

class ConfigurationGeneralTab:
    
    def __init__(self):
        self.region_section_symbol = ":General.Region_JLabel"
        self.system_section_symbol = ":General.System_JLabel"
        self.results_section_symbol = ":General.Results_JLabel"
        self.upgrade_differential_level_section_symbol = ":General.Upgrade Differential Level_JLabel"
        self.slides_section_symbol = ":General.Slides_JLabel"
        self.print_reports_section_symbol = ":General.Print Reports_JLabel"
        self.language_listbox_symbol = ":General. _JComboBox"
        self.date_format_listbox_symbol = ":General. _JComboBox_2"
        self.time_format_am_pm_radiobutton_symbol = ":General.AM/PM_JRadioButton"
        self.daylight_saving_time_checkbox_symbol = ":General.Enable_JCheckBox"
        self.numberformat_radiobutton1_symbol = ":General.1,234.56_JRadioButton"
        self.auto_logout_time_symbol = ":General_JTextField_2"
        self.lis_release_delay_symbol = ":General_JTextField"
        self.screensaver_timeout = ":General_JTextField_3"
        self.turn_around_time_warning_symbol = ":General_JTextField_4"
        self.show_unordered_results_checkbox_symbol = ":General.Enable_JCheckBox_2"
        self.auto_release_unflagged_samples_listbox_symbol = ":General. _JComboBox_6"
        self.allow_viewing_unreportable_results_checkbox_symbol = ":General.Enable_JCheckBox_3"
        self.for_samples_with_many_all_radiobutton_symbol = ":General.All_JRadioButton"
        self.for_samples_with_many_partial_editbox_symbol = ":General_JTextField_5"
        self.discard_images_from_unflagged_editbox_symbol = ":General_JTextField_6"
        self.discard_images_from_flagged_editbox_symbol = ":General_JTextField_7"
        self.maximum_Number_of_historical_editbox_symbol = ":General_JTextField_8"
        self.require_authentication_checkbox_symbol = ":General.Enable_JCheckBox_4"
        self.when_cells_are_viewed_listbox_symbol = ":General. _JComboBox_7"
        self.when_morphology_is_entered_listbox_symbol = ":General. _JComboBox_8"
        self.accession_number_listbox_symbol = ":General_JComboBox"
        self.slide_id_listbox_symbol = ":General_JComboBox_2"
        self.slide_text_test_date_time_listbox_symbol = ":General_JComboBox_3"
        self.slide_text_blank_listbox_symbol = ":General_JComboBox_4"
        self.retain_slides_all_samples_radiobutton_symbol = ":General.All Samples_JRadioButton"
        self.retain_slides_onlyFlaggedSamples_radiobutton_symbol = ":General.Only Flagged Samples_JRadioButton"
        self.slides_per_sample_editbox_symbol = ":General_JTextField_9"
        self.print_slide_index_sheet_enable_checkbox = ":General.Enable_JCheckBox_3"
        self.display_slide_label_corrections_checkbox = ":General.Enable_JCheckBox_4"
        self.lab_report_print_all_symbol = ":General.Lab Report_JRadioButton"
        self.lab_report_print_by_exception_symbol = ":General.Lab Report_JRadioButton_2"
        self.lab_report_print_none_symbol = ":General.Lab Report_JRadioButton_3"
        self.patient_report_print_all_symbol = ":General.Patient Report_JRadioButton"
        self.patient_report_print_by_exception_symbol = ":General.Patient Report_JRadioButton_2"
        self.patient_report_print_none_symbol = ":General.Patient Report_JRadioButton_3"
        self.digicount_qc_report_print_all_symbol = ":General.DigiCount™ QC Report_JRadioButton"
        self.digicount_qc_report_print_by_exception_symbol = ":General.DigiCount™ QC Report_JRadioButton_2"
        self.digicount_qc_report_print_none_symbol = ":General.DigiCount™ QC Report_JRadioButton_3"
    
    def clickTab(self):
        clickTab(waitForObject(":Configuration.General_TabProxy"))
        
    def setLISReleaseDelay(self,timeout):
         mouseClick(waitForObject(":General_JTextField"), 32, 15, 0, Button.Button1)
         type(waitForObject(":General_JTextField"), timeout)
         clickButton(":Configuration.Save_JButton")
         
    def confirmSections(self):
        region_section = findObject(self.region_section_symbol)
        system_section = findObject(self.system_section_symbol)
        results_section = findObject(self.results_section_symbol)
        upgrade_differential_section = findObject(self.upgrade_differential_level_section_symbol)
        slides_section = findObject(self.slides_section_symbol)
        print_reports_section = findObject(self.print_reports_section_symbol)
        
        test.verify(region_section.text == "Region", "Confirm that the Region section text is Region")
        test.verify(system_section.text == "System","Confirm that the System section text is System")
        test.verify(results_section.text == "Results","Confirm that the Results section text is Results")
        test.verify(upgrade_differential_section.text == "Upgrade Differential Level","Confirm that the Upgrade Differential Level section text is Upgrade Differential Level")
        test.verify(slides_section.text == "Slides","Confirm that the Slides section text is Slides")
        test.verify(print_reports_section.text == "Print Reports","Confirm that the Print Reports section text is Print Reports")
        
    def confirmDefaultRegionSection(self):
        language = findObject(self.language_listbox_symbol)
        date_format = findObject(self.date_format_listbox_symbol)
        time_format = findObject(self.time_format_am_pm_radiobutton_symbol)
        daylight_savings = findObject(self.daylight_saving_time_checkbox_symbol)
        number_format = findObject(self.numberformat_radiobutton1_symbol)
        
        test.verify(str(language.selecteditem) == "English", "Confirm that the default Language is English")
        test.verify(str(date_format.selecteditem) == "6/15/11 - English (United States)")
        test.verify(time_format.text == "AM/PM", "Confirm that the time format default is AM/PM")
        test.log("TODO This has been removed from the application.  Just need to find out if that is per spec")
        #test.verify(daylight_savings.selected == True,"Confirm that Daylight Savings Time is Enabled by default")
        test.verify(number_format.selected == True, "Confirm that Number Format 1,234.56 is selected by default")
        
    def confirmDefaultSystemSection(self):
        auto_logout =findObject(self.auto_logout_time_symbol)
        lis_release_delay = findObject(self.lis_release_delay_symbol)
        screensaver_timeout = findObject(self.screensaver_timeout)
        turn_around = findObject(self.turn_around_time_warning_symbol)        

        test.verify(auto_logout.value.toString() == "0.0", "Confirm that the Auto-Logout Time value is 0")
        test.verify(lis_release_delay.value.toString() == "15.0", "Confirm that the LIS Release Delay value is 15")
        test.verify(screensaver_timeout.value.toString() == "0.0", "Confirm that the Screensaver Timeout value is 0")
        test.verify(turn_around.value.toString() == "999.0", "Confirm that the Turn-Around Time Warning value is 999")
        
    def confirmDefaultResultsSection(self):
        show_unordered = findObject(self.show_unordered_results_checkbox_symbol)
        auto_release = findObject(self.auto_release_unflagged_samples_listbox_symbol)
        allow_viewing = findObject(self.allow_viewing_unreportable_results_checkbox_symbol)
        all_radiobutton = findObject(self.for_samples_with_many_all_radiobutton_symbol)
        partial_editbox = findObject(self.for_samples_with_many_partial_editbox_symbol)
        unflagged_editbox = findObject(self.discard_images_from_unflagged_editbox_symbol)
        flagged_editbox = findObject(self.discard_images_from_flagged_editbox_symbol)
        historical_editbox = findObject(self.maximum_Number_of_historical_editbox_symbol)
        require_authentication = findObject(self.require_authentication_checkbox_symbol)
        
        test.verify(show_unordered.selected == False, "Confirm that the ShowUnordered Results check box is not checked")
        test.verify(str(auto_release.selecteditem) == "None", "Confirm that the Auto-Release Unflagged Samples list box default item is None")
        test.verify(allow_viewing.selected == False, "Confirm that the AllowViewing Unreportable Results checkbox is not checked")
        test.verify(all_radiobutton.selected == True, "Confirm that the For Samples with many ... All radio button is selected")
        test.verify(partial_editbox.text == "200", "Confirm that the Partial text box contains 200")
        test.verify(unflagged_editbox.text == "730", "Confirm that the Discard Images from Unflagged... edit box contains 730")
        test.verify(flagged_editbox.text == "730", "Confirm that the Discard Images from Flagged... edit box contains 730")
        test.verify(historical_editbox.text == "2", "Confirm that the Maximum Number of Historical Results Displayed edit box is 2")
        test.verify(require_authentication.selected == False, "Confirm that the Require Authentication for Release checkbox is not checked")
        
    def confirmDefaultUpgradeDifferentialLevelSection(self):
        when_cell_viewed = findObject(self.when_cells_are_viewed_listbox_symbol)
        when_morphology_entered = findObject(self.when_morphology_is_entered_listbox_symbol)
        
        #In this case 'Autodiff is displayed as None'
        test.verify(str(when_cell_viewed.selecteditem) == "Autodiff", "Confirm When Cells are Viewed: None")
        test.verify(str(when_morphology_entered.selecteditem) == "Autodiff", "Confirm When Morphology is Entered: None")
        
    def confirmDefaultSlidesSection(self):
        accession_number = findObject(self.accession_number_listbox_symbol)
        slide_id = findObject(self.slide_id_listbox_symbol)
        test_date_time = findObject(self.slide_text_test_date_time_listbox_symbol)
        blank = findObject(self.slide_text_blank_listbox_symbol)
        
        all_samples = findObject(self.retain_slides_all_samples_radiobutton_symbol)
        only_flagged = findObject(self.retain_slides_onlyFlaggedSamples_radiobutton_symbol)
        
        slides_per_sample = findObject(self.slides_per_sample_editbox_symbol)
        print_slide_index = findObject(self.print_slide_index_sheet_enable_checkbox)
        display_slide_label = findObject(self.display_slide_label_corrections_checkbox)
        
        test.verify(str(accession_number.selecteditem) == "Accession number","Confirm Slide Text combobox 1: Accession Number selected by default")
        test.verify(str(slide_id.selecteditem) == "Slide ID","Confirm Slide Text combobox 2: Slide ID selected by default")
        test.verify(str(test_date_time.selecteditem) == "Test date/time","Confirm Slide Text combobox 3: Test Date/Time selected by default")
        test.verify(str(blank.selecteditem) == "(Blank)","Confirm Slide Text combobox 4: (Blank) selected by default")
        test.verify(all_samples.text == "All Samples","Confirm Retain Slides radio button group: All Samples (selected by default), Only Flagged Samples")
        test.verify(all_samples.selected == True,"Confirm Retain Slides radio button group: All Samples (selected by default), Only Flagged Samples")
        test.verify(only_flagged.text == "Only Flagged Samples","Confirm Flagged Samples not selected")
        test.verify(only_flagged.selected == False,"Confirm Flagged Samples not selected")
        test.verify(slides_per_sample.text == "1","Confirm Slides Per Sample: 1")
        test.verify(print_slide_index.selected == False,"Confirm Print Slide Index Sheet checkbox: (unchecked)")
        test.verify(display_slide_label.selected == False,"Confirm Display slide label corrections checkbox: (unchecked)")
        
    def confirmDefaultPrintReportsSection(self):
        lab_report_print_all = findObject(self.lab_report_print_all_symbol)
        patient_report_print_by_exception = findObject(self.lab_report_print_by_exception_symbol)
        digicount_print_none = findObject(self.lab_report_print_none_symbol)
        lab_report__print_all = findObject(self.patient_report_print_all_symbol)
        patient_report__print_by_exception = findObject(self.patient_report_print_by_exception_symbol)
        digicount__print_none = findObject(self.patient_report_print_none_symbol)
        lab_report__print_all = findObject(self.digicount_qc_report_print_all_symbol)
        patient_report__print_by_exception = findObject(self.digicount_qc_report_print_by_exception_symbol)
        digicount__print_none = findObject(self.digicount_qc_report_print_none_symbol)
        
        test.verify(lab_report_print_all.selected == False,"Confirm Lab Report Print All not selected")
        test.verify(patient_report_print_by_exception.selected == False,"Confirm Lab Report Print by Exception not selected")
        test.verify(digicount_print_none.selected == True,"Confirm Lab Report: Print None selected")
        test.verify(lab_report__print_all.selected == False,"Confirm Patient Report Print All not selected")
        test.verify(patient_report__print_by_exception.selected == False,"Confirm Patient Report Print By Exception not selected")
        test.verify(digicount__print_none.selected == True,"Confirm Patient Report: Print None selected")
        test.verify(lab_report__print_all.selected == False,"Confirm Digicount Print All not selected")
        test.verify(patient_report__print_by_exception.selected == False,"Confirm Digicount Print by Exception not selected")
        test.verify(digicount__print_none.selected == True,"Confirm Daily QC Report: Print None selected")