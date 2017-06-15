# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables

class ConsumableHistoryTab(Tables):
    
    def __init__(self):
        self.object_symbol = ":Bloodhound 1.Consumable History_TabProxy"
        self.start_month_textfield_symbol = ":Consumable History.Start:_JTextField"
        self.start_day_textfield_symbol = ":Consumable History./_JTextField"
        self.start_year_textfield_symbol = ":Consumable History./_JTextField_2"
        self.end_month_textfield_symbol = ":Consumable History.End:_JTextField"
        self.end_day_textfield_symbol = ":Consumable History./_JTextField_3"
        self.end_year_textfield_symbol = ":Consumable History./_JTextField_4"
        self.search_button_symbol = ":Consumable History.Search_JButton"
        self.export_digimac3_stain_pack_button_symbol = ":Consumable History.Export DigiMAC3™ Stain Pack_JButton"
        self.export_digiwash_solution_button_symbol = ":Consumable History.Export DigiWash™ Solution_JButton"
        self.export_digiclean_solution_button_symbol = ":Consumable History.Export DigiClean™ Solution_JButton"
        self.consumable_history_report_button_symbol = ":Consumable History.Print_JButton"
        
        self.digimac3_stain_pack_table_symbol = ":Consumable History_JTable_2"
        self.digiwash_solution_table_symbol = ":Consumable History_JTable_3"
        self.digicleansolution_table_symbol = ":Consumable History_JTable"
        self.digimac3_reticulocyte_table_symbol = ":Consumable History_JTable_4"
        
    def clickTab(self):
        clickTab(self.object_symbol)
        
    def confirmDateWidget(self):
        start_month = findObject(self.start_month_textfield_symbol)
        start_day = findObject(self.start_day_textfield_symbol)
        start_year = findObject(self.start_year_textfield_symbol)
        end_month = findObject(self.end_month_textfield_symbol)
        end_day = findObject(self.end_day_textfield_symbol)
        end_year = findObject(self.end_year_textfield_symbol)
        
        test.verify(start_month.enabled == True, "Confirm that the start month edit field exists and is enabled by default")
        test.verify(start_day.enabled == True, "Confirm that the start day edit field exists and is enabled by default")
        test.verify(start_year.enabled == True, "Confirm that the start year edit field exists and is enabled by default")
        test.verify(start_month.enabled == True, "Confirm that the end month edit field exists and is enabled by default")
        test.verify(start_day.enabled == True, "Confirm that the end day edit field exists and is enabled by default")
        test.verify(start_year.enabled == True, "Confirm that the end year edit field exists and is enabled by default")
        
    def clickSearchButton(self):
        clickButton(self.search_button_symbol)
        
    def clickExportDigiMac34StainPackButton(self):
        clickButton(self.export_digimac3_stain_pack_button_symbol)
        
    def clickExportDigiWashSolutionButton(self):
        clickButton(self.export_digiwash_solution_button_symbol)
        
    def clickExportDigiCleanSolutionButton(self):
        clickButton(self.export_digiclean_solution_button_symbol)
        
    def clickConsumableHistoryReportButton(self):
        clickButton(self.consumable_history_report_button_symbol)
        
    def confirmDigiCleanSolutionTableData(self,lot_number):
        self.confirmARowOfTableData()

    def confirmDigiMacTableData(self,lot_number):
        self.confirmARowOfTableData(self.digimac3_stain_pack_table_symbol,lot_number)
        
    def confirmDigiWashTableData(self,lot_number):
        self.confirmARowOfTableData(self.digiwash_solution_table_symbol,lot_number)
        
    def confirmDigiCleanSolutionTableData(self,lot_number):
        self.confirmARowOfTableData(self.digicleansolution_table_symbol,lot_number,"---")
        
    def confirmARowOfTableData(self,table_symbol,lot_number,install_date = ""):
        Tables.populateTableData(self,table_symbol)
        table_data = Tables.getTableData(self)
        
        if (install_date == "---"):
            test.verify(table_data[0]['Install\nDate'] == "---","Confirm that the Install Date column contains ---")
        else:
            test.verify(datetime.strptime(table_data[0]['Install\nDate'],'%m/%d/%y').day > 0,"Confirm that the Install Date column contains ---")
            
        test.verify(table_data[0]['Lot\nNumber'] == lot_number, "Confirm that the expected lot number: " + lot_number + " is equal to the actual lot number: " + table_data[0]['Lot\nNumber']) 
        test.verify(datetime.strptime(table_data[0]['Exp Date\n(Open)'],'%m/%d/%y').day > 0, "Confirm that the Exp Date (Open) column contains a real date")
        test.verify(datetime.strptime(table_data[0]['Exp Date\n(Closed)'],'%m/%d/%y').day > 0, "Confirm that the Exp Date (Closed) column contains a real date")
        test.verify(table_data[0]['Tech ID'] == "Vadim", "Confirm that the Tech ID column contains the name Vadim")
    
    def accessionToLotNumber(self,accession_number):
        test.log("Get the accession number up to and including the X to get the lot number")
        lot_number = accession_number.split("X")[0] + "X"
        test.log("Remove the first letter of the accession number to get the lot number")
        lot_number = lot_number.replace(lot_number[:1],'')
        return lot_number
    
    def confirmDigiCleanSolutionHeaders(self):
        expected_headers = ['Install\nDate', 'Lot\nNumber', 'Exp Date\n(Open)', 'Exp Date\n(Closed)', 'Tech ID']
        self.confirmHeaders(self.digicleansolution_table_symbol,expected_headers)

    def confirmDigiMac3StainPackHeaders(self):
        expected_headers = ['Install\nDate', 'Lot\nNumber', 'Exp Date\n(Open)', 'Exp Date\n(Closed)', 'Tech ID']
        self.confirmHeaders(self.digimac3_stain_pack_table_symbol,expected_headers)
        
    def confirmDigWashSolutionHeaders(self):
        expected_headers = ['Install\nDate', 'Lot\nNumber', 'Exp Date\n(Open)', 'Exp Date\n(Closed)', 'Tech ID']
        self.confirmHeaders(self.digiwash_solution_table_symbol,expected_headers)
        
    def confirmDigiMac3ReticulocyteHeaders(self):
        expected_headers = ['Install\nDate', 'Lot\nNumber', 'Exp Date\n(Open)', 'Exp Date\n(Closed)', 'Tech ID']
        self.confirmHeaders(self.digimac3_reticulocyte_table_symbol,expected_headers)  
        
    def confirmHeaders(self,table_symbol, expected_headers):
        headers = Tables.getHeaders(self,table_symbol)
        
        test.verify(len(expected_headers) == len(headers), "Confirm that the table header contains the expected number of columns")
        
        counter = 0
        for header in headers:
            test.verify(header == expected_headers[counter], "Confirm that the expected header: " + expected_headers[counter] + " is equal to the actual header " + header)
            counter += 1  
