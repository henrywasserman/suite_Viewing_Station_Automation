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
from config import Config

class DigiCountTab(Controls):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":QC.DigiCount™_TabProxy"
        self.accession_number_combobox_symbol = ":QC.New control on Bloodhound 1:_JComboBox"
        self.runs_table_symbol = ":Table.Fail*_QCTable_2"
        self.low_graph_symbol = ":Low_JPanel_6"
        self.low_table_symbol = ":Low_GraphPanelRowHeader"
        self.normal_graph_symbol = ":Normal_JPanel_2"
        self.normal_table_symbol = ":Normal_JPanel_3"
        self.high_graph_symbol = ":High_JPanel_2"
        self.high_table_symbol = ":High_JPanel_3"
        self.all_graph_symbol = ":All_JPanel_2"
        self.all_table_symbol = ":All_JPanel_3"
        self.table_table_symbol = ":Table.Fail*_QCTable"  
        self.level_label_symbol = ":QC.Inactive: Inactive_JLabel"
        self.level_active_label_symbol = ":QC.Active: Normal_JLabel"
        self.activate_edit_button_symbol = ":QC.Activate/Edit_JButton"
        self.exclude_button_symbol = ":QC.Exclude_JButton"
        self.include_history_checkbox_symbol = ":QC.Include History_JCheckBox"
        self.save_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Save_JButton"
        self.cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.digicounttabs = ":DigiCount™.Print_JTabbedPane"  
        
        self.ranges_table_symbol = ":Table.Fail*_QCTable"
        self.tabs = ["Low", "Normal", "High", "All", "Table"]
        self.jpanels = [":Low_JPanel", ":Normal_JPanel", ":High_JPanel", ":All_JPanel"]
        self.last_run_pattern = re.compile('.*Last\\s+run\\s+on\\s+\\d+\/\\d+\/\\d+\\s+\\d+\:\\d+\\s+\\w+.*')
        self.tab_symbol_dictionary = {        
                                    "Low":self.low_graph_symbol,
                                    "Normal":self.normal_graph_symbol,
                                    "High":self.high_graph_symbol,
                                    "All":self.all_graph_symbol,
                                    "Table":self.table_table_symbol  
                                    }
        
        self.activateeditdigicountcontroldialog = ActivateEditDigicountControlDialog()
        self.qctab = QCTab()
        self.excludedialog = ExcludeDialog()
        
    def getSelectedControlItem(self):
        item = Controls.getSelectedComboboxItem(self,self.accession_number_combobox_symbol)
        return item
        
    def clickExcludeButton(self):
        clickButton(self.exclude_button_symbol)
        
    def clickIncludeHistoryCheckbox(self):
        Controls.clickCheckbox(self,self.include_history_checkbox_symbol)
        
    def confirmDigiCountTabIsSelected(self):
        tab = findObject(self.object_symbol)
        test.verify(tab.selected == True,"Confirm that the DigiCount tab is selected") 
        
    def confirmActiveLowLabelExists(self):
        label = findObject(self.level_active_label_symbol)
        test.verify("Active: Low" == label.text,"Confirm that the Active: Low label exists")
        
    def confirmActiveNormalLabelExists(self):
        label = findObject(self.level_active_label_symbol)
        test.verify("Active: Normal" == label.text,"Confirm that the Active: Normal label exists")
        
    def confirmActiveHighLabelExists(self):
        label = findObject(self.level_active_label_symbol)
        test.verify("Active: High" == label.text,"Confirm that the Active: High label exists")
        
    def clickTab(self):
        clickTab(waitForObject(self.object_symbol))
        
    def clickLowTab(self):
        clickTab(self.digicounttabs, "Low")
        
    def clickNormalTab(self):
        clickTab(self.digicounttabs, "Normal")
        
    def clickHighTab(self):
        clickTab(self.digicounttabs, "High")
        
    def clickAllTab(self):
        clickTab(self.digicounttabs, "All")
        
    def clickTableTab(self):
        clickTab(self.digicounttabs, "Table")
        
    def clickActivateEditButton(self):
        clickButton(self.activate_edit_button_symbol)

    def selectAccessionNumberComboBoxItem(self, item):
        Controls.selectComboboxItem(self,self.accession_number_combobox_symbol, item)
        
    def countFailuresAndWarnings(self,factory_defaults):
        table = findObject(self.runs_table_symbol)
        field = table.getClass().getDeclaredField("model")
        field.setAccessible(True)
        model = field.get(table)
        
        status_count = {}
        failure_count = 0
        warning_count = 0
        for row_index in range(table.getRowCount()):
            statistic = model.getRunsTable().getRow(row_index)
            for column_index in range(table.getColumnCount()):
                if self.getFactoryDefaultTest(str(statistic).split(" ")[0], factory_defaults) == 'Unreported':
                    continue
                status = str(model.inspect(statistic,column_index).status)
                if (status == "Failure"):
                    failure_count += 1
                elif(status == "Warning"):
                    warning_count += 1
        
        status_count = {"failures":failure_count, "warnings":warning_count}
        return status_count
                            
    def getAccessionNumberByLevel(self,level):
        combo_box = squish.findObject(self.accession_number_combobox_symbol)
        label = squish.findObject(self.level_label_symbol)
        
        accession_number = "Could not find accession number"
        
        for index in range(combo_box.getItemCount()):
            combo_box.setSelectedIndex(index)
            if level in label.text:
                accession_number = combo_box.selecteditem
                break
            
        return accession_number
        
    def navigate(self,tabname):
        clickTab(self.digicounttabs, tabname)
    
    def confirm5SubTabs(self):
       #Run through all the tabs
        test.verify(self.digicounttabs.getTabCount() == len(self.tabs),"Confirm there are " + str(len(self.tabs)) + " tabs")
        for index in range(self.digicounttabs.getTabCount()):
            test.compare(self.digicounttabs.getTitleAt(index), self.tabs[index],"Confirm the Text in tab " + str(index+1) + " to be " + self.tabs[index])
        
    def confirmButtonFunctionality(self,tabs):
        #Run through all the tabs - clicking on each one
        for index in range(len(tabs)):
           test.log("Click on the " + tabs[index] + " tab") 
           clickTab(self.digicounttabs, tabs[index])
           self.confirmControlsExist(index,tabs)
           
    def confirmLabelFunctionality(self,tabs):
        #Run through all the tabs - clicking on each one
        for index in range(len(tabs)):
           test.log("Click on the " + tabs[index] + " tab") 
           clickTab(self.digicounttabs, tabs[index])
           self.confirmLabelsExist(index, tabs)


    def confirmLabelsExist(self,index,tabs):
        #These next 5 Confirm Control Details text
        test.verify(self.last_run_pattern.match(findObject(":QC.Last Run on AM_JLabel").text) != None,"Confirm the Control Status to the right of the combobox - Last Run for the " + tabs[index] + " subtab")
        
        if (object.exists(":QC.Control is overdue and has caused lockout._JLabel-1")):   
            test.verify(findObject(":QC.Control is overdue and has caused lockout._JLabel-1").text.rfind("Control is") != -1, "Confirm the \"Control is\" string, to the right of the combobox Control-1 for the " + tabs[index] + " subtab")
        
        if (object.exists(":QC.Control is overdue and has caused lockout._JLabel-2")):
            test.verify(findObject(":QC.Control is overdue and has caused lockout._JLabel-2").text.rfind("Control Status") != -1, "Confirm the \"Control Status\" string, to the right of the combobox Control-2 for the " + tabs[index] + " subtab")
        else:
            test.log("Potential Problem - Control is overdue and has caused lockout - no longer exists on the QC Panel for the " + tabs[index] + " subtab")
        if (object.exists(":QC.Active: Normal_JLabel")):
            test.verify(findObject(":QC.Active: Normal_JLabel").text.rfind("Active") != -1, "Confirm the \"Active\" string below the combobox for the " + tabs[index] + " subtab")
        if (object.exists(":QC.Fail 5; Warn 34_JLabel")):
            test.verify(findObject(":QC.Fail 5; Warn 34_JLabel").text.rfind("fail") != -1, "Confirm the \"Fail\" string below the combobox for the " + tabs[index] + " subtab")
        else:
            test.log("Potential Problem QC Fail message does not exist on the digicount QC Tab for the " + tabs[index] + " subtab")

    def confirmControlsExist(self,index,tabs):
        #Confirm Tab Contains all the proper controls
        self.qctab.confirmQCButtons()
 
        test.verify(findObject(self.tab_symbol_dictionary[tabs[index]]).isShowing() == True,"Confirm that the " + tabs[index] + " page is showing")
        #If the Tab is Table then some of the expectations change
        #TODO: This should be refactored to use a factory pattern if - else's are ugly
        if (tabs[index] != "Table"):
            test.verify(findObject(":QC_JComboBox").enabled == True,"Confirm Control selector combobox is enabled for the " + tabs[index] + " subtab")        
            
        if (tabs[index] != "Table"):
            test.verify(findObject(self.include_history_checkbox_symbol).enabled == True,"Confirm \"Include History\" checkbox is enabled (all subtabs except for Table) for the " + tabs[index] + " subtab")
            test.verify(findObject(self.exclude_button_symbol).enabled == True,"Confirm \"Exclude\" button enabled for Table in the " + tabs[index] + " tab for the " + tabs[index] + " subtab")
            #Zoom buttons at the bottom of the  “Low”, “Normal”, “High”, and “All”
            test.verify(findObject(":Low.+_JButton").enabled == True,"Confirm + Zoom button at the bottom of the  \“Low\”, \“Normal\”, \“High\”, and \“All\” for the " + tabs[index] + " subtab")
            test.verify(findObject(":Low.-_JButton").enabled == True,"Confirm - Zoom button at the bottom of the  \“Low\”, \“Normal\”, \“High\”, and \“All\” for the " + tabs[index] + " subtab")                
        else:
            test.verify(findObject(self.exclude_button_symbol).enabled == False,"Confirm \"Exclude\" button (grayed out if no table cell is selected) for the " + tabs[index] + " subtab")
            if (object.exists(self.include_history_checkbox_symbol)):
                test.verify(findObject(self.include_history_checkbox_symbol).visible == False, "Confirm \"Include History\" checkbox is enabled (all subtabs except for Table) for the " + tabs[index] + " subtab")
            else:
                test.verify(True,"Confirm \"Include History\" checkbox is enabled (all subtabs except for Table) for the " + tabs[index] + " subtab")
                
            test.verify(findObject(":Low.+_JButton").visible == True,"Confirm + Zoom button at the bottom of the \“Table\" tab is not there for the " + tabs[index] + " subtab")
            test.verify(findObject(":Low.-_JButton").visible == True,"Confirm - Zoom button at the bottom of the \“Table\" tab is not there for the " + tabs[index] + " subtab")
        
        test.verify(findObject(":QC.Print_JButton").enabled == False,"Confirm \"Print\" button (currently grayed out) for the " + tabs[index] + " subtab")
            
        #Analyzer selector
        test.verify(findObject(":QC_JComboBox").enabled == True,"Analyzer selector combobox for the " + tabs[index] + " subtab")
        
        #Activate/Edit" button on Table subtab
        if(tabs[index] == "Table"):
            test.verify(findObject(self.activate_edit_button_symbol).enabled == True,"Confirm Activate/Edit button on Table subtab ")
            #Export" button on Table subtab
            test.verify(findObject(":QC.Export_JButton").enabled == True, "Confirm Export button on Table subtab")
        
    def confirmExcludeButton(self):
        if (object.exists(self.ranges_table_symbol)):
            mouseClick(waitForObjectItem(self.ranges_table_symbol, "7/0"), 19, 14, 0, Button.Button1)
        else:
            test.log("Possible failure - Failure label does not exist on the QC DigiCount page")
        #Not enabled
        test.verify(findObject(self.exclude_button_symbol).enabled == False,"Confirm \"Exclude\" button (grayed out if no table cell is selected)")
        if (object.exists(self.runs_table_symbol)):
            mouseClick(waitForObjectItem(self.runs_table_symbol, "7/3"), 107, 13, 0, Button.Button1)
        else:
            test.fail("Look into why this label no longer exists :Table.Fail*_QCTable_2")
        #Enabled
        test.verify(findObject(self.exclude_button_symbol).enabled == True,"Confirm \"Exclude\" button (enabled if table cell is selected)")

        clickTab(waitForObject(":DigiCount™.High_TabProxy"))
        mouseClick(waitForObject(":High_Graph"), 179, 1, 0, Button.Button1)
        mouseDrag(waitForObject(":High_Graph_2"), 115, 63, 111, 5, Modifier.None, Button.Button1)
        #Not Enabled
        test.verify(findObject(self.exclude_button_symbol).enabled == False,"Confirm \"Exclude\" button (grayed out if no table cell is selected)")
        
        mouseClick(waitForObject(":High_Graph"), 179, 1, 0, Button.Button1)
        #Set it back to Enabled just to be a good citizen : )
        test.verify(findObject(self.exclude_button_symbol).enabled == True,"Confirm \"Exclude\" button (enabled if table cell is selected)")
        
    def excludeButtonClick(self):
        clickButton(waitForObject(self.exclude_button_symbol))
    
    #TODO Refactor Dialog should have it's own class
    def exludeDialogResultCheck(self):
        mouseClick(waitForObject(":Result.Exclude Result_JCheckBox"), 14, 13, 0, Button.Button1)
    
    #TODO Refactor Dialog should have it's own class    
    def excludeDialogEnterReason(self):
        type(waitForObject(":Result_JTextArea"), "Automation Exclude Result Comment")
    
    #TODO Refactor Dialog should have it's own class    
    def excludeDialogClickSave(self):
        clickButton(waitForObject(self.save_button_symbol))
        
    #TODO Refactor Exclude Dialog should have it's own class
    def excludeDialogClickCancel(self):
        clickButton(waitForObject(self.cancel_button_symbol))
    
    #TODO Refactor Dialog should have it's own class
    def confirmExcludeDialogStatus(self):
        test.verify(findObject(self.save_button_symbol).enabled == False,"Confirm that Exclude Dialog Save button is disabled")
        test.verify(findObject(":Result.Ilvolvsky, Vadim_JTextArea").editable == False,"Confirm that the Comment is not editable")
        self.excludeDialogClickCancel()
    
    def confirmHistoryCheckboxFunctionality(self):
        #Run through all the tabs - clicking on each one
        for index in range(self.digicounttabs.getTabCount()):
           clickTab(self.digicounttabs, self.tabs[index])
           self.confirmIncludeHistoryFunctionality(index)
    
    def confirmIncludeHistoryFunctionality(self,index):
        if (self.tabs[index] != "Table"):
            currentgraphsize = findObject(self.jpanels[index]).width
            #Click Include History Checkbox to turn on functionality
            mouseClick(waitForObject(self.include_history_checkbox_symbol), 15, 12, 0, Button.Button1)
            #Testing the size of this jpanel for Include History. Without History size is 1485
            test.verify(findObject(self.jpanels[index]).width > currentgraphsize,"Testing to see if JPanel has Include History Information")
            #Click the Include History Checkbox again to turn off functionality
            mouseClick(waitForObject(self.include_history_checkbox_symbol), 15, 12, 0, Button.Button1)
            test.verify(findObject(self.jpanels[index]).width == currentgraphsize, "Testing to see if JPanel removes Include History Information")
                                
    def confirmAllControlsIncludedOnGraphOrTable(self):
        #Run through all the Items in the Control Selector Drop Down
        list = QCTab().getControlDropdownListItems()
        for item in range(len(list)):
            findObject(self.accession_number_combobox_symbol).setSelectedIndex(item)
            #Run through all the tabs - clicking on each one:All_JPanel_2
            for index in range(self.digicounttabs.getTabCount()):
                clickTab(self.digicounttabs, self.tabs[index])
                self.confirmAllControls(index)
    
    #TODO This should be refactored to use a Table Factory
    def confirmAllControls(self,index):
        #Most of the controls total 28
        totalparameters = 28
        totalvalues = 28
        total_linegraphs = 28
        
        if (self.tabs[index] == "Table"):
            return
        
        elif (self.tabs[index] == "Low"):
            #Parameter Value Graph
            underscore_numbers = ["_2","_7","_6"]
        elif (self.tabs[index] == "All"):
            underscore_numbers = ["_6","_7","_2"]
        else:
            #Parameter Value Graph
            underscore_numbers = ["_5","_6","_2"]
        
        #In the case of the All tab the controls total 84 for values and linegraphs
        if (self.tabs[index] == "All"):
            totalparameters = 28
            totalvalues = 84
            total_linegraphs = 84
            
        #Verify that there are 28 Paremeter Rows
        test.verify(findObject(self.jpanels[index]+ underscore_numbers[0]).getComponentCount() == totalparameters,"Confirm that all Parameters are listed in the Table")
        #Verify that there are 28 Value Rows
        test.verify(findObject(self.jpanels[index]+underscore_numbers[1]).getComponentCount() == totalvalues,"Confirm that all Values are listed in the Table")
        #Verify that there are 28 line graphs
        test.verify(findObject(self.jpanels[index]+underscore_numbers[2]).getComponentCount() == total_linegraphs,"Confirm that all line graphs appear in the panel")

    def confirmChangingControlChangesData(self):
        #workingdir = Config().getWorkingDir()
        #images = workingdir + "/../data/images/"
        #scripts = workingdir + "/../../scripts/"
        #classpath = workingdir + "/../../imagecompare/bin"
        
        #image1 = images + "confirmChangingControlChangesData1.png"
        #image2 = images + "confirmChangingControlChangesData2.png"        
        
        #Select the Low Tab
        clickTab(self.digicounttabs, self.tabs[0])
        
        #Select the First Item
        findObject(self.accession_number_combobox_symbol).setSelectedIndex(0)
        
        images = Images()
        
        image_filename1 = images.saveImage("confirmChangingControlChangesData1.png",":Low_Graph_5")
        
        controlstring = findObject(self.accession_number_combobox_symbol).getItemAt(0).toString()
        #Verify that the first Item Control String is the same as the Control String found in the table
        test.verify(findObject(":Low_Graph").getSelectedGraphableLine().getGraphLine().toString()
                    == findObject(self.accession_number_combobox_symbol).getItemAt(0).toString(),"Testing that a cell contains the Control String: " + controlstring)
        
        #Select the Second Item
        findObject(self.accession_number_combobox_symbol).setSelectedIndex(1)
        
        image_filename2 = images.saveImage("confirmChangingControlChangesData2.png",":Low_Graph_5")
        
        controlstring = findObject(self.accession_number_combobox_symbol).getItemAt(1).toString()
        #Test that the Second Item Control String is the same as the Control String found in the new table
        test.verify(findObject(":Low_Graph").getSelectedGraphableLine().getGraphLine().toString()
                    == findObject(self.accession_number_combobox_symbol).getItemAt(1).toString(),"Testing that a cell contains the Control String: " + controlstring)
        
        images.compareImages(image_filename1, image_filename2, "false")
                   
    def confirmAnalyzerSelector(self,servers):
        server_list = ["Bloodhound 1", "Bloodhound 2"]
        list = QCTab().getAnalyzerDropdownListItems()
        test.verify(str(len(list)) == servers, "Confirming that the number of servers in the list equal the qc.server number in the bloodhound.properties file")
        for server in list:
            findObject(":QC_JComboBox").setSelectedIndex(server)
            test.verify(findObject(":QC_JComboBox").selecteditem.toString().strip() == server_list[server], "Checking for "+ server_list[server]+" in the Analyzer Selector")
            
        #Be a good citizen and put the list back to zero.
        findObject(":QC_JComboBox").setSelectedIndex(0)

    def confirmTableButtons(self):
        #Confirm the DigiCount, Reproducibility and Whole Blood Buttons are enabled.
        QCTab().confirmQCButtons()
        test.verify(findObject(self.activate_edit_button_symbol).enabled,"Confirm Activate/Edit button is enabled")
        
    def isSelected(self):
        return findObject(self.object_symbol).selected == 1
    
    def confirmMeasuredColumns(self,filename):
        table_object = findObject(self.ranges_table_symbol)
        Tables.confirmDigiCountTabTableData(self,table_object,filename)
#        f = open(filename)
#        reader = csv.reader(f,delimiter = ',')
#        
#        digicount_dictionary = {}
#        
#        for data in reader:
#            digicount_dictionary[data[0].split(' ',1)[0]] = data[1:]
#        
#        f.close()
#        
#        runs_table_data = Tables.populateTableData(self,self.runs_table_symbol)
#        
#        ranges_table_data = Tables.populateTableData(self,self.ranges_table_symbol)
#         
#        for index in range(len(ranges_table_data)):
#            for key in runs_table_data[index]:
#                test.verify(digicount_dictionary[ranges_table_data[index]['Parameter']][0] == Controls.removeNonAscii(self,runs_table_data[index][key]),"Confirm that the expected data in row " + ranges_table_data[index]['Parameter'] + " of the Measured columns table: " + digicount_dictionary[ranges_table_data[index]['Parameter']][0]+ " is equal to the actual data: " + Controls.removeNonAscii(self,runs_table_data[index][key]))
                
    def confirmResultsInLowGraph(self):
        levels = ['Low']
        self.confirmAllGraphResults(self.low_table_symbol,self.low_graph_symbol,"low_digitable.csv","low_digigraph.csv",levels)
        
    def confirmResultsInNormalGraph(self):
        levels = ['Normal']
        self.confirmGraphResults(self.normal_table_symbol,self.normal_graph_symbol,"normal_digitable.csv","normal_digigraph.csv",levels)
        
    def confirmResultsInHighGraph(self):
        levels = ['High']
        self.confirmGraphResults(self.high_table_symbol,self.high_graph_symbol,"high_digitable.csv","high_digigraph.csv",levels)
        
    def confirmResultsInAllGraph(self):
        levels = ['Low','Normal','High']
        self.confirmAllGraphResults(self.all_table_symbol,self.all_graph_symbol,"all_digitable.csv","all_digigraph.csv",levels)
        
    def confirmGraphResults(self,table_symbol,graph_symbol,table_filename,graph_filename,levels):
        table_data = Tables.populateDigiCountDataTable(self,table_symbol)
        #Un-comment to do recording
        Tables.tableDataToFile(self,table_data, table_filename)
        Tables.confirmTableData(self,table_data,table_filename)
        graph_data = Graphs.getAllGraphData(self,graph_symbol)
        #Un-comment to do recording
        Graphs.graphDataToFile(self,graph_data, graph_filename)
        Graphs.confirmGraphData(self,graph_data, graph_filename)
        
    def confirmAllGraphResults(self,table_symbol,graph_symbol,table_filename,graph_filename,levels):
        table_data = Tables.populateDigiCountDataAllTable(self,table_symbol)
        #Un-comment to do recording
        Tables.tableDataAllToFile(self,table_data, table_filename)
        Tables.confirmAllTableData(self,table_data,table_filename)
        graph_data = Graphs.getAllGraphData(self,graph_symbol)
        #Un-comment to do recording
        Graphs.graphDataToFile(self,graph_data, graph_filename)
        Graphs.confirmGraphData(self,graph_data, graph_filename)
        
    def getListBoxItems(self):
        combo_box = findObject(self.accession_number_combobox_symbol)
        return Controls.getListBoxItems(self,combo_box)
    
    def getFactoryDefaultTest(self,parameter,factory_defaults):
        test = ""
        for index in range(len(factory_defaults)):
            if factory_defaults[index]["Parameter"] == parameter:
                test = factory_defaults[index]["Test"]
                break
        return test
    
    def getAllGraphData(self,parameter = "all"):
        graph_data = Graphs.getAllGraphData(self,self.all_graph_symbol,parameter)
        return graph_data
    
            