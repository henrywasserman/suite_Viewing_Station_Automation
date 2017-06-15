# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables

class ResultsOverview(Tables):
    
    def __init__(self):
        self.overview_sidebar_comments_symbol = ":Overview_JTextArea"
        self.overview_table_symbol = ":Overview_JTable"
        self.overview_parameter_table_symbol = ":Overview_JTable_2"
        self.dilution_numbers = {}
    
    def clickTab(self):
        clickTab(waitForObject(""))
        test.verify(True)
        
    def enterComments(self,comments):
        "First, make sure we are not adding the same text twice"
        if findObject(self.overview_sidebar_comments_symbol).text == '':
            type(findObject(self.overview_sidebar_comments_symbol),comments)

    def confirmCommentsAreNotEditable(self):
        comments = findObject(self.overview_sidebar_comments_symbol)
        test.verify(comments.editable == False, "Confirm that the Comments Text Area is not editable")        
    
    def populateParameterTableData(self):
        return Tables.populateTableData(self,self.overview_parameter_table_symbol)
        
    def setCurrentDilutionNumbers(self):
        self.dilution_numbers = {}
        table_data = self.populateCurrentTableData()
        table_data_parameters = self.populateParameterTableData()
        
        test.log("This will get the most recent run")

        
        index = self.getParameterRowNumber(table_data_parameters,'WBC (10/L)')
        self.dilution_numbers['WBC'] = table_data[index]["0"]
        
        index = self.getParameterRowNumber(table_data_parameters,'RBC (10/L)')
        self.dilution_numbers['RBC'] = table_data[index]["0"]
        
        index = self.getParameterRowNumber(table_data_parameters,'PLT (10/L)')
        self.dilution_numbers['PLT'] = table_data[index]["0"]
        
        index = self.getParameterRowNumber(table_data_parameters,'#NRBC (10/L)')
        self.dilution_numbers['#nRBC'] = table_data[index]["0"]
        
        #index = self.getParameterRowNumber(table_data_parameters,'')
        #self.dilution_numbers['#RET'] = table_data[index][key]
        
        index = self.getParameterRowNumber(table_data_parameters,'HGB (g/dL)')
        self.dilution_numbers['HGB'] = table_data[index]["0"]
        
        index = self.getParameterRowNumber(table_data_parameters,'HCT (%)')
        self.dilution_numbers['HCT'] = table_data[index]["0"]
        
    def getParameterRowNumber(self,table_data,parameter):
        
        for index in range(len(table_data)):
            if table_data[index]['Parameter'] == parameter:
                break
        
        return index
        
    def populateCurrentTableData(self):
        table_data = []
        table = squish.findObject(self.overview_table_symbol)
        table_header = table.getTableHeader()
        for row in range(table.getRowCount()):
            row_data = {}
            for column in range(table.getColumnCount()):
                header = str(column)
                row_data[header] = Tables.removeNonAscii(self,str(table.getValueAt(row,column)))
                
            table_data.append(row_data)
        
        return table_data

        
        
        
        