# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import re

from controls import Controls
from excludedialog import ExcludeDialog

class PopulationTab(Controls):
    def __init__(self):
        self.object_symbol = ":QC.Population_TabProxy"
        self.graph_object_symbol = ":Population_JPanel"
        self.table_object_symbol = ":Population_GraphPanelRowHeader"
        self.plus_button_symbol = ":Population.+_JButton"
        self.minu_button_symbol = ":Population.-_JButton"
        self.clickable_graph_symbol = ":Population_Graph_3"
        self.exclude_button_symbol = ":QC.Exclude_JButton"
        self.excludedialog = ExcludeDialog()
     
    def clickTab(self):
        clickTab(findObject(self.object_symbol))
        
    def clickPlusButton(self):
        clickButton(self.plus_button_symbol)
        
    def clickMinusButton(self):
        clickButton(self.minu_button_symbol)
        
    def excludeButtonClick(self):
        clickButton(self.exclude_button_symbol)
    
    def confirmButtonFunctionality(self):
         #Confirm Exclude button functionality
         test.verify(findObject(":QC.Exclude_JButton").enabled == True, "Confirm that with data in graph, exclude button is enabled")
         #Confirm that the print button is grayed out
         test.verify(findObject(":QC.Print_JButton").enabled == False,"Confirm \"Print\" button (currently grayed out)") 
         #Confirm Zoom buttons
         test.verify(findObject(":Population.+_JButton").enabled == True, "Confirm that the + zoom button is enabled")
         test.verify(findObject(":Population.-_JButton").enabled == True, "Confirm that the - zoom button is enabled")
         test.verify(findObject(":QC.Print_JButton").enabled == False, "Confirm that the Print button is currently disabled - grayed out")
         #Confirm the Population, Reproducibility and Whole Blood Buttons are enabled. 
         #And Also Confirm tha Analyzer Selector Combo Box appears
         QCTab().confirmQCButtons()
         
    def confirmResultsInPopulationGraph(self):
        type = ['population']
        self.confirmGraphResults(self.table_object_symbol,self.graph_object_symbol,"population_table.csv","population_graph.csv",type)
         
    def confirmGraphResults(self,table_symbol,graph_symbol,table_filename,graph_filename,type):
        table_data = Tables.populateDigiCountDataTable(self,table_symbol)
        #Un-comment to do recording
        Tables.tableDataToFile(self,table_data, table_filename)
        Tables.confirmTableData(self,table_data,table_filename)
        graph_data = Graphs.getAllGraphData(self,graph_symbol)
        #Un-comment to do recording
        Graphs.graphDataToFile(self,graph_data, graph_filename,type)
        Graphs.confirmGraphData(self,graph_data, graph_filename)
        
    def confirmTotalGraphPoints(self,total):
        graph_data = Graphs.getAllGraphData(self,self.graph_object_symbol)
        #For now I am just testing for 1 or two points until we lock this down.
        actual_total = len(graph_data['SampleType.TREND']['WBC']['population'])
        test.verify(total == actual_total ,"Confirm that the expected graph points " + str(total) + " is equal to the actual points on the graph " + str(actual_total) )

    def confirmGraphHasPoints(self):
        graph_data = Graphs.getAllGraphData(self,self.graph_object_symbol)
        #For now I am just testing for 1 or two points until we lock this down.
        actual_total = len(graph_data['SampleType.TREND']['WBC']['population'])
        test.verify(actual_total > 0 ,"Confirm that the actual graph points are greater than zero. Actual number: " + str(actual_total) )
                
    def confirmBootstrapText(self):
        graph_data = Graphs.confirmBootstrapText(self,self.graph_object_symbol)
        
    def confirmPlusButtonIncreasesGraphScale(self):
        before_graph_points = Graphs.getGraphPoints(self,self.graph_object_symbol)
        self.clickPlusButton()
        after_graph_points = Graphs.getGraphPoints(self,self.graph_object_symbol)
        test.verify(before_graph_points['WBC']['xs'][0] < after_graph_points['WBC']['xs'][0],"Confirm that the x value of the point before the plus button is selected: " + str(before_graph_points['WBC']['xs']) + " is less than the same point after the plus button is clicked: " + str(after_graph_points['WBC']['xs']))

    def confirmMinusButtonDecreasesGraphScale(self):
        before_graph_points = Graphs.getGraphPoints(self,self.graph_object_symbol)
        self.clickMinusButton()
        after_graph_points = Graphs.getGraphPoints(self,self.graph_object_symbol)
        test.verify(before_graph_points['WBC']['xs'] > after_graph_points['WBC']['xs'],"Confirm that the x value of the point before the minus button is selected: " + str(before_graph_points['WBC']['xs']) + " is greater than the same point after the minus button is clicked: " + str(after_graph_points['WBC']['xs']))
        
    def doubleClickGraphPoint(self,display_name,index):
        graph_points = Graphs.getGraphPoints(self,self.graph_object_symbol)
        x_point = graph_points[display_name]['xs'][index]
        y_point = graph_points[display_name]['ys'][index]
         
        mouseClick(waitForObject(self.clickable_graph_symbol), x_point, y_point, 0, Button.Button1)
        doubleClick(waitForObject(self.clickable_graph_symbol), x_point, y_point, 0, Button.Button1)
        
        snooze(1.0)
        
        
        
