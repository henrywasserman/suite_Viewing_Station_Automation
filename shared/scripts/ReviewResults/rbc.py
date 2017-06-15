# -*- coding: utf-8 -*-
import test
import testData
import object
import objectMap
import squishinfo
import squish

from tables import Tables
from config import Config

class RBC(Tables):
    
    def __init__(self):
        version = Config().version
        self.object_symbol = ":Results.RBC_TabProxy"
        self.blood_cell_image_symbol = ":RBC_ListWithExtras"
        self.inspect_cell_dialog_symbol = ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.inspect_cell_dialog_comments_symbol = ":Bloodhound™ Viewing Station " + version + "_PlaceholderOverlay"
        self.inspect_cell_cancel_button_symbol = ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.overview_table_symbol = ":Report_JTable_5"
        self.rbcmorphology_table_symbol = ":Report_JTable_6"
        self.inclusions_table_symbol = ":Report_JTable_7"
        self.report_tab_comments_symbol = ":Report_PlaceholderOverlay_2"

    def clickTab(self):
        clickTab(self.object_symbol)
            
    def doubleClickFirstBloodSampleImage(self):
        counter = 0
        while(True):
            mouseClick(waitForObjectItem(self.blood_cell_image_symbol,"_0"), 27, 30, 0, Button.Button1)
            doubleClick(waitForObjectItem(self.blood_cell_image_symbol, "_0"), 27, 30, 0, Button.Button1)
            
            dialog_box = findObject(self.inspect_cell_dialog_symbol)
            #I am assuming in this case that if it's a layered dialog we have the Inspect Cell dialog
            if "LayeredDialog" in dialog_box.toString():
                break
            
            if counter == 30:
                break
            
            counter += 1
            
    def confirmReportTabCommentEditable(self,status):
        comments = findObject(self.report_tab_comments_symbol)
        if status == "editable":
            test.verify(comments.parent.editable == 1,"Verify that the Results Report Tab Comment Field is editable")
        else:
            test.verify(comments.parent.editable == 0, "Verify that the Results Report Tab Comment Field is not editable")
            
    def confirmCellDialogComments(self,status):
        comments = findObject(self.inspect_cell_dialog_comments_symbol)
        if status == "editable":
            test.verify(comments.parent.editable == True,"Confirm that the Dialog Comments are editable")
        else:
            test.verify(comments.parent.editable == False, "Confirm that the Dialog Comments are not editable")
            
    def clickInspectCellCancelButton(self):
        squish.clickButton(self.inspect_cell_cancel_button_symbol)
            
    def clickReportTab(self,object_symbol=":RBC.Report_TabProxy"):
        squish.clickTab(findObject(object_symbol))

    def confirmOverviewTableIsEditable(self,status):
        if status:
            Tables.confirmTableDataEditableState(self, self.overview_table_symbol,"editable")
        else:
            Tables.confirmTableDataEditableState(self, self.overview_table_symbol,"not_editable")
            
    def confirmRBCMorphologyTableIsEditable(self,status):
        if status:
            Tables.confirmTableDataEditableState(self, self.rbcmorphology_table_symbol,"editable")
        else:
            Tables.confirmTableDataEditableState(self, self.rbcmorphology_table_symbol,"not_editable")
            
    def confirmInclusionsTableIsEditable(self,status):
        if status:
            Tables.confirmTableDataEditableState(self, self.inclusions_table_symbol,"editable")
        else:
            Tables.confirmTableDataEditableState(self, self.inclusions_table_symbol,"not_editable")