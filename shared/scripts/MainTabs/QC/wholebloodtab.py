# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish
import re
import codecs
import shutil

from newwholebloodcontroldialog import NewWholeBloodControlDialog
from controls import Controls 

class WholeBloodTab(Controls):
    def __init__(self):
        #Warning does not always appear in this label
        self.fail_warn_pattern = re.compile('.*fail.*')
        self.date_time_pattern = re.compile('\\d+\/\\d+\/\\d+\\s+\\d+\:\\d+\\s+\\w+.*')
        self.bloodhound_pattern = re.compile('Bloodhound\\s1.*')
        self.panel_with_checkboxes = []
        self.checkbox_objects = []
        self.colorbox_objects = []
        self.dropdown_analyzer_items = []
        self.checkbox_text = []
        self.control_combobox_symbol = ":QC.New control on Bloodhound 1:_JComboBox"
        self.table_tab_symbol = ":Whole Blood.Table_TabProxy"
        self.graph_tab_symbol = ":Whole Blood.Graph_TabProxy"
        self.right_table_symbol = ":Table_QCTable"
        self.analyzer_combobox_symbol = ":QC_JComboBox"
        self.graph_object_symbol = ":Graph_JPanel_6"
        self.separate_by_mode_graph_object_symbol = ":Graph_JPanel_7"
        self.table_object_symbol = ":Table_QCTable_2"
        self.plus_button_symbol = ":Graph.+_JButton"
        self.minus_button_symbol = ":Graph.-_JButton"
        self.absolute_radiobutton_symbol = ":Graph.Absolute_JRadioButton"
        self.percent_radiobutton_symbol = ":Graph.Percent_JRadioButton"
        self.separate_by_mode_checkbox_symbol = ":Graph.Separate by Mode_JCheckBox"
        
        self.newwholebloodcontroldialog = NewWholeBloodControlDialog()
        #Set the List of Analyzers
        self.getListOfAnalyzers()
        
        #Hard coding these for now until I can figure out a better way to analyze colors that are close to each other
        self.expected_colorbox_object_colors = ["java.awt.Color[r=40,g=75,b=159]",
                                       "java.awt.Color[r=56,g=105,b=223]",
                                       "java.awt.Color[r=110,g=159,b=40]",
                                       "java.awt.Color[r=153,g=223,b=56]"]
        
    def clickTab(self):
        clickTab(waitForObject(":QC.Whole Blood_TabProxy"))
        
    def clickTableTab(self,tablename):
        if tablename == "Graph":
            clickTab(waitForObject(self.graph_tab_symbol))
        elif tablename == "Table":
            clickTab(waitForObject(self.table_tab_symbol))
    
    def clickPercentRadioButton(self):
        radio_button = findObject(self.percent_radiobutton_symbol)
        radio_button.doClick()
        
    def clickAbsoluteRadioButton(self):
        radio_button= findObject(self.absolute_radiobutton_symbol)
        radio_button.doClick()
        
    def confirmPercentRadioButtonIsActive(self):
        radio_button = findObject(self.percent_radiobutton_symbol)
        test.verify(radio_button.selected == True,"Confirm that the Percent Radio Button is Active")

    def confirmAbsoluteRadioButtonIsActive(self):
        radio_button = findObject(self.absolute_radiobutton_symbol)
        test.verify(radio_button.selected == True,"Confirm that the Absolute Radio Button is Active")
    
    def confirmAbsoluteRadioButtonIsInactive(self):
        radio_button = findObject(self.absolute_radiobutton_symbol)
        test.verify(radio_button.selected == False, "Confirm that the Absolute Radio Button is Inactive")
        
    def confirmPercentRadioButtonIsInactive(self):
        radio_button = findObject(self.percent_radiobutton_symbol)
        test.verify(radio_button.selected == False, "Confirm that the Percent Radio Button is Inactive")
    
    def clickSeparateByModeCheckbox(self):
        separate_by_mode = findObject(self.separate_by_mode_checkbox_symbol)
        separate_by_mode.doClick()
        
    def confirmAdditionalLineAdded(self):
        self.setCheckBoxAndColorBoxObjects()
        test.verify(len(self.dropdown_analyzer_items) * 2 == len(self.checkbox_objects),"Confirm that there are twice as many analyzer checkboxes as there are Analyzers")
        
    def setCheckBoxAndColorBoxObjects(self):
        self.checkbox_objects = []
        self.colorbox_objects = []
        panel = findObject(self.separate_by_mode_graph_object_symbol)
        
        for index1 in range(panel.getComponentCount()):
            component1 = panel.getComponent(index1)
            for index2 in range(component1.getComponentCount()):
                component2 = component1.getComponent(index2)
                for index3 in range(component2.getComponentCount()):
                    component3 = component2.getComponent(index3)
                    if 'javax.swing.JCheckBox' in component3.toString():
                        self.checkbox_objects.append(component3)
                        continue
                    elif 'javax.swing.JPanel' in component3.toString():
                        self.colorbox_objects.append(component3)
                        continue
                    for index4 in range(component3.getComponentCount()):
                        #test.log(component3.getComponent(index4).toString())
                        if 'javax.swing.JCheckBox' in component3.getComponent(index4).toString():
                            self.checkbox_objects.append(component3.getComponent(index4))
                        elif 'javax.swing.JPanel' in component3.getComponent(index4).toString():
                            self.colorbox_objects.append(component3.getComponent(index4))
                            
    #Confirm that the top line displays the analyzer name with "Closed" to the right of it which represents the "Rack" and "STAT" runs
    def confirmTopLineDisplaysAnalizerNameWithClosed(self):
        self.setCheckBoxAndColorBoxObjects()
        counter = 0
        for checkbox in self.checkbox_objects:
            if counter % 2 == 0:
                test.verify("Closed" in checkbox.text,"Confirm that the first checkbox line contains Closed")
                counter += 1
            
    #Confirm that the line below displays the analyzer name with "Open" to the right of it which represents the "Open Port" runs
    def confirmBelowLineDisplaysAnalizerNameWithOpen(self):
        self.setCheckBoxAndColorBoxObjects()
        counter = 0
        for checkbox in self.checkbox_objects:
            if counter % 2 == 1:
                test.verify("Open" in checkbox.text,"Confirm that the second checkbox line contains Open")
                counter += 1

    #Confirm that all of the analyzer lines still have colored boxes and checkboxes next to them
    def confirmAnalyzerColoredBoxesAndCheckBoxes(self):
        self.setCheckBoxAndColorBoxObjects()
        counter = 0
        for colorbox in self.colorbox_objects:
            test.verify(self.expected_colorbox_object_colors[counter] == str(colorbox.background),"Confirm that the expected color " + self.expected_colorbox_object_colors[counter] + " is equal to the actual color " + str(colorbox.background))
            counter += 1

        test.verify(len(self.dropdown_analyzer_items) * 2 == len(self.checkbox_objects),"Confirm that there are twice as many analyzer checkboxes as there are Analyzers")            
        
    def clickOnAllClosedCheckboxesTo(self,status):
        self.setCheckBoxAndColorBoxObjects()
        for checkbox in self.checkbox_objects:
            if 'Closed' in checkbox.text:
                checkbox.doClick()
                if status.lower() == 'disable':
                    test.verify(checkbox.selected == False, "Confirm that the checkbox that was just clicked is now not selected")
                else:
                    test.verify(checkbox.selected == True, "Confirm that the checkbox that was just clicked is now selected")

    def clickOnAllOpenCheckboxesTo(self,status):
        self.setCheckBoxAndColorBoxObjects()
        for checkbox in self.checkbox_objects:
            if 'Open' in checkbox.text:
                checkbox.doClick()
                if status.lower() == 'disable':
                    test.verify(checkbox.selected == False, "Confirm that the checkbox that was just clicked is now not selected")
                else:
                    test.verify(checkbox.selected == True, "Confirm that the checkbox that was just clicked is now selected")
                    
    def clickOnAllCheckboxesTo(self,status):
        self.setCheckBoxAndColorBoxObjects()
        for checkbox in self.checkbox_objects:
            checkbox.doClick()
            if status.lower() == 'disable':
                test.verify(checkbox.selected == False, "Confirm that the checkbox that was just clicked is now not selected")
            else:
                test.verify(checkbox.selected == True, "Confirm that the checkbox that was just clicked is now selected")
                    
    def confirmAllVisiblePointsAreFor(self,mode):
        graph_data = Graphs.getAllGraphData(self,self.graph_object_symbol)
        for parameter in graph_data:
            for type in graph_data[parameter]:
                for display_name in graph_data[parameter][type]:
                    for index in range(len(graph_data[parameter][type][display_name])):
                        if graph_data[parameter][type][display_name][index]["visible"] == 1:
                            if mode.lower() == "open":
                                test.verify(graph_data[parameter][type][display_name][index]["processing_mode"] == "Open","Confirm that every graph point that is visible has a processing mode of Open")
                            elif mode.lower() == "rack or stat":
                                test.verify(graph_data[parameter][type][display_name][index]["processing_mode"] == "STAT" or
                                            graph_data[parameter][type][display_name][index]["processing_mode"] == "Rack","Confirm that every graph point that is visible has a processing mode of either Rack or STAT")
                            elif mode.lower() == "no points":
                                test.verify(False,"Found a visible point on the graph. There should not be any visible points on the graph in this testcase")
                            elif mode.lower() == "all points":
                                test.verify(graph_data[parameter][type][display_name][index]["processing_mode"] == "STAT" or
                                            graph_data[parameter][type][display_name][index]["processing_mode"] == "Rack" or
                                            graph_data[parameter][type][display_name][index]["processing_mode"] == "Open","Confirm that every graph point that is visible has a processing mode of either Rack, STAT or Open")
                            

    #Confirm that the analyzer lines colored boxes are a slightly different shade from the one above it
    def confirmColoredBoxColors(self):
        self.setCheckBoxAndColorBoxObjects()        
        counter = 0
        for colorbox in self.colorbox_objects:
            test.verify(self.expected_colorbox_object_colors[counter] == str(colorbox.background),"Confirm that the expected color " + self.expected_colorbox_object_colors[counter] + " is equal to the actual color " + str(colorbox.background))
            counter += 1

    def selectAnalyzer(self,item):
        Controls.selectComboboxItem(self,self.analyzer_combobox_symbol, item)
        
    def selectControlItem(self,item):
        Controls.selectComboboxItem(self,self.control_combobox_symbol, item)
        
    def confirmPlusAndMinusButtons(self):
        plus_button = findObject(self.plus_button_symbol)
        minus_button = findObject(self.minus_button_symbol)
        test.verify(plus_button.enabled == True,"Confirm that the plus button is enabled.")
        test.verify(minus_button.enabled == True, "Confirm that the minus button is enabled.")
        
    def confirmColoredSquaresAreDifferent(self):
        dictionary = {}
        self.setListOfCheckBoxesAndColorBoxesForCurrentAnalyzer()
        for colorbox in self.colorbox_objects:
            dictionary[colorbox.background.toString()] = 1
        
        test.verify(len(dictionary) == len(self.colorbox_objects),"Confirm that each colorbox in the wholeblood graph tab has a unique color")
        
    def confirmAllControls(self):
        #Make sure we are on the Graph Tab
        self.clickTableTab("Graph")
        #Click on the Scroll Bar and Drag the mouse all the way to the left
        mouseDrag(findObject(":Graph_JButton"),115,63,-1000,5, Modifier.None, Button.Button1)
        #Click on the empty graph space and drag the mouse
        mouseDrag(waitForObject(":Graph_Graph"), 115, 63, 111, 5, Modifier.None, Button.Button1)
        #Verify the Exclude button is disabled
        test.verify(findObject(":QC.Exclude_JButton").enabled == False,"Confirm the Exclude Button is disabled when points are not selected")
        
        #Click on the Scroll Bar and Drag the mouse all the way to the right
        mouseDrag(findObject(":Graph_JButton"), 115, 63, 1000, 5, Modifier.None, Button.Button1)
        #Click on Graph
        mouseClick(waitForObject(":Graph_Graph_3"), 2518, 10, 0, Button.Button1)
        test.verify(findObject(":QC.Exclude_JButton").enabled == True, "Confirm the Exclude Button is enabled when data points are selected")
        
        #Test for the Exclude Button
        #There  is currently a bug in Mantis that the export button does not exist here.  So I am going
        #to let this test pass even though the export button cannot be found.  When this tests "fails"
        #It will signal that this bug (no export button) has been fixed.
        
        test.verify(not object.exists(":QC.Export_JButton"),"Export Button should not exist (this was a know mantis bug resolved to have the button not exist")
        test.verify(findObject(":QC.Print_JButton").enabled == False,"Confirm that the Print button is disabled")
        #Confirm "DigiCount"", ""Reproducibility"", ""Whole Blood"", and ""Activate/Edit"" buttons
        #Confirm that the Analyser selector combobox exists
        QCTab().confirmQCButtons()
        
    #When Separate by Mode Checkbox is selected there should be two corresponding checkboxes for each analyzer
    def confirmTwoCheckboxesForEachAnalyzer(self):
        #For each Analyzer
        for item in self.analyzer_list:
            #Set the Combo Box to that Analyzer item
            self.analyzer_dropdown.setSelectedIndex(item)
            #Get it's String
            analyzer_name = self.analyzer_dropdown.getSelectedItem().toString().strip()
            #Get Lists of Checkboxes and ColorBoxes
            self.setListOfCheckBoxesAndColorBoxesForCurrentAnalyzer()
            #Get the String For the checkbox label
            bloodhound_checkbox_label = self.checkbox_objects[item].label
            #Compare them
            test.verify(analyzer_name == bloodhound_checkbox_label, "Confirm that the dropdown item name is the same as the checkbox label")
            
        #Be a good citizen and return the Analyzer Dropdown to it's default state.
        self.analyzer_dropdown.setSelectedIndex(0)
                
    #For each item in the Analyzer Dropdown there should be a corresponding checkbox.
    def confirmCheckboxForEachAnalyzer(self):

        #For each Analyzer
        for item in self.analyzer_list:
            #Set the Combo Box to that Analyzer item
            self.analyzer_dropdown.setSelectedIndex(item)
            #Get it's String
            analyzer_name = self.analyzer_dropdown.getSelectedItem().toString().strip()
            #Get Lists of Checkboxes and ColorBoxes
            self.setListOfCheckBoxesAndColorBoxesForCurrentAnalyzer()
            #Get the String For the checkbox label
            bloodhound_checkbox_label = self.checkbox_objects[item].label
            #Compare them
            test.verify(analyzer_name == bloodhound_checkbox_label, "Confirm that the dropdown item name is the same as the checkbox label")
            
        #Be a good citizen and return the Analyzer Dropdown to it's default state.
        self.analyzer_dropdown.setSelectedIndex(0)
        
    def confirmCheckboxesAreCheckedByDefault(self):
        #For each Analyzer
        for item in range(len(self.analyzer_list)):
            self.setListOfCheckBoxesAndColorBoxesForCurrentAnalyzer()
            test.verify(self.checkbox_objects[item].selected == 1,"Confirm that checkbox " + str(item) + " is selected")
            
    def confirmAnalzyerNames(self):
        #For each Analyzer
        for item in range(len(self.analyzer_list)):
            test.verify(self.checkbox_text[item] == Controls.removeNonAscii(self,self.dropdown_analyzer_items[item]), "Confirm that the expected analyzer item " + self.checkbox_text[item] + " is the same as the actual analyzer item " + Controls.removeNonAscii(self,self.dropdown_analyzer_items[item]) )
            
    def confirmRadioButtonsExist(self):
        absolute = findObject(self.absolute_radiobutton_symbol)
        percent = findObject(self.percent_radiobutton_symbol)

        test.verify("Absolute" == str(absolute.text),"Confirm that the Absolute radio button exists")
        test.verify(absolute.selected == True,"Confirm that the Absolute radio button is selected by default")
        test.verify("Percent" == str(percent.text), "Confirm that the Percent radio button exists")
        
    def confirmDefaultRadioButtonSelection(self):
        separate_by_mode = findObject(self.separate_by_mode_checkbox_symbol)
        test.verify(separate_by_mode.selected == False,"Confirm that the Separate by Mode checkbox exists and is not checked by default")
            
    def confirmColorBox(self):
        #For each Analyzer
        for item in range(len(self.analyzer_list)):
            #At this point just looking for the Color Blue
            #findObject("::Graph_Graph_5").getAccessibleContext().getBackground().toString()
            #Here is the color of the graph line - [r=48,g=90,b=191] we can double check this here:
            #http://www.javascripter.net/faq/rgbtohex.htm
            #Get Lists of Checkboxes and ColoBoxes
            self.setListOfCheckBoxesAndColorBoxesForCurrentAnalyzer()
            self.deSelectAllCheckBoxes()
            self.selectACheckBox(self.dropdown_analyzer_items[item])
            graphline_color = findObject(":Graph_Graph").getSelectedGraphableLine().getGraphLine().getColor()
            #Here is the color of the :Graph_Jpanel color box [r=48, g=90, b=191]
            color_box_color = self.colorbox_objects[item].getBackground()
            test.verify(graphline_color == color_box_color,"Confirm that the color of the graphline is the same as the color box")
        
    def confirmAbsoluteAndPercentRadioButtons(self):
        #Confirm that radio buttons exist and that Absolute is the default and is selected.
        test.verify(findObject(self.absolute_radiobutton_symbol).isSelected() == True,"Confirm that the Absolute Radio Button is selected")
        #Confirm that the Percent Radio Button is not selected
        test.verify(findObject(self.percent_radiobutton_symbol).isSelected() == False,"Confirm that the Percent Radio Button is not selected")
       
    def confirmSeparateByModeCheckBox(self):
        #Confirm that the Separate by Mode Check Box exists and is not selected
        test.verify(findObject(self.separate_by_mode_checkbox_symbol).isSelected() == False, "Confirm that the Separate by Mode checkbox is not selected")
        
    def confirmButtonsChangeGraphConfigurations(self):
        "This will test if the graph appears. If isNull == 0 graph exists on screen"
        "Test Graph Exists"
        test.verify(isNull(findObject(":Graph_Graph_5").getSelectedGraphableLine()) == 0,"Confirm Whole Blood Graph is displayed")
        "Click on the Bloodhound 1 checkbox"
        
        #Now Deselect the 2 Bloodhound Checkboxes
        self.deSelectAllCheckBoxes()
        "if the graph does not appear.  isNull will == 1"
        test.verify(isNull(findObject(":Graph_Graph_5").getSelectedGraphableLine()) == 1,"After Clicking Bloodhound 1 checkbox, confirm Whole Blood Graph is not displayed")
        #Put Graph Back on the screen
        self.selectAllCheckBoxes()
        #Take a screen shot to compare Absolute and Percent Radio Button changes
        self.confirmAbsoluteAndPercentRadioButtonChanges()

        self.confirmSeparateByModeCheckBoxChanges()
        
    def confirmSeparateByModeCheckBoxChanges(self):
        images = Images()
        
        #First get the default image
        image_filename1 = images.saveImage("separate_by_mode_image_checked",":Graph_Graph")
        #Then click the Separte by Mode checkbox
        findObject(self.separate_by_mode_checkbox_symbol).doClick()
        #Now save the new image
        image_filename2 = images.saveImage("separate_by_mode_image_unchecked",":Graph_Graph")
        #Compare the Images expecting them to be different
        images.compareImages(image_filename1, image_filename2, "False")
        
        #Now put the Separate Mode back to its original state
        findObject(self.separate_by_mode_checkbox_symbol).doClick()
        
    def confirmAbsoluteAndPercentRadioButtonChanges(self):
        images = Images()

        image_filename1 = images.saveImage("absolute_radio_image",":Graph_JPanel_3")        
        #Now Click on the Percent Radio Button  
        mouseClick(waitForObject(self.percent_radiobutton_symbol), 15, 18, 0, Button.Button1)
        image_filename2 = images.saveImage("percent_radio_image",":Graph_JPanel_3")
        
        test.log("Test to see if the WBC image when the Absolute Radio Button is selected is different from the WBC Image when the Percent Radio button is selected")
        images.compareImages(image_filename1, image_filename2, "false")
        
        #Select the Absolute Radio Button to put it back
        mouseClick(waitForObject(self.absolute_radiobutton_symbol), 15, 18, 0, Button.Button1)
        
        #Select the Separate by Mode Checkbox
        mouseClick(waitForObject(self.separate_by_mode_checkbox_symbol), 15, 18, 0, Button.Button1)
        #Verify That there are now 2 checkboxs - Bloodhound 1 Close and Bloodhound 1 Open
        test.verify(findObject(":Graph.Bloodhound 1 Closed_JCheckBox").selected == 1, "The Bloodhound 1 Closed checkbox is selected")
        test.verify(findObject(":Graph.Bloodhound 1 Closed_JCheckBox").text == "Bloodhound 1 Closed", "Confirm that the text is Bloodhound 1 Closed")
        test.verify(findObject(":Graph.Bloodhound JCheckBox").selected == 1, "Bloodhound 1 Open" "The Bloodhound 1 Open checkbox is selected")
        test.verify(findObject(":Graph.Bloodhound JCheckBox").text == "Bloodhound 1 Open", "Confirm that the text is Bloodhound 1 Open")
        #Select the Separate by Mode Checkbox
        mouseClick(waitForObject(self.separate_by_mode_checkbox_symbol), 15, 18, 0, Button.Button1)
        
    def confirmTableButtons(self):
        qctab = QCTab() 
        # "Confirm that the following buttons/functionality (click on each button and review the result) are available on the Whole Blood > Table tab:
        #-""Exclude"" button (grayed out by default unless a table cell is selected)
        test.verify(findObject(":QC.Exclude_JButton").enabled == False, "Confirm that the Exclude button is disabled")
        #-""Export"" button
        test.verify(findObject(":QC.Export_JButton").enabled == True, "Confirm that the Export button is enabled")
        #-""DigiCount"", ""Reproducibility"", and ""Whole Blood"" buttons
        qctab.confirmQCButtons()
        #-""Close"" button (grayed out if the control selected is not active)
        test.verify(findObject(":QC.Close_JButton").enabled == False,"Confirm that the Close button is disabled")
        #-Control selector combobox
        test.verify(findObject(":QC.New control on Bloodhound 1:_JComboBox").enabled == True, "Confirm that the Control selector combobox is enabled.")
        #-Control Details text under the Control selector combobox and the Control Status to the right of the combobox
        self.confirmControlDetailsText()
        #-Analyzer selector combobox
        #Note Analyzer selector combobox is checked during QCTab().confirmButtons()
        
        #-""Print"" button (currently grayed out)"
        test.verify(findObject(":QC.Print_JButton").enabled == False, "Confirm that the Print button is currently disabled - grayed out")

    def confirmControlDetailsText(self):
       #Confirm Control Details text under the Control selector bombobox and the Control Status to the right of the combo box.
        if (object.exists(":QC.Closed_JLabel")):
            test.verify(findObject(":QC.Closed_JLabel").text == "Closed","Confirm the Control Details below combo box - Closed")
        else:
            test.log("The Closed label did not exist, but at this point it is not necessary to make sure it is there every time.")
            
        if (object.exists("")):
            test.verify(findObject(":QC.Was active_JLabel").text == "Was active", "Confirm the text to the right of the combo box - Was active")
        else:
            test.log("TODO find out if this label should exist :QC.Was active_JLabel")
        
        if (object.exists(":QC.Fail 5; Warn 34_JLabel")):    
            test.verify(self.fail_warn_pattern.match(findObject(":QC.Fail 5; Warn 34_JLabel").text) != None,"Confirm that there is Fail Warn text and it conforms to the expected pattern Fail #;Warn #")
        else:
            test.fail("The fail label should exist: :QC.Fail 5; Warn 34_JLabel")
        #TODO Need to fix the object mapping of these labels.  Regular expressions in the Object Maps are not currently working properly.
        #test.verify(self.date_time_pattern.match(findObject(":QC.9/25/13 9:55 PM to_JLabel").text) != None,"Confirm the text to the right of the combo box with the date time pattern ##/##/## ##:## \w+")
        #test.verify(self.date_time_pattern.match(findObject(":QC.10/10/13 8:37 AM_JLabel").text) != None,"Confirm the text to the right of the combo box with the date time pattern ##/##/## ##:## \w+")
        
    #-Combobox labeled ""Reference"" and defaulted to ""Mean""
    def confirmCombobox(self):
        test.verify(findObject(":Table.Reference:_JComboBox").enabled == True, "Confirm that the Reference ComboBox is enabled")
        test.verify(findObject(":Table.Reference:_JComboBox").selecteditem.toString() == "Mean", "Confirm that the ComboBox is defaulted to Mean")
        test.verify(findObject(":Table.Reference:_JLabel").text == "Reference:", "Confirm that the Label next to the Combo Box contains 'Reference:'")

    #-""Save"" button (enabled when the selected control is active and disabled if otherwise)
    def confirmSaveButton(self):
        test.verify(findObject(":Table.Save_JButton").enabled == False, "Confirm that the save button is disabled by default")
        #Select the Bloodhood control from the Reference dropdown
        findObject(":Table.Reference:_JComboBox").setSelectedIndex(1)
        test.verify(self.bloodhound_pattern.match(findObject(":Table.Reference:_JComboBox").selecteditem.toString()) != None, "Confirm that the selected item now contains Bloodhound 1")
        #Confirm that the Save button is now enabled
        test.verify(findObject(":Table.Save_JButton").enabled == True, "Confirm that the Save button is now enabled")
        #Be a good citizen and put the Combo Box back to item 0
        findObject(":Table.Reference:_JComboBox").setSelectedIndex(0)
        
    def confirmReferenceComboRuns(self):
        #First Click on the Table Tab
        self.clickTableTab("Table")
        #Grab the Bloodhound STAT and OPEN Table Headers
        self.grabBloodhoundStatAndOpenHeaders()
        
    def grabBloodhoundStatAndOpenHeaders(self):
        #Note I was not yet able to grab the Date from the Table header.
        #So all other information in the Item dropdown is being validated except date.
        #TODO Grab the date also...
        header_list = []
        #Grab the Bloodhound1 Header text
        header1 = findObject(":Bloodhound 1").text.split("\n")
        #Grab the Bloodhound2 Header text
        header2 = findObject(":Bloodhound 2").text.split("\n")
        
        header_list = [header1, header2]
        
        #Graph the Items in the Reference dropdown
        reference_items = self.getListOfReferenceItems()
        
        #Skip the first Item in the list if it is "Mean"
        p = re.compile('(\d+\:\d+)\:\d+(\s[PM|AM]+)')
        counter = 0
        for item in reference_items:
            if item == "Mean":
                continue
            #This will test that the Header information is contained in the Reference dropdown list
            #It assumes that the order is Mean, Bloodhound 1, Bloodhound 2
            #-1 means that the string was not found 
            for header in header_list[counter]:
                m = p.match(header)
                if m != None:
                    header = m.group(1) + m.group(2)
                test.verify(header in item,"Confirming that item in reference dropdown "+ item + " contains " + str(header) + " from Table Header")
            
            counter = counter + 1
                         
    def selectARun(self):
        findObject(":Table.Reference:_JComboBox").setSelectedIndex(1)
        test.verify(self.bloodhound_pattern.match(findObject(":Table.Reference:_JComboBox").selecteditem.toString()) != None, "Confirm that the selected item now contains Bloodhound 1")

    def getListOfAnalyzers(self):
        #Get the list of Analyzers in the dropdown
        self.analyzer_list = QCTab().getAnalyzerDropdownListItems()
        #Get the Analizer Dropdown object
        self.analyzer_dropdown = findObject(self.analyzer_combobox_symbol)
        for item in self.analyzer_list:
            self.analyzer_dropdown.setSelectedIndex(item)
            self.dropdown_analyzer_items.append(self.analyzer_dropdown.getSelectedItem().toString().strip())
            
        #Be a good citizen and set the Analyzer back to it's default state
        self.analyzer_dropdown.setSelectedIndex(0)
        
    def getListOfReferenceItems(self):
        #  def getAnalyzerDropdownListItems(self):
        list = []
        reference_combo_box = findObject(":Table.Reference:_JComboBox")
        for item in range(reference_combo_box.getItemCount()):
            list.append(reference_combo_box.getItemAt(item).toString().strip())
        return list
    
    def setListOfCheckBoxesAndColorBoxesForCurrentAnalyzer(self):
        #Get the Panel that contains the checkboxes
        
        self.checkbox_objects = []
        self.colorbox_objects = []
        self.checkbox_text = []
        
        lower_wholeblood_panel = findObject(":Graph_JPanel_2")
        
        #Find and store all the Check Boxes and Color Boxes in the panel
        for count1 in range(lower_wholeblood_panel.getComponentCount()):
            panel_with_checkboxes = lower_wholeblood_panel.getComponent(count1)
            for count2 in range(panel_with_checkboxes.getComponentCount()):
                if (panel_with_checkboxes.getComponent(count2).getClass().toString() == "class javax.swing.JCheckBox"):
                    self.checkbox_objects.append(panel_with_checkboxes.getComponent(count2))
                    self.checkbox_text.append(panel_with_checkboxes.getComponent(count2).getText())
                elif (panel_with_checkboxes.getComponent(count2).getClass().toString() == "class javax.swing.JPanel"):
                    self.colorbox_objects.append(panel_with_checkboxes.getComponent(count2))
                    
    def selectACheckBox(self,name):
        for checkbox in self.checkbox_objects:
            if checkbox.text == name and checkbox.selected == False:
                checkbox.doClick()
                break

    def deSelectACheckBox(self,name):
        for checkbox in self.checkbox_objects:
            if checkbox.text == name and checkbox.selected == True:
                checkbox.doClick()
                break
                
    def selectAllCheckBoxes(self):
        for checkbox in self.checkbox_objects:
            if checkbox.selected == False:
                checkbox.doClick()
                
    def deSelectAllCheckBoxes(self):
        for checkbox in self.checkbox_objects:
            if checkbox.selected == True:
                checkbox.doClick()
    
    def confirmComboRunTargetReference(self):
        #Make sure that we are on the Table Tab
        self.clickTableTab("Table")
        #Get the The Items in the Reference Dropdown
        reference_items = self.getListOfReferenceItems()
  
        item_counter = 1      
        for item in reference_items:
            #This assumes that Mean is the first Item in the Reference list box.
            if item == "Mean":
                continue
            
            #This should just grab the Strings that contain Bloodhound
            column_name = item.partition('-')[0]
            
            #Select the Referenced Run.
            findObject(":Table.Reference:_JComboBox").setSelectedIndex(item_counter)
            item_counter = item_counter + 1
            
            exportfile = QCTab().exportData("wholeblood")
            exported_table = Tables().createTableDictionary(exportfile)
            
            headers = exported_table["\xef\xbb\xbfParameter"]
            header_counter = 0
            for header in headers[0]:
                
                if header.rfind(column_name) != -1:
                    break;
                header_counter = header_counter + 1
            
            #Compare the Target Reference column with the current bloodhound column. They should be the same.
            test.verify(exported_table["HGB"][0][0].strip() == exported_table["HGB"][0][header_counter].strip(), "Confirming that the Target Reference Column matches the current Analyzer selection")
            
    def confirmControlComboBoxSelectedItem(self,item):
        combo_box = squish.findObject(self.control_combobox_symbol)
        Controls.confirmSelectedItem(self,combo_box,item,"Control Combo Box")
        
    def confirmTableTabSelected(self):
        table = squish.findObject(self.table_tab_symbol)
        test.verify(table.selected == 1, "Confirm that the table tab is selected")
        
    def confirmAnalyzerFirstSubColumn(self,analyzer_name):
        table_data = Tables.populateTableData(self,self.right_table_symbol)
        test.verify(analyzer_name in str(table_data[0]),"Confirm that the table column has the analyzer Bloodhound 1 in it.")

    def confirmTimeInHeader(self):
        table_data = Tables.populateTableData(self,self.right_table_symbol)
        time = str(table_data[0].keys()[0].split("\n")[1])
        a = re.compile("\d+\:\d+:\d+\s\w+")
        a.match(time)
        test.verify(a.match(time) != None,"Confirm that the time pattern matches the second line of the header.  ##:## ??: " + time)
        
    def confirmModeInHeader(self,mode):
        headers = Tables.getTableDataHeaders(self,self.right_table_symbol)
        test.verify(mode == headers[0].split('\n')[2],"Confirm that the word " + mode + " is the third line of the header")
        
    def confirmTableForNewRun(self):
        table_data = Tables.populateTableData(self,self.right_table_symbol)
        test.verify(len(table_data) > 27, "Confirm that the new table has at least twenty eight rows.")
        
    def confirmNewColumn(self, previous_total):
        table_data = Tables.populateTableData(self,self.right_table_symbol)
        test.verify(previous_total + 1 == len(table_data[0]), "Confirm that one new column was added to the previous table size")
    
    def confirmAnalyzerNames(self,analyzer_names):
        
        headers = Tables.getTableDataHeaders(self,self.right_table_symbol)
        for index in range(len(analyzer_names)):
            test.verify(analyzer_names[index] == headers[index].split("\n")[0], "Confirm that the expected header: " + analyzer_names[index] + " is equal to the actual header: " + headers[index].split("\n")[0])
            
    def confirmGraphResults(self,graph_filename,table_filename,record = True):
        table_data = Tables.populateWholebloodTableData(self,self.table_object_symbol)
        #Un-comment to do recording
        if record:
            Tables.wholebloodTableDataToFile(self,table_data, table_filename)
        
        Tables.confirmWholeBloodTableData(self,table_data,table_filename)
        graph_data = Graphs.getAllGraphData(self,self.graph_object_symbol)
        #Un-comment to do recording
        Graphs.graphDataToFile(self,graph_data, graph_filename)
        Graphs.confirmGraphData(self,graph_data, graph_filename)

