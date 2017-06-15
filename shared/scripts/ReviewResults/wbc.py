# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables
from inspectcellsdialog import InspectCellsDialog
from config import Config

class WBC(Tables):
    
    def __init__(self):
        version = Config().version
        self.report = {}
        self.report["Auer Rods"]                                =       ["true","false","false","false","false"]
        self.report["Döhle Bodies"]                             =       ["true","false","false","false","false"]
        self.report["Hypo/ Agranular GranulocytesNeutrophils"]  =       ["true","false","false","false","false"]
        #self.report["Agran/Hypogranular Neutrophils"]           =       ["true","false","false","false","false"]
        self.report["Toxic Granulation"]                        =       ["true","false","false","false","false"]
        self.report["Hyposegmentation"]                         =       ["true","false","false","false","false"]
        self.report["Hypersegmentation"]                        =       ["true","false","false","false","false"]
        self.report["Toxic Vacuolation"]                        =       ["true","false","false","false","false"]
        self.report["Smudge Cells"]                             =       ["true","false","false","false","false"]
        
        self.report_array = [
                             "Auer Rods",
                             "Döhle Bodies",
                             "Hypo/ Agranular GranulocytesNeutrophils",
                             "Toxic Granulation",
                             "Hyposegmentation",
                             "Hypersegmentation",
                             "Toxic Vacuolation",
                             "Smudge Cells"
                             ]
        
        self.object_symbol                              =       ":Results.WBC_TabProxy_2"
        self.blood_image_symbol                         =       ":Neutrophil (96.0%)_ListWithExtras"
        self.reclassify_combobox_symbol                 =       ":Bloodhound™ Viewing Station " + version + "_JComboBox"
        self.inspect_cell_dialog_comments_symbol        =       ":Bloodhound™ Viewing Station " + version + "_PlaceholderOverlay"
        self.inspect_cell_dialog_symbol                 =       ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.inspect_cell_cancel_button_symbol          =       ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.general_table_symbol                       =       ":Report_JTable"
        self.neutrophils_table_symbol                   =       ":Report_JTable_2"
        self.report_tab_comments_symbol                 =       ":Report_PlaceholderOverlay"
        self.neutrophils_images_symbol                  =       ":Neutrophil (2.2%)_ListWithExtras"
        self.gallery_symbol                             =       ":WBC_ScrollablePanel"
        self.report_tab_symbol                          =       ":WBC.Report_TabProxy"
        
        self.inspectcellsdialog = InspectCellsDialog()
    
    def clickTab(self, object_symbol = ":Results.WBC_TabProxy_2"):
        squish.clickTab(waitForObject(object_symbol))
        
    def clickInspectCellCancelButton(self):
        squish.clickButton(self.inspect_cell_cancel_button_symbol)
        
    def doubleClickFirstBloodSampleImage(self):
        counter = 0
        while(True):
            mouseClick(waitForObjectItem(self.blood_image_symbol,"_0"), 77, 64, 0, Button.Button1)
            doubleClick(waitForObjectItem(self.blood_image_symbol, "_0"), 77, 64, 0, Button.Button1)
            
            dialog_box = findObject(self.inspect_cell_dialog_symbol)
            #I am assuming in this case that if it's a layered dialog we have the Inspect Cell dialog
            if "LayeredDialog" in dialog_box.toString():
                break
            
            if counter == 30:
                break
            
            counter += 1
            
    def confirmCellDialogComments(self,status):
        comments = findObject(self.inspect_cell_dialog_comments_symbol)
        if status == "editable":
            test.verify(comments.parent.editable == True,"Confirm that the Dialog Comments are editable")
        else:
            test.verify(comments.parent.editable == False, "Confirm that the Dialog Comments are not editable")
        
    def clickReportTab(self,object_symbol=":WBC.Report_TabProxy"):
        squish.clickTab(findObject(object_symbol))
    
    #TODO When we need more functionality, this needs to be changed from being hard coded mouseclicks    
    def checkAndUncheckOptions(self):
        #This was recorded to click a few things on the WBC Report Table inside the Results Tab
        mouseClick(waitForObjectItem(":Report_JTable", "0/2"), 13, 11, 0, Button.Button1)
        test.log("Changed Auer Rods to 1+ ie true")
        self.report["Auer Rods"] = ["false","true","false","false","false"]

        mouseClick(waitForObjectItem(":Report_JTable", "2/2"), 17, 9, 0, Button.Button1)
        test.log("Hypo/ Agranular GranulocytesNeutrophils to 1+ ie true")
        self.report["Hypo/ Agranular GranulocytesNeutrophils"] = ["false","true","false","false","false"]
        
        mouseClick(waitForObjectItem(":Report_JTable", "4/2"), 17, 9, 0, Button.Button1)
        test.log("Changed Hyposegmentation to 1+ ie true")
        self.report["Hyposegmentation"] = ["false","true","false","false","false"]
        
        mouseClick(waitForObjectItem(":Report_JTable", "6/2"), 17, 9, 0, Button.Button1)
        test.log("Changed Toxic Vacuolation to 1+ ie true")
        self.report["Toxic Vacuolation"] = ["false","true","false","false","false"]
                
    def setAuerRods(self,state):
        for index in range(len(state)):
            if(not state[index] == self.report["Auer Rods"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","0/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Auer Rods"][index] = state[index]
                
    def setDohleBodies(self,state):
        for index in range(len(state)):
            if(not state[index] == self.report["Döhle Bodies"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","1/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Döhle Bodies"][index] = state[index]
                
    def setHypoAgranular(self,state):
        for index in range(len(state)):
            if(not state[index] == self.report["Hypo/ Agranular GranulocytesNeutrophils"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","2/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Hypo/ Agranular GranulocytesNeutrophils"][index] = state[index]
                
    def setToxicGranulation(self,state):
        for index in range(len(state)):
            if(not state[index] == self.report["Toxic Granulation"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","3/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Toxic Granulation"][index] = state[index]
                
    def setHyposegmentation(self,state):
        for index in range(len(state)):        
            if(not state[index] == self.report["Hyposegmentation"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","4/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Hyposegmentation"][index] = state[index]

    def setHypersegmentation(self,state):
        for index in range(len(state)):        
            if(not state[index] == self.report["Hypersegmentation"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","5/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Hypersegmentation"][index] = state[index]
                
    def setToxicVacuolation(self,state):
        for index in range(len(state)):
            if(not state[index] == self.report["Toxic Vacuolation"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","6/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Toxic Vacuolation"][index] = state[index]
                
    def setSmudgeCells(self,state):
        for index in range(len(state)):
            if(not state[index] == self.report["Smudge Cells"][index]):
                mouseClick(waitForObjectItem(":Report_JTable","7/" + str(index + 1)), 13, 11, 0, Button.Button1)
                self.report["Smudge Cells"][index] = state[index]
                
    def confirmGeneralTableIsEditable(self,status):
        if status:
            Tables.confirmTableDataEditableState(self, self.general_table_symbol,"editable")
        else:
            Tables.confirmTableDataEditableState(self, self.general_table_symbol,"not_editable")
        
    def confirmNeutrophilsTableIsEditable(self,status):
        if status:
            Tables.confirmTableDataEditableState(self, self.neutrophils_table_symbol,"editable")
        else:
            Tables.confirmTableDataEditableState(self, self.neutrophils_table_symbol,"not_editable")
        
    def confirmCorrespondingReportChanges(self):
        #Get the General Table
        self.confirmCheckboxes(":Report_JTable_4")
        test.log("The table below no longer exists as of 2/25/2014")                    
        #Get the Neutrophils Table
        #self.confirmCheckboxes(":Report_JTable_3")
        
    def confirmCheckboxes(self,object_symbol):
        table = findObject(object_symbol)
        #Confirm that the checkboxes are the ones expected.
        for row in range(table.getRowCount()):
            for column in range(table.getColumnCount()):
                if column == 0:
                    continue
                
                row_value = str(table.getValueAt(row,column))
                expected_value = self.report[self.report_array[row]][column - 1 ]
                test.verify(expected_value == row_value,"Confirm that the expected checkbox value: " + str(expected_value) + " is equal to actual value: " + str(row_value) + " for " + self.report_array[row] + " column " + str(column - 1 ))

    def confirmReportTabCommentEditable(self,status):
        comments = findObject(self.report_tab_comments_symbol)
        if status == "editable":
            test.verify(comments.parent.editable == 1,"Verify that the Results Report Tab Comment Field is editable")
        else:
            test.verify(comments.parent.editable == 0, "Verify that the Results Report Tab Comment Field is not editable")

    def hightlightNeutrophilsCells(self,total):
        for index in range(total):
            mouseClick(waitForObjectItem(self.neutrophils_images_symbol, "_" + str(index)), 86, 62, 1, Button.Button1)
        
        nativeType(" ")
        
    def confirmNewLine(self,name):
        gallery = findObject(self.gallery_symbol)
        
        field = gallery.getClass().getDeclaredField("tabs")
        field.setAccessible(True)
        tabs = field.get(gallery)
        
        tabs_array = tabs.keySet().toArray()
        
        found_name = False
        for index in range(tabs_array.length):
            if str(tabs_array.at(index)) == name:
                found_name = True
                break
            
        test.verify(found_name,"Confirm that " + name + " was found in the WBC gallery") 
            
    def resetReportArray(self):
        self.report["Auer Rods"]                                =       ["true","false","false","false","false"]
        self.report["Döhle Bodies"]                             =       ["true","false","false","false","false"]
        self.report["Hypo/ Agranular GranulocytesNeutrophils"]  =       ["true","false","false","false","false"]
        #self.report["Agran/Hypogranular Neutrophils"]           =       ["true","false","false","false","false"]
        self.report["Toxic Granulation"]                        =       ["true","false","false","false","false"]
        self.report["Hyposegmentation"]                         =       ["true","false","false","false","false"]
        self.report["Hypersegmentation"]                        =       ["true","false","false","false","false"]
        self.report["Toxic Vacuolation"]                        =       ["true","false","false","false","false"]
        self.report["Smudge Cells"]                             =       ["true","false","false","false","false"]
                