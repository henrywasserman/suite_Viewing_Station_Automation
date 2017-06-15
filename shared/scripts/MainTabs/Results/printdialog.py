# -*- coding: utf-8 -*-
import glob
import os
import sys
import test
import testData
import object
import objectMap
import squishinfo
import squish

from images import Images
from startup import Startup
from config import Config

class PrintDialog:
    
    def __init__(self):
        version = Config().version
        self.print_button_symbol =              ":Bloodhound™ Viewing Station " + version + ".Print_JButton"
        self.cancel_button_symbol =             ":Bloodhound™ Viewing Station " + version + ".Cancel_JButton"
        self.paper_source_symbol =              ":Bloodhound™ Viewing Station " + version + ".Paper Source:_JComboBox"
        self.printer_combo_box_symbol =         ":Bloodhound™ Viewing Station " + version + ".Printer:_JComboBox"
        self.format_combo_box_symbol =          ":Bloodhound™ Viewing Station " + version + ".Format:_JComboBox"
        self.number_of_copies_symbol =          ":Bloodhound™ Viewing Station " + version + "_JTextField"
        self.collated_checkbox_symbol =         ":Bloodhound™ Viewing Station " + version + ".Collated_JCheckBox" 
        self.next_page_button_symbol =          ":Bloodhound™ Viewing Station " + version + ".→_JButton"
        self.previous_page_button_symbol =      ":Bloodhound™ Viewing Station " + version + ".←_JButton"
        self.first_page_button_symbol =         ":Bloodhound™ Viewing Station " + version + ".⇤_JButton"
        self.last_page_button_symbol =          ":Bloodhound™ Viewing Station " + version + ".⇥_JButton"
        self.print_dialog_panel =               ":Bloodhound™ Viewing Station " + version + "_JPanel_2"
        self.pages_symbol =                     ":Bloodhound™ Viewing Station " + version + ".1 of 2_JLabel"                   
        
        self.user = os.environ['USER']       
    
    def confirmFormatComboBox(self):
        test.verify(squish.findObject(self.format_combo_box_symbol).enabled == True,"Confirm that the Format ComboBox exists and is enabled")
        
    def confirmFormatComboBoxSelection(self,selection):
        test.verify(str(squish.findObject(self.format_combo_box_symbol).selecteditem) == selection,"Confirm that the Format ComboBox selection is " + selection)
        
    def confirmPrintDialogDoesNotExist(self):
        test.verify(squish.findObject(self.print_dialog_panel).visible == False,"Confirm that the print dialog box is not visible")
        
    def confirmPrintDialogAppears(self):
        test.verify(squish.findObject(self.print_dialog_panel).visible == True,"Confirm that the print dialog box is visible")

    def confirmLabOnlyRawItem(self):
        test.verify(str(squish.findObject(self.format_combo_box_symbol).selecteditem) == "Lab-only (Raw)","Confirm that the selected Item is 'Lab-only (Latest)'")

    def confirmPrinterComboBox(self):
        test.verify(squish.findObject(self.printer_combo_box_symbol).enabled == True, "Confirm that the Printer ComboBox exists and is enabled")

    def confirmNumberOfCopiesTextField(self):
        test.verify(squish.findObject(self.number_of_copies_symbol).enabled == True,"Confirm Number of Copies Text Field exists and is enabled")
    
    def confirmCollatedCheckbox(self):
        test.verify(squish.findObject(self.collated_checkbox_symbol).enabled == True,"Confirm Collated CheckBox exists and is enabled")
    
    def confirmPaperSourceComboBox(self):
        test.verify(squish.findObject(self.paper_source_symbol).editable == False,"Confirm Paper Source ComboBox exists and editable is disabled")
    
    def confirmFirstPageButton(self,status = "enabled"):
        self.confirmButton(self.first_page_button_symbol,status,"First Page")
        
    def clickFirstPageButton(self):
        squish.clickButton(self.first_page_button_symbol)
    
    def confirmPreviousPageButton(self, status ="enabled"):
        self.confirmButton(self.previous_page_button_symbol,status,"Previous Page")
        
    def clickPreviousPageButton(self):
        squish.clickButton(self.previous_page_button_symbol)
    
    def confirmNextPageButton(self,status = "enabled"):
        self.confirmButton(self.next_page_button_symbol,status,"Next Page")

    def clickNextPageButton(self):
        squish.clickButton(self.next_page_button_symbol)
    
    def confirmLastPageButton(self, status = "enabled"):
        self.confirmButton(self.last_page_button_symbol,status,"Laset Page")
        
    def clickLastPageButton(self):
        squish.clickButton(self.last_page_button_symbol)
    
    def confirmCancelButton(self):
        test.verify(squish.findObject(self.cancel_button_symbol).enabled == True,"Confirm Cancel Button exists and is enabled")
        
    def clickCancelButton(self):
        squish.clickButton(self.cancel_button_symbol)
    
    def confirmPrintButton(self):
        test.verify(squish.findObject(self.print_button_symbol).enabled == True,"Confirm Print Button exists and is enabled")
        
    def clickPrintButton(self):
        squish.clickButton(self.print_button_symbol)

    def confirmTotalPages(self,total):
        pages = squish.findObject(self.pages_symbol).text
        total_pages = int(pages.split(" ")[2])
        test.verify(total_pages == total,"Comparing number of total print pages with expected number")
                
    def moveDialogToTopCorner(self):
        squish.findObject(self.print_dialog_panel).setLocation(0,0)
        
    def selectAFormatComboItem(self,item_name):
        formatcombo = squish.findObject(self.format_combo_box_symbol)
        for index in range(formatcombo.getItemCount()):
            if str(formatcombo.getItemAt(index)) == item_name:
                formatcombo.setSelectedIndex(index)
                break
        
    def selectAPrinterComboItem(self,item_name):
        printercombo = squish.findObject(self.printer_combo_box_symbol)
        for index in range(printercombo.getItemCount()):
            if str(printercombo.getItemAt(index)) == item_name:
                printercombo.setSelectedIndex(index)
                break
            
    def confirmPaperSourceDropDownItems(self,items):
        self.confirmDropDowns(self.paper_source_symbol,items)
        
    def comparePrintReportScreenShot(self,screenshot):
        images = Images()
        #Adding this call to try to get the Control Bar out of the image that is created
        squish.findObject(self.print_dialog_panel).setLocation(0,0)
        test.vp(screenshot)
                
    def confirmFormatDropDownItems(self,items):
        self.confirmDropDowns(self.format_combo_box_symbol,items)
            
    def confirmPrintDropDownItems(self,items):
        self.confirmDropDowns(self.printer_combo_box_symbol,items)

    #Confirm that the Lab Only Item exists for each page in the print preview            
    def confirmLabOnlyForAnySample(self):
        pages = squish.findObject(self.pages_symbol).text
        total_pages = int(pages.split(" ")[2])
        for page in range(total_pages - 1 ):
            test.verify(str(squish.findObject(self.format_combo_box_symbol).getItemAt(0)) == "Lab-only (Raw)","Confirm Lab-only (Raw) as default Format")
            self.clickNextPageButton()
            
        for page in range(total_pages - 1 ):
            test.verify(str(squish.findObject(self.format_combo_box_symbol).getItemAt(0)) == "Lab-only (Raw)","Confirm Lab-only (Raw) as default Format")
            self.clickPreviousPageButton()

        
    def getTotalPagesToBePrinted(self,object_symbol):
        pages = squish.findObject(object_symbol).text
        total_pages = int(pages.split(" ")[2])
        return total_pages
        
    def observeEditableFieldDefaultedTo1(self):
        number_of_copies = squish.findObject(self.number_of_copies_symbol).text
        test.verify(number_of_copies == "1","Observe Editable Field that is defaulted to 1")
        
    def confirmDropDowns(self,object_symbol,items):
        drop_down_list = squish.findObject(object_symbol)
        item_array = items.split(",")
        item_dictionary = {}
        
        test.verify(drop_down_list.getItemCount() == len(item_array),"Confirm that the size of the expected dropdown list is equal to the size of the actual drop down list")
        
        #Create a dictionary
        for item in item_array:
            item_dictionary[item] = 0
        
        counter = 0
        for item in item_array:
            test.verify (item_dictionary[str(squish.findObject(object_symbol).getItemAt(counter))] == 0,
                "Confirming item " + item + " is in the expected item dictionary") 
            counter += 1
            
    def deletePrinterFiles(self):
        #First delete all pdf files in the user directory
        printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + self.user + '/*.pdf')
        for f in printerfiles:
            os.remove(f)
        
        #Next delete all jpg files in the user directory
        printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + self.user + '/*.jpg')
        for f in printerfiles:
            os.remove(f)

    def confirmButton(self,object_symbol,status,button_name):
        if status == "enabled":
            test.verify(squish.findObject(object_symbol).enabled == True,"Confirm that the " + button_name + " Button is enabled")
        elif status == "disabled":
            test.verify(squish.findObject(object_symbol).enabled == False,"Confirm that the " + button_name + " Button is disabled")
            
    def confirmPrintedPages(self):
        printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + self.user + '/*.pdf')
        for file in printerfiles:
            shared.system.pdfTojpg(file)
            
    def confirmTotalPrintedPages(self,total):
        counter = 0
        test_passed = False
        #Wait 30 Seconds to find the correct number of printed pages
        while (True):
            squish.snooze(1.0)
            printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + self.user + '/*.pdf')
            if len(printerfiles) == total:
                test_passed = True
                break
            counter += 1
            if counter == 30:
                break
            
            test.verify(test_passed,"Confirm that the number of expected printed pages " + str(total) + " is equal to the actual printed pages " + str(len(printerfiles)))
            
    def getPrintedFilesTotal(self,expected_total):
        
        counter = 0
        while(True):
            printerfiles = glob.glob(u'/Users/Shared/PDFwriter/' + self.user + '/*.pdf')
            if len(printerfiles) == expected_total:
                break
            squish.snooze(1.0)
            counter += 1
            #Wait for 30 seconds
            if counter == 30:
                break
        return printerfiles
            
            
        
        
        