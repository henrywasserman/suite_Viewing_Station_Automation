# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import time

from controls import Controls

class EventLogsTab(Controls):
    
    def __init__(self):
        self.object_symbol = ":Bloodhound 1.Event Logs_TabProxy"
        self.search_button_symbol = ":Event Logs.Search_JButton"
        self.export_button_symbol = ":Event Logs.Export_JButton"
        self.print_event_log_button_symbol = ":Event Logs.Print_JButton"
        
        self.start_month_textfield_symbol = ":Event Logs.Start:_JTextField"
        self.start_day_textfield_symbol = ":Event Logs./_JTextField"
        self.start_year_textfield_symbol = ":Event Logs./_JTextField_2"
        
        self.end_month_textfield_symbol = ":Event Logs.End:_JTextField"
        self.end_day_textfield_symbol = ":Event Logs./_JTextField_3"
        self.end_year_textfield_symbol = ":Event Logs./_JTextField_4"
        
        self.table_symbol = ":Event Logs_JTable"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def clickSearchButton(self):
        clickButton(self.search_button_symbol)
        
    def clickExportButton(self):
        clickButton(self.export_button_symbol)
        
    def clickPrintEventLogButton(self):
        clickButton(self.print_event_log_button_symbol)

    def confirmSearchButton(self):
        search_button = findObject(self.search_button_symbol)
        test.verify(search_button.enabled == True, "Confirm that the search button exists and is enabled by default")
    
    def confirmExportButton(self):
        export_button = findObject(self.export_button_symbol)
        test.verify(export_button.enabled == True, "Confirm that the export button exists and is enabled by default")
    
    def confirmPrintEventLogButton(self):
        print_event_button = findObject(self.print_event_log_button_symbol)
        test.verify(print_event_button.enabled == True, "Confirm that the print event button exists and is enabled by default")
        
    #255. Observe the Event Logs tab has text fields to set the date range and a button to search for 
    #all logs in that range.
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
        
    def confirmLogDataExists(self):
        Tables.populateTableData(self,self.table_symbol)
        table_data = Tables.getTableData(self)
        test.verify(len(table_data) > 0, "Confirm that the Event Log Table contains data")
        
    def confirmTableHeaders(self):
        table_headers = {'Code':0,'Name':0,'Message':0,'Timestamp':0,'Severity':0,'Details':0}
        Controls.confirmTableHeaders(self,self.table_symbol,table_headers)
        