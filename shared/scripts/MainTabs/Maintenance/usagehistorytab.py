# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import time

from controls import Controls

class UsageHistoryTab(Controls):
    
    def __init__(self):
        self.object_symbol = ":Bloodhound 1.Usage History_TabProxy"
        self.search_button_symbol = ":Usage History.Search_JButton"
        self.export_button_symbol = ":Usage History.Export_JButton"
        self.print_usage_history_button_symbol = ":Usage History.Print_JButton"
        
        
        self.username_textfield_symbol = ":Usage History_PlaceholderOverlay"
        self.results_label_symbol = ":Usage History.Total Results (all time): 2_JLabel"
        self.results_label_2_symbol = ":Usage History.Normal/Flagged in Selected Time Period: 0/0_JLabel"
        
        self.start_month_textfield_symbol = ":Usage History.Start:_JTextField"
        self.start_day_textfield_symbol = ":Usage History./_JTextField"
        self.start_year_textfield_symbol = ":Usage History./_JTextField_2"
        
        self.end_month_textfield_symbol = ":Usage History.End:_JTextField"
        self.end_day_textfield_symbol = ":Usage History./_JTextField_3"
        self.end_year_textfield_symbol = ":Usage History./_JTextField_4"
        
        self.table_symbol = ":Usage History_JTable"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def clickSearchButton(self):
        clickButton(self.search_button_symbol)
        
    def confirmTableData(self):
        Tables.populateTableData(self,self.table_symbol)
        table_data = Tables.getTableData(self)
        
        test.verify(len(table_data) > 0, "Confirm that the usage history table contains at least one row")
        
    def confirmTableHeaders(self):
        table_headers = {'Code':0, 'Username':0, 'Timestamp':0, 'Details':0}
        Controls.confirmTableHeaders(self,self.table_symbol,table_headers)
    
    def confirmResultsLabel(self):
        results_label = findObject(self.results_label_symbol)
        results_2_label = findObject(self.results_label_2_symbol)
        
        test.verify("Total Results (all time)" in results_label.text, "Confirm that the string 'Total Results (all time)' exists in the results label " + results_label.text)
        test.verify("Normal/Flagged in Selected Time Period" in results_2_label.text, "Confirm that the string Normal/Flagged in Selected Time Period' exists in the results2 label " + results_2_label.text)
        
    def setUsername(self,shared):
        username = findObject(self.username_textfield_symbol)
        username.parent.setText(getattr(shared.vadim,"username"))

    def confirmSearchButton(self):
        search = findObject(self.search_button_symbol)
        test.verify(search.enabled == True, "Confirm that the search button exists and is enabled by default")
        
    def confirmExportButton(self):
        export = findObject(self.export_button_symbol)
        test.verify(export.enabled == True, "Confirm that the search button exists and is enabled by default")
        
    def confirmPrintUsageHistoryButton(self):
        print_usage_history = findObject(self.print_usage_history_button_symbol)
        test.verify(print_usage_history.enabled == True, "Confirm that the search button exists and is enabled by default")
        
    def confirmUsernameTextField(self):
        username = findObject(self.username_textfield_symbol)
        test.verify(username.enabled == True, "Confirm that the username text field exists and is enabled by default")
        
    def confirmDateTextFields(self):
        start_month = findObject(self.start_month_textfield_symbol)
        start_day = findObject(self.start_day_textfield_symbol)
        start_year = findObject(self.start_year_textfield_symbol)
        
        end_month = findObject(self.end_month_textfield_symbol)
        end_day = findObject(self.end_day_textfield_symbol)
        end_year = findObject(self.end_year_textfield_symbol)
        
        search_button = findObject(self.search_button_symbol)
    
        test.verify(start_month.enabled,"Confirm that the start month textfield exists and is enabled by default")
        test.verify(start_day.enabled,"Confirm that start day textfield exists and is enabled by default")
        test.verify(start_year.enabled,"Confirm that start year textfield exists and is enabled by default")
        test.verify(end_month.enabled,"Confirm that end month textfield exists and is enabled by default")
        test.verify(end_day.enabled,"Confirm that end day textfield exists and is enabled by default")
        test.verify(end_year.enabled,"Confirm that end year textfield exists and is enabled by default")
        
        test.verify(search_button.enabled, "Confirm that the search button exists and is enabled by default")

    def confirmDataRangeDefaultedToCurrentDay(self):
        start_month = findObject(self.start_month_textfield_symbol)
        start_day = findObject(self.start_day_textfield_symbol)
        start_year = findObject(self.start_year_textfield_symbol)
        
        end_month = findObject(self.end_month_textfield_symbol)
        end_day = findObject(self.end_day_textfield_symbol)
        end_year = findObject(self.end_year_textfield_symbol)

        month = time.strftime("%m")
        day = time.strftime("%d")
        year = time.strftime("%Y")
        
        test.verify(month == start_month.text, "Confirm that the start month is equal to the current month")
        test.verify(day == start_day.text, "Confirm that the start day is equal to the current day")
        test.verify(year == start_year.text, "Confirm that the start year is equal to the current year")
        test.verify(month == end_month.text, "Confirm that the end month is equal to the current month")
        test.verify(day == end_day.text, "Confirm that the end day is equal to the current day")
        test.verify(year == end_year.text, "Confirm that the end year is equal to the current year")
        