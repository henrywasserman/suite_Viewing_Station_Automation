import test
import testData
import object
import objectMap
import os
import re
import subprocess
import squishinfo
import squish

class SpreadSheets(Tables):
    def compareSpreadsheets(self,expected,actual,medical_record = ''):        
        test.log("medical record: " + medical_record)
        test.log("expected spreadsheet: " + expected)
        test.log("actual spreadsheet: " + actual)
        
        #Get the filename without the extension
        base = os.path.basename(expected)
        filename = os.path.splitext(expected)[0]
        
        #Bring in the Spreadsheet Testdata
        expected_dataset = testData.dataset(expected)
        actual_dataset = testData.dataset(actual)
        
        _4711_dataset = testData.dataset(filename + "_4711.xls")
        _4712_dataset = testData.dataset(filename + "_4712.xls")
        
        if not medical_record == '':
            _4711_no_medical_record_dataset = testData.dataset(filename + "_4711_no_medical_record.xls")
            _4712_no_medical_record_dataset = testData.dataset(filename + "_4712_no_medical_record.xls")
        
        for fieldname in testData.fieldNames(expected_dataset[-1]):
            
            if "Time" in fieldname:
                continue
            if "Date" in fieldname:
                continue
            if "Accession" in fieldname:
                continue
            if "Analyzer" in fieldname:
                continue
            if "Released by User" in fieldname:
                continue
            
            for index in range(len(expected_dataset)):
                #Since Vadim does not want too many verifications - We are only going to report on tests here that fail.
                spreadsheet_compare_tests_passed = True

                if "Status" in fieldname or \
                    "Mode" in fieldname or \
                    "Archived By User" in fieldname:
                                        
                    if not testData.field(expected_dataset[index],fieldname) == testData.field(actual_dataset[index],fieldname):
                        spreadsheet_compare_tests_passed = False
                        test.verify(testData.field(expected_dataset[0],fieldname) == 
                                    testData.field(actual_dataset[index],fieldname),
                                    "Confirming against expected data in row " + str(index) + " for fieldname "  + fieldname
                                    + " expected: " + testData.field(expected_dataset[0],fieldname) 
                                    + " actual: " + testData.field(actual_dataset[index],fieldname))
                        
                elif not "Medical Record #" in testData.fieldNames(actual_dataset[index]):
                    if medical_record == '4711':
                        no_medical_record_dataset = _4711_no_medical_record_dataset
                        
                    if medical_record == '4712':
                        no_medical_record_dataset = _4712_no_medical_record_dataset
                        
                    try:
                        testData.field(no_medical_record_dataset[index],fieldname)
                    except NameError:
                        test.log("Known Bug, don't yet have a mantis number.  Could not find: " + fieldname)
                        continue
                        
                    if not testData.field(no_medical_record_dataset[0],fieldname) == testData.field(actual_dataset[index],fieldname):
                        
                        spreadsheet_compare_tests_passed = False
                        
                        test.verify(testData.field(no_medical_record_dataset[0],fieldname) == 
                            testData.field(actual_dataset[index],fieldname),
                            "Confirming against expected data in row " + str(index) + " for fieldname "  + fieldname
                            + " expected: " + testData.field(no_medical_record_dataset[0],fieldname)
                            + " actual: " + testData.field(actual_dataset[index],fieldname))


                elif testData.field(actual_dataset[index],'Medical Record #') == "4711":
                    
                    if not testData.field(_4711_dataset[0],fieldname) == testData.field(actual_dataset[index],fieldname):
                        
                        spreadsheet_compare_tests_passed = False
                        
                        test.verify(testData.field(_4711_dataset[0],fieldname) == 
                            testData.field(actual_dataset[index],fieldname),
                            "Confirming against expected data in row " + str(index) + " for fieldname "  + fieldname
                            + " expected: " + testData.field(_4711_dataset[0],fieldname)
                            + " actual: " + testData.field(actual_dataset[index],fieldname))
                elif testData.field(actual_dataset[index],'Medical Record #') == "4712":
                    
                    try:
                
                        if not testData.field(_4712_dataset[0],fieldname) == testData.field(actual_dataset[index],fieldname):
                    
                            spreadsheet_compare_tests_passed = False
                        
                            test.verify(testData.field(_4712_dataset[0],fieldname) == 
                                        testData.field(actual_dataset[index],fieldname),
                                        "Confirming against expected data in row " + str(index) + " for fieldname "  + fieldname
                                        + " expected: " + testData.field(_4712_dataset[0],fieldname) 
                                        + " actual: " + testData.field(actual_dataset[index],fieldname))
                    except NameError:
                        test.fail("The " + fieldname + " column does not exist in  " + filename + "_4712.xls")
                        spreadsheet_compare_tests_passed = False
            if spreadsheet_compare_tests_passed:
                test.verify(spreadsheet_compare_tests_passed,"Spreadsheet Compare test for column " + fieldname + " is " + str(spreadsheet_compare_tests_passed))
                
    def compareSpreadSheetToTableData(self,table_data,actual, start_index):
        
        actual_dataset = testData.dataset(actual)
        
        for fieldname in testData.fieldNames(actual_dataset[-1]):
            for index in range(len(actual_dataset)):
                
                table_data_fieldname = fieldname
                
                if fieldname == 'Patient Name':
                    table_data_fieldname = "Name"
                elif fieldname == 'Medical Record #':
                    table_data_fieldname = 'Medical\nRecord #'
                elif fieldname == 'Dept.':
                    table_data_fieldname = 'Location'
                #Skipping Sex fieldname for now - Gender is found in the Results Tab
                #Will need to persist this info for each row selected
                elif fieldname == 'Sex':
                    continue
                #Skipping Data of Birth until I find out where that comes from
                elif fieldname == "Date of Birth":
                    continue
                
                self.confirmFieldName(table_data, actual_dataset, index, start_index, table_data_fieldname,  fieldname)
        
    def confirmFieldName(self, table_data, actual_dataset, index, start_index, table_data_fieldname, fieldname):
        
        #Have to do some math here because each row can have multiple analyzers
        #Coding this up right now for two analyzers only
        if index == 0 or index == 1:
            table_index = 0        
        else:
            table_index = (index - (index % 2)) / 2
        test.verify(table_data[table_index + start_index][table_data_fieldname] == 
            testData.field(actual_dataset[index],fieldname),
            "Confirming against expected data in row " + str(index) + " for fieldname "  + fieldname
            + " expected: " +  table_data[table_index + start_index][table_data_fieldname]
            + " actual: " + testData.field(actual_dataset[index], fieldname))
        
    def openExcelAndSaveFile(self,export_file):
        test.log("First delete the file if it exists")
        self.run_this_scpt(
            "tell application \"Microsoft Excel\"\r\
                open \"" + export_file + ".txt\"\r \
                set wb to active workbook \r\
                set fn to (POSIX file \"" + export_file + ".xls\") as string\r\
                save workbook as wb filename fn file format Excel7 file format overwrite yes\r\
                quit\r\
            end tell"
    )
        
    def run_this_scpt(self,scpt, args=[]):
        p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate(scpt)
        return stdout