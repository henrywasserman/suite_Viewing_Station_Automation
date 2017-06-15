# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from controls import Controls
from digicountexcludedialog import DigiCountExcludeDialog

class QCOverview(Controls):
    
    def __init__(self):
        self.digicount_button_symbol = ":QC.DigiCount™_JButton"
        self.reproducibility_button_symbol = ":QC.Reproducibility_JButton"
        self.wholeblood_button_symbol = ":QC.Whole Blood_JButton"
        self.reflag_all_button_symbol = ":QC.Reflag all_JButton"
        self.table_object_symbol = ":Overview.Print_JTable"
        self.table_color_red = "java.awt.Color[r=254,g=126,b=126]"
        self.digicount_color_red = "java.awt.Color[r=255,g=187,b=187]"
        self.table_color_yellow = "java.awt.Color[r=255,g=220,b=113]"
        self.digicount_color_yellow = "java.awt.Color[r=255,g=238,b=170]"
        
        self.overview_tab_symbol = ":QC.Overview_TabProxy"
        self.digicount_tab_symbol = ":QC.DigiCount™_TabProxy"
        self.population_tab_symbol = ":QC.Population_TabProxy"
        self.reproducibility_tab_symbol = ":QC.Reproducibility_TabProxy"
        self.wholeblood_tab_symbol = ":QC.Whole Blood_TabProxy"

        self.table_color_green = "java.awt.Color[r=202,g=218,b=169]"
        self.table_color_gray = "java.awt.Color[r=191,g=191,b=191]"
        self.digicount_table_symbol = ":Table.Fail*_QCTable_2"
        self.wholeblood_table_symbol = ":Table_QCTable"
        self.reproducibility_table_symbol = ":Reproducibility.fail*_QCTable"
        self.reproducibility_table2_symbol = ":Reproducibility.fail*_QCTable_2"
    
        self.digicountexcludedialog = DigiCountExcludeDialog()
        
    def clickTab(self):
        clickTab(waitForObject(self.overview_tab_symbol))    
    
    def clickDigiCountButton(self):
        clickButton(self.digicount_button_symbol)
        
    def clickOverviewCell(self,row,header_text):
        header_text = header_text.lower()
        header = {"low":1,"normal":2,"high":3,"population":4,"reproducibility":5,"wholeBlood":6 }
        mouseClick(waitForObjectItem(self.table_object_symbol, str(row) + "/" + str(header[header_text])), 0, 0, 0, Button.Button1)

    def confirmTableIsDisplayed(self):
        table_data = Tables.populateTableData(self,self.table_object_symbol)
        test.log("Just looking here to see if one or more rows are being displayed")
        test.verify(len(table_data) > 0, "Confirm that the Overview Table contains at least one row.")
        
    def confirmRedRowHeader(self):
        table = findObject(self.table_object_symbol)
        test_passed = False
        
        for row_index in range(table.getRowCount()):
            if test_passed:
                break
            for column_index in range(table.getColumnCount()):
                color = self.getOverviewTableCellColor(row_index, column_index)
                test.log(color)
                
                test.log("In this case we are looking for the row header to be red.")
                test.log("If it is not red move on and look for one that is")
                if column_index == 0:
                    row_header_color = color
                    
                    if row_header_color == self.table_color_red:
                        continue
                    else:
                        break
                
                if color == self.table_color_red:
                    test.verify (row_header_color == color, "Confirm that when the row_header is red, there is at least one other cell in the row that is red")
                    test_passed = True
                    break
                
        if not test_passed:
            test.verify(False,"Test failed. Could not find red in any rows of the the columns")

            
    def confirmYellowRowHeader(self):
        table = findObject(self.table_object_symbol)
        test_passed = False
        
        row = self.findARowWithAYellowCell()
        
        while(self.isCellRed(row,0)):
            self.removeRedCellInRow(row)
            self.clickTab()
            
        for row_index in range(table.getRowCount()):
            if test_passed:
                break
            for column_index in range(table.getColumnCount()):
                snooze(1.0)
                
    def confirmAllColorsAreInCurrentTable(self):
        table = findObject(self.table_object_symbol)
        test_passed = False
        
        colors = {}
        
        for row_index in range(table.getRowCount()):
            if test_passed:
                break
            for column_index in range(table.getColumnCount()):
                colors[self.getOverviewTableCellColor(row_index, column_index)] = 0
                if len(colors) == 4:    
                    test_passed = True
                    break
                    
        return test_passed
                
    def findARowWithAYellowCell(self):
        table = findObject(self.table_object_symbol)
        test_passed = False
        
        for row_index in range(table.getRowCount()):
            if test_passed:
                break
            for column_index in range(table.getColumnCount()):
                if self.getOverviewTableCellColor(row_index, column_index) == self.table_color_yellow:
                    test_passed = True
                    row = row_index
                    break
        return row
                
    def removeRedCellInRow(self,row):
        table = findObject(self.table_object_symbol)
        excluded_cell = False
        for column in range(table.getColumnCount()):
            if excluded_cell:
                break
            
            if column == 0:
                continue
            
            if self.isCellRed(row,column):
                test.log("This click will open the appropriate table for the column")
                self.clickTableCell(row, column)
                test.log("Test to see if this is a digicount column 1,2 or 3")
                if column < 4:
                    test.log("Made it to the digicount table")
                    excluded_cell = self.excludeCell(self.digicount_table_symbol,row)
                elif column == 4:
                    test.log("Made it to the Population column")
                    excluded_cell = self.excludeCell("add population table here",row)                                
                elif column == 5:
                    test.log("Made it to the Reproducibility column")
                    excluded_cell = self.excludeCell(self.reproducibility_table_symbol,row)
                    if not excluded_cell:
                       excluded_cell = self.excludeCell(self.reproducibility_table2_symbol,row) 
                else:
                    test.log("Made it to the Wholeblood column")
                    excluded_cell = self.excludeCell(self.wholeblood_table_symbol,row)
                                
    def isCellRed(self,row,column):
        is_red = False
        color = self.getOverviewTableCellColor(row,column)
        if color == self.table_color_red:
            is_red = True
        
        return is_red
            
    def isCellYellow(self,row,column):
        is_yellow = False
        color = self.getOverviewTableCellColor(row,column)
        if color == self.table_color_yellow:
            is_yellow = True
        
        return is_yellow 
        
    def isCellGreen(self,row,column):
        is_green = False
        color = self.getOverviewTableCellColor(row,column)
        if color == self.table_color_green:
            is_green = True
        
        return is_green 
        
    def isCellGray(self,row,column):
        is_gray = False
        color = self.getOverviewTableCellColor(row,column)
        if color == self.table_color_gray:
            is_gray = True
        
        return is_gray
    
    def getDigiCountTableCellColor(self,row,column):
        table = findObject(self.digicount_table_symbol)
        table.setRowSelectionAllowed(True)
        table.setColumnSelectionAllowed(True)
        
        cell_renderer = table.getCellRenderer(row,column)
        field = cell_renderer.getClass().getSuperclass().getSuperclass().getDeclaredField("cellBackground")
        field.setAccessible(True)
        
        if column == 0:
            mouseClick(waitForObjectItem(self.digicount_table_symbol, str(row) + "/" + str(column)), 0, 0, 0, Button.Button1)
            nativeMouseClick(waitForObjectItem(self.digicount_table_symbol, str(row) + "/" + str(column)), 0, 0, 0, Button.Button1)
        else:
            table.changeSelection(row,column,True,True)
        
        cell = field.get(cell_renderer)
        if str(cell) == '<null>':
            cell = str(cell)
        else:
            cell = cell.toString()
            
        return cell

    def getWholeBloodTableCellColor(self,row,column):
        table = findObject(self.wholeblood_table_symbol)
        table.setRowSelectionAllowed(True)
        table.setColumnSelectionAllowed(True)
        table.changeSelection(row,column,True,True)
        cell_renderer = table.getCellRenderer(row,column)
        field = cell_renderer.getClass().getSuperclass().getSuperclass().getSuperclass().getDeclaredField("cellBackground")
        field.setAccessible(True)
        cell = field.get(cell_renderer)
        if str(cell) == '<null>':
            cell = str(cell)
        else:
            cell = cell.toString()
            
        return cell
    
    def getReproducibilityTableCellColor(self,row,column):
        table = findObject(self.wholeblood_table_symbol)
        table.setRowSelectionAllowed(True)
        table.setColumnSelectionAllowed(True)
        table.changeSelection(row,column,True,True)
        cell_renderer = table.getCellRenderer(row,column)
        field = cell_renderer.getClass().getSuperclass().getSuperclass().getSuperclass().getDeclaredField("cellBackground")
        field.setAccessible(True)
        cell = field.get(cell_renderer)
        if str(cell) == '<null>':
            cell = str(cell)
        else:
            cell = cell.toString()
            
        return cell
        
    def getTableCellColor(self,row,column):
        table = findObject(self.table_object_symbol)
        cell_renderer = table.getCellRenderer(row,column)
        field = cell_renderer.getClass().getSuperclass().getDeclaredField("cellBackground")
        field.setAccessible(True)
        cell = field.get(cell_renderer)
        test.log(cell.toString())
        return cell.toString()
    
    def getOverviewTableCellColor(self,row,column):
        table = findObject(self.table_object_symbol)
        cell_renderer = table.getCellRenderer(row,column)
        table.setRowSelectionAllowed(True)
        table.setColumnSelectionAllowed(True)
        table.changeSelection(row,column,True,True)
        field = cell_renderer.getClass().getSuperclass().getDeclaredField("cellBackground")
        field.setAccessible(True)
        cell = field.get(cell_renderer)
        if str(cell) == '<null>':
            cell = str(cell)
        else:
            cell = cell.toString()

        return cell.toString()

    
    def clickTableCell(self,row,column):
        mouseClick(waitForObjectItem(self.table_object_symbol, str(row) + "/" + str(column)), 96, 51, 0, Button.Button1)

    def confirmTableHeaders(self,headers):
        table = findObject(self.table_object_symbol)
        counter = 0
        for header in headers:
            if header == "DigiCount™":
                test.verify(header == str(table.getModel().getColumnGroup(counter)),"Confirm that the header " + header + " is in the table " + str(table.getModel().getColumnGroup(counter)))
                counter += 3
            else:
                test.verify(header == table.getColumnName(counter),"Confirm that the header " + header + " exists in the Overview Table: " + str(table.getColumnName(counter)))
                counter += 1
                            
    def confirmDigiCountMainHeader(self,sub_headers):
        table = findObject(self.table_object_symbol)
        for index in range(len(sub_headers)):
            test.verify(str(table.getModel().getColumnGroup(index + 1)) == "DigiCount™","Confirm that DigiCount is the name of the Column Group " + str(table.getModel().getColumnGroup(index + 1)))
            test.verify(table.getColumnName(index + 1) == sub_headers[index],"Confirm that " + sub_headers[index] + " is the name of the Column Subgroup " + table.getColumnName(index + 1))
    
    def confirm5SubTabs(self):
        test.compare(waitForObject(self.overview_tab_symbol).getText(),"Overview","Confirm the Text in the Overview Tab")
        test.compare(waitForObject(self.digicount_tab_symbol).getText(),"DigiCount™","Confirm the Text in the DigiCount™ Tab")
        test.compare(waitForObject(self.population_tab_symbol).getText(),"Population", "Confirm the Text in the Population Tab")
        test.compare(waitForObject(self.reproducibility_tab_symbol).getText(),"Reproducibility","Confirm the Text in the Reproducibility Tab")
        test.compare(waitForObject(self.wholeblood_tab_symbol).getText(),"Whole Blood", "Confirm the Text in the Whole Blood Tab.")
        
    def overviewDefaultTest(self):
        test.compare(waitForObject(self.overview_tab_symbol).selected,True,"Confirm that the QC tab is defaulted to the \"Overview\" subtab.")
                
    def confirmReflagAllButton(self):
        reflag_all_button = findObject(self.reflag_all_button_symbol)
        test.verify(reflag_all_button.enabled == True,"Confirm Reflag all Button exists and is enabled")
        
    def confirmPrintGrayedOut(self):
        test.verify(findObject(":QC.Print_JButton").enabled == False,"Confirm there is a \"Print\" button (grayed out)")
        
    def moveThroughTable(self,row,column,table_symbol):
        if row == 0 and column == 0:
            mouseClick(waitForObjectItem(table_symbol, "0/0"), 0, 0, 0, Button.Button1)
            nativeMouseClick(waitForObjectItem(table_symbol, "0/0"), 0, 0, 0, Button.Button1)

        elif column == column - 1:
            for times in column_total -1 :
                squish.nativeType("<Left>")
            squish.nativeType("<Down>")
        else:
            squish.nativeType("<Right>")

    def excludeCell(self,table_symbol,overview_row):
        table_data = Tables.populateTableData(self,table_symbol)
        column_total = len(table_data[overview_row].keys())
        cell_excluded = False
        for row in range(len(table_data)):
            if cell_excluded:
                break
            for column in range(column_total):
                self.moveThroughTable(row, column, table_symbol)
                if table_symbol == self.digicount_table_symbol: 
                    color =  self.getDigiCountTableCellColor(row, column)
                elif table_symbol == self.wholeblood_table_symbol:
                    color = self.getWholeBloodTableCellColor(row, column)
                elif table_symbol == self.reproducibility_table_symbol:
                     color = self.getReproducibilityTableCellColor(row, column)
                else:
                    test.log("Need to see what else will work at this point")
                    color = self.getDigiCountTableCellColor(row, column)
                if color == self.digicount_color_red:
                    test.log("Click on the cell")
                    mouseClick(waitForObjectItem(table_symbol, "0/0"), 0, 0, 0, Button.Button1)
                    nativeMouseClick(waitForObjectItem(table_symbol, "0/0"), 0, 0, 0, Button.Button1)
                    self.digicountexcludedialog.clickCheckbox()
                    self.digicountexcludedialog.enterComment("exclude from automation")
                    self.digicountexcludedialog.clickSaveButton()
                    cell_excluded = True
                    break
        return cell_excluded
    
    def recordFailuresAndWarnings(self):
        overview_table = []
        table = findObject(self.table_object_symbol)
        column_model = table.getTableHeader().getColumnModel()
        for row_index in range(table.getRowCount()):
            overview_row = {}
            for column_index in range(table.getColumnCount()): 
                if column_index == 0:
                    continue
                control_cell = table.getValueAt(row_index,column_index)
                
                field = control_cell.getClass().getDeclaredField("warnCount")
                field.setAccessible(True)
                warn_count = field.get(control_cell)
                
                field = control_cell.getClass().getDeclaredField("failCount")
                field.setAccessible(True)
                fail_count = field.get(control_cell)
                                
                overview_row[column_model.getColumn(column_index).getHeaderValue().toString()] = { "failures":fail_count, "warnings":warn_count }
                
            overview_table.append(overview_row.copy())
            
        return overview_table