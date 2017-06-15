# -*- coding: utf-8 -*-
import csv
import test
import testData
import object
import objectMap
import re
import squishinfo
import squish
import __builtin__

class Tables(__builtin__.object):
    
    def __init__(self):
        self.table = 0
        self.table_data = []
    
    def createTableDictionary(self,inputfile):
        table = {}
        with open(inputfile,'r') as infile:
            for line in infile:
                line_array = line.split('\t')
                parameter = line_array.pop(0)
                table[parameter] = [line_array]
        return table
    
    def populateTableDataWithAllRowsEqualToReadyforRelease(self,object_symbol):
        self.clickTab()
        self._waitForTableStatusReadyForRelease(object_symbol)
        
    def populateTableData(self,object_symbol):
        self.table_data = []
        self.table = squish.findObject(object_symbol)
        table_header = self.table.getTableHeader()
        for row in range(self.table.getRowCount()):
            row_data = {}
            for column in range(self.table.getColumnCount()):
                header = self.removeNonAscii(table_header.getColumnModel().getColumn(column).getHeaderValue().toString())
                row_data[header] = self.removeNonAscii(str(self.table.getValueAt(row,column)))
                
            self.table_data.append(row_data)
        
        return self.table_data
    
    def getTableDataHeaders(self,object_symbol):
        table_data_headers = []
        self.table = squish.findObject(object_symbol)
        table_header = self.table.getTableHeader()
        for row in range(self.table.getRowCount()):
            for column in range(self.table.getColumnCount()):
                table_data_headers.append(self.table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString())
                
        return table_data_headers
            
    def confirmTableDataEditableState(self,object_symbol,status):
        self.table = squish.findObject(object_symbol)
        if status == "editable":
            #Not sure what to do here for editable.  Need a use case before coding.
            snooze(1.0)
        else:
            for row in range(self.table.getRowCount()):
                for column in range(self.table.getColumnCount()):
                    test.verify(self.table.isCellEditable(row,column) == 0, "Confirm that row " + str(row) + " and column " + str(column) + " is not editable")
        
    def compareStatusIcon(self):
        test.verify(True)
            
    #Wait for the status for each row to be Ready for Release
    #And at the same time Populate Table
    def _waitForTableStatusReadyForRelease(self,object_symbol):
        counter = 0
        while (not object.exists(object_symbol)):
            AnalyzerEventsDialog().dismissAnalyzerEvents()
            snooze(1.0)
            counter = counter + 1
            if counter == 300:
                break
        #Now make sure all rows are in the ready state
        counter = 0
        ready = False
        while (not ready):
            squish.snooze(1.0)
            self.table_data = []
            counter += counter
            if counter == 300:
                test.fail("Waiting for Ready for Release Timed Out")
                break
            self.table= squish.findObject(object_symbol)
            table_header = self.table.getTableHeader()
            for row in range(self.table.getRowCount()):
                row_data = {}
                for column in range(self.table.getColumnCount()):
                    try:
                        row_data[self.table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString()] \
                        = str(self.table.getValueAt(row,column))
                        if row_data["Status"] != "Ready for Release":
                            break;
                    except:
                        pass
                else:
                    self.table_data.append(row_data)
                    continue
                break
            else:
                if row + 1 == self.table.getRowCount():
                    ready = True
                    test.verify(ready,"Confirm that all rows in the table are in the Ready for Release state")
                continue
            
    #Wait for the status for each row to be Ready for Release or Awaiting Review
    #And at the same time Populate Table
    def waitForTableStatusReadyForReleaseOrAwaitingReview(self,object_symbol):
        counter = 0
        while (not object.exists(object_symbol)):
            AnalyzerEventsDialog().dismissAnalyzerEvents()
            snooze(1.0)
            counter = counter + 1
            if counter == 300:
                break
        #Now make sure all rows are in the ready state
        counter = 0
        ready = False
        while (not ready):
            squish.snooze(1.0)
            self.table_data = []
            counter += counter
            if counter == 300:
                test.fail("Waiting for Ready for Release or Awaiting Review Timed Out")
                break
            self.table= squish.findObject(object_symbol)
            table_header = self.table.getTableHeader()
            for row in range(self.table.getRowCount()):
                row_data = {}
                for column in range(self.table.getColumnCount()):
                    try:
                        row_data[self.table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString()] \
                        = str(self.table.getValueAt(row,column))
                        if (row_data["Status"] != "Ready for Release") and row_data["Status"] != "Awaiting Review":
                            break;
                    except:
                        pass
                else:
                    self.table_data.append(row_data)
                    continue
                break
            else:
                if row + 1 == self.table.getRowCount():
                    ready = True
                    test.verify(ready,"Confirm that all rows in the table are in the Ready for Release state")
                continue
        
    def getTableData(self):
        return self.table_data
    
    def getHeaders(self,object_symbol):
        headers = []
        table = squish.findObject(object_symbol)
        header = table.getTableHeader().getColumnModel()
        
        for index in range(header.getColumnCount()):
            headers.append(header.getColumn(index).getHeaderValue().toString())
            
        return headers
    
    def getAccessionNumberByIndex(self,index):
        return self.table_data[index]["Accession #"]
    
    def clickOnTableRow(self,status):
        test.log("Here is status: " + status)
        counter = 0
        for row in self.table_data:
            if row["Status"] == status:
                test.log("Here is row status: " + row["Status"])
                self.table.setRowSelectionInterval(counter,counter)
                break
            counter += 1
        return counter
            
    def selectTableRows(self,start_index, end_index, object_symbol = 'default'):
        if object_symbol == 'default':
            self.table.setRowSelectionInterval(start_index,end_index)
        else:
            table = squish.findObject(object_symbol)
            table.setRowSelectionInterval(start_index,end_index)
            
    def clickOnRowByMedicalRecord(self,medical_record):
        counter = 0
        for row in self.table_data:
            if row["Medical\nRecord #"] == medical_record:
                self.table.setRowSelectionInterval(counter,counter)
                break
            counter += 1
        return counter
            
    def doubleClickOnTableRow(self,row):
        squish.mouseClick(object.children(object.children(self.table)[0])[row],11,15,0,squish.Button.Button1)
        squish.doubleClick(object.children(object.children(self.table)[0])[row],11,16,0,squish.Button.Button1)
        
    def doubleClickOnTableRowByName(self,object_symbol,field_name, cell_value):
        counter = 0
        for row in self.table_data:
            if row[field_name] == cell_value:
                squish.mouseClick(squish.waitForObjectItem(object_symbol, str(counter) + "/0"), 52, 13, 0, squish.Button.Button1)
                squish.doubleClick(squish.waitForObjectItem(object_symbol, str(counter) + "/0"), 52, 13, 0, squish.Button.Button1)
                break
            counter += 1
            
    def clickOnTableRowByName(self,object_symbol,field_name, cell_value):
        counter = 0
        Tables.populateTableData(self,object_symbol)
        for row in self.table_data:
            if row[field_name] == cell_value:
                squish.mouseClick(squish.waitForObjectItem(object_symbol, str(counter) + "/0"), 40, 15, 0, squish.Button.Button1)
                break
            counter += 1
        return row
        
    def clickOnTableCellByIndex(self,object_symbol,x,y):
        squish.mouseClick(squish.waitForObjectItem(object_symbol, str(x) + "/" + str(y)), 52, 13, 0, squish.Button.Button1)
    
    def waitToClickOnTableRowByName(self,object_symbol,field_name, cell_value):
        timer_counter = 0
        found = False
        timed_out = False
        while(not found and not timed_out):
            self.table_data = []
            Tables.populateTableData(self,object_symbol)
            counter = 0
            for row in self.table_data:
                if row[field_name] == cell_value:
                    squish.mouseClick(squish.waitForObjectItem(object_symbol, str(counter) + "/0"), 40, 15, 0, squish.Button.Button1)
                    found = True
                    break
                counter += 1
                timer_counter += 1
                if timer_counter == 300:
                    timed_out = True
                    
        return row
            
    def getTableRowByName(self,object_symbol,field_name, cell_value):
        Tables.populateTableData(self,object_symbol)
        counter = 0
        for row in self.table_data:
            if row[field_name] == cell_value:
                break
            counter +=1
        return row

    def clickOnTableRowIndex(self, row):
        squish.mouseClick(object.children(object.children(self.table)[row])[0],11,15,0,squish.Button.Button1)
        
    #Wait until the status shows up in x number of rows
    def waitForTableStatusCount(self,object_symbol,status,count):
        counter = 0
        while (not object.exists(object_symbol)):
            AnalyzerEventsDialog().dismissAnalyzerEvents()
            snooze(1.0)
            counter = counter + 1
            if counter == 300:
                break
        #Now make sure all rows are in the ready state
        counter = 0
        ready = False
        while (not ready):
            squish.snooze(1.0)
            self.table_data = []
            counter += counter
            if counter == 300:
                test.fail("Waiting for " + status + " Timed Out")
                break
            self.table = squish.findObject(object_symbol)
            table_header = self.table.getTableHeader()
            status_counter = 0
            for row in range(self.table.getRowCount()):
                row_data = {}
                for column in range(self.table.getColumnCount()):
                    try:
                        row_data[self.table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString()] \
                        = str(self.table.getValueAt(row,column))
                        if row_data["Status"] != status:
                            status_counter += 1
                    except:
                        pass
            if count == status_counter:
                ready = True

    def getSideBarText(self,object_symbol):
        sidebartext = []
        wraplist = squish.findObject(object_symbol)
        
        for index in range(wraplist.getComponentCount()):
            field = wraplist.getComponent(index).getClass().getDeclaredField("toRender")
            field.setAccessible(True)
            
            #Check to see if we have a special text string that uses the AttributedStringIterator
            if "AttributedStringIterator" in field.get(wraplist.getComponent(index)).asList().iterator().next().toString():
                it = field.get(wraplist.getComponent(index)).asList().iterator().next()
                sidebar_info = ''
                for index in range(it.getEndIndex()):
                      char = it.setIndex(index)
                      sidebar_info = sidebar_info + chr(int(str(char)))
                      
            else:
                sidebar_info = field.get(wraplist.getComponent(index))
            
            sidebartext.append(sidebar_info)
                                    
        return sidebartext
    
    def getSideBarTextByIndex(self,index,status):
        self.clickOnTableRow(status)
        sidebar_class = self.getSideBarText()[index]
        if hasattr(sidebar_class, 'getClass') and 'javax.swing.JButton' in sidebar_class.toString():
            text = sidebar_class.get(0).toString()
        elif hasattr(sidebar_class, 'getClass') and sidebar_class.getClass().toString() == "class com.google.common.collect.RegularImmutableList":
            text = sidebar_class.get(1).toString()
        elif hasattr(sidebar_class, 'getClass') and sidebar_class.getClass().toString() == "class com.google.common.collect.SingletonImmutableList":
            text = sidebar_class.get(0).toString() 
        else: 
            text = sidebar_class[index]
            
        return text
            
    
    def confirmSideBarText(self,index,pattern):
        #TODO This is not the best way to do this because
        #index could throw 'exceptions.IndexError'
        #Let's see how it goes
        counter = 0
        while (True):
            sidebartext = self.getSideBarTextByIndex(index,"Ready for Release")
            ## Confirm that the sidebar text matches pattern
            individual_run_status_pattern = re.compile('.*Individual run status.*')
            accession_number_pattern = re.compile('^\w+$')
            sample_pattern = re.compile(pattern)
            #For Now recurse if we see 'Individual run status
            if individual_run_status_pattern.match(str(sidebartext)) != None or \
                    accession_number_pattern.match(str(sidebartext)) != None:
                squish.snooze(1.0)
                counter += 1
                index += 1
            else:
                break
            if counter == 300:
                test.fail("tables.py confirmSideBarText timed out because it kept finding 'Individual run status'")
                
        test.verify(sample_pattern.match(str(sidebartext)) != None,"Confirm that the sidebar text " + str(sidebartext) + " contains " + pattern)

    def confirmNameColumnSortOrder(self,table_symbol,column,sort_order):
        sortkeys = squish.findObject(table_symbol).getRowSorter().getSortKeys()
        test.verify(column == sortkeys.get(0).getColumn(),"Confirm that the correct column " + str(column) + " is being sorted")
        test.verify(sort_order == str(sortkeys.get(0).getSortOrder()),"Confirm that the correct order " + sort_order + " is being used")
        
    def enterDigiCountTableData(self,table_object,filename):
        f = open(filename)
        reader = csv.reader(f,delimiter = ',')
        
        digicount_dictionary = {}
        
        for data in reader:
            digicount_dictionary[data[0].split(' ',1)[0]] = data[1:]
        
        f.close()
                
        for row in range(table_object.getRowCount()):
            for column in range(table_object.getColumnCount()):
                if column == 0:
                    continue
                if digicount_dictionary[str(table_object.getValueAt(row,0).getDisplayName())][column - 1] != '' and column != 5:
                    table_object.setValueAt(digicount_dictionary[str(table_object.getValueAt(row,0).getDisplayName())][column - 1],row,column)
                
    def csvToDictionary(self,filename):
        f = open(filename)
        
        reader = csv.reader(f,delimiter = ',')
        
        digicount_dictionary = {}
        
        for data in reader:
            digicount_dictionary[data[0].split(' ',1)[0]] = data[1:]
            
        f.close()
        
        return digicount_dictionary
    
    def confirmDigiCountTabTableData(self, table_object, filename):
        digicount_dictionary = self.csvToDictionary(filename)
        
        for row in range(table_object.getRowCount()):
            for column in range(table_object.getColumnCount()):
                if column == 0:
                    test.verify(str(table_object.getValueAt(row,column)) in digicount_dictionary, "Confirm that the the Parameter String " + str(table_object.getValueAt(row,column)) + " exists in the expected test table")
                elif digicount_dictionary[str(table_object.getValueAt(row,0))][column - 1] == '':
                    test.verify('<null>' == str(table_object.getValueAt(row,column)) or '' == str(table_object.getValueAt(row,column)),"Confirm that the expected cell value: <null> is equal to the actual cell value: " + str(table_object.getValueAt(row,column)))
                elif column == 2:
                    mean = self.removeNonAscii(str(table_object.getValueAt(row,1)))
                    range_value = digicount_dictionary[str(table_object.getValueAt(row,0))][column - 1]
                    
                    parameter = self.removeNonAscii(str(table_object.getValueAt(row,0)))
                    
                    if 'WBC' == parameter or 'RBC' == parameter or '%RET' == parameter or '#RET' == parameter:
                        low_range = "{0:.2f}".format(float(mean) - float(range_value))
                        high_range = "{0:.2f}".format(float(mean) + float(range_value))
                    elif 'PLT' == parameter:
                        low_range = "{0:.0f}".format(float(mean) - float(range_value))
                        high_range = "{0:.0f}".format(float(mean) + float(range_value))
                    else:
                        low_range = "{0:.1f}".format(float(mean) - float(range_value))
                        high_range = "{0:.1f}".format(float(mean) + float(range_value))
                        
                    range_string = low_range + " - " + high_range
                    test.verify(range_string == str(table_object.getValueAt(row,column)),"Confirm that for " + parameter + " the expected cell value: " + range_string + " is equal to the actual cell value: " + str(table_object.getValueAt(row,column)))                    
                else:
                    test.verify(digicount_dictionary[str(table_object.getValueAt(row,0))][column - 1] == self.removeNonAscii(str(table_object.getValueAt(row,column))),"Confirm that the expected cell value: " + digicount_dictionary[str(table_object.getValueAt(row,0))][column - 1] + " is equal to the actual cell value " + str(table_object.getValueAt(row,column)))

    
    def confirmDigiCountTableData(self, table_object, filename):
        digicount_dictionary = self.csvToDictionary(filename)
        
        for row in range(table_object.getRowCount()):
            for column in range(table_object.getColumnCount()):
                if column == 0:
                    test.verify(str(table_object.getValueAt(row,column).getDisplayName()) in digicount_dictionary, "Confirm that the the Parameter String " + str(table_object.getValueAt(row,column).getDisplayName()) + " exists in the expected test table")
                elif digicount_dictionary[str(table_object.getValueAt(row,0).getDisplayName())][column - 1] == '':
                    test.verify('<null>' == str(table_object.getValueAt(row,column)),"Confirm that the expected cell value: <null> is equal to the actual cell value: " + str(table_object.getValueAt(row,column)))
                elif column == 2:
                    mean = table_object.getValueAt(row,1)
                    range_value = digicount_dictionary[str(table_object.getValueAt(row,0).getDisplayName())][column - 1]
                    
                    parameter = self.removeNonAscii(str(table_object.getValueAt(row,0)))
                    
                    if 'WBC (10/L)' == parameter or 'RBC (10/L)' == parameter or '%RET (%)' == parameter or '#RET (10/L)' == parameter:
                        low_range = "{0:.2f}".format(float(str(mean)) - float(range_value))
                        high_range = "{0:.2f}".format(float(str(mean)) + float(range_value))
                    elif 'PLT (10/L)' == parameter:
                        low_range = "{0:.0f}".format(float(str(mean)) - float(range_value))
                        high_range = "{0:.0f}".format(float(str(mean)) + float(range_value))
                    else:
                        low_range = "{0:.1f}".format(float(str(mean)) - float(range_value))
                        high_range = "{0:.1f}".format(float(str(mean)) + float(range_value))
                        
                    range_string = low_range + " - " + high_range
                    test.verify(range_string == str(table_object.getValueAt(row,column)),"Confirm that for " + parameter + " the expected cell value: " + range_string + " is equal to the actual cell value: " + str(table_object.getValueAt(row,column)))                    
                else:
                    test.verify(digicount_dictionary[str(table_object.getValueAt(row,0).getDisplayName())][column - 1] == str(table_object.getValueAt(row,column)),"Confirm that the expected cell value: " + digicount_dictionary[str(table_object.getValueAt(row,0).getDisplayName())][column - 1] + " is equal to the actual cell value" + str(table_object.getValueAt(row,column)))
                    
    def digiCountTableDataToCSV(self, table_object, filename):
                
        f = open(filename,'w')
        
        for row in range(table_object.getRowCount()):
            for column in range(table_object.getColumnCount()):
                if column == 0:
                    f.write(str(table_object.getValueAt(row,column).getDisplayName()) + ",")
                elif str(table_object.getValueAt(row,column)) == "<null>":
                    f.write(",")
                elif column == table_object.getColumnCount() - 1:
                    f.write(str(table_object.getValueAt(row,column)) + "\n")
                else:
                    f.write(str(table_object.getValueAt(row,column)) + ",")
                    
        f.close()
        
    def populateDigiCountDataTable(self,object_symbol):
        low_table_data = squish.findObject(object_symbol)
        field = low_table_data.getClass().getDeclaredField("dataColumn")
        field.setAccessible(True)
        
        data_column = field.get(low_table_data)
        
        field = data_column.getClass().getDeclaredField("dataGraphHeadersMap")
        field.setAccessible(True)
        dataGraphHeadersMap = field.get(data_column)
        
        data_array = dataGraphHeadersMap.keySet().toArray()
        
        table_data = {}
        
        for index in range(data_array.length):
            data = dataGraphHeadersMap.get(data_array.at(index)).toArray().at(0)
            
            highlabel_field = data.getClass().getDeclaredField("highLabel")
            meanlabel_field = data.getClass().getDeclaredField("meanLabel")
            lowlabel_field = data.getClass().getDeclaredField("lowLabel")
            
            highlabel_field.setAccessible(True)
            meanlabel_field.setAccessible(True)
            lowlabel_field.setAccessible(True)
            
            parameter = self.removeNonAscii(data_array.at(index).toString())
            
            highlabel = highlabel_field.get(data).toString()
            meanlabel = meanlabel_field.get(data).toString()
            lowlabel = lowlabel_field.get(data).toString()
            
            table_data[parameter] = {'highlabel':highlabel,"meanlabel":meanlabel,"lowlabel":lowlabel}
            
        return table_data

    def populateWholebloodTableData(self,object_symbol):
        wholeblood_table_data = squish.findObject(object_symbol)
        
        table_data = {}
        
        for row in range(wholeblood_table_data.getRowCount()):
            data = []
            for column in range(wholeblood_table_data.getColumnCount()):
                #First Column will be used for the dictionary key
                if column == 0:
                    continue
                
                data.append(self.removeNonAscii(str(wholeblood_table_data.getValueAt(row,column))))
                
            table_data[str(wholeblood_table_data.getValueAt(row,0))] = data[:]
                
        return table_data
    
    def populateDigiCountDataAllTable(self,object_symbol):
        low_table_data = squish.findObject(object_symbol)
        field = low_table_data.getClass().getDeclaredField("dataColumn")
        
        field.setAccessible(True)
        
        data_column = field.get(low_table_data)
        
        field = data_column.getClass().getDeclaredField("dataGraphHeadersMap")
        field.setAccessible(True)
        dataGraphHeadersMap = field.get(data_column)
        
        data_array = dataGraphHeadersMap.keySet().toArray()
        
        table_data = {}
        levels = ['low','normal','high']
        
        for index in range(data_array.length):
            header_map_array = dataGraphHeadersMap.get(data_array.at(index)).toArray()
            for level in range(header_map_array.length):
                data = dataGraphHeadersMap.get(data_array.at(index)).toArray().at(level)
                
                highlabel_field = data.getClass().getDeclaredField("highLabel")
                meanlabel_field = data.getClass().getDeclaredField("meanLabel")
                lowlabel_field = data.getClass().getDeclaredField("lowLabel")
                value_field = data.getClass().getDeclaredField("value")
                
                highlabel_field.setAccessible(True)
                meanlabel_field.setAccessible(True)
                lowlabel_field.setAccessible(True)
                value_field.setAccessible(True)
                
                parameter = self.removeNonAscii(data_array.at(index).toString())
                
                highlabel = highlabel_field.get(data).toString()
                meanlabel = meanlabel_field.get(data).toString()
                lowlabel = lowlabel_field.get(data).toString()
                value = value_field.get(data).toString()
                
                table_data.setdefault(parameter,{})[levels[level]] = {'highlabel':highlabel, 'meanlabel':meanlabel,'lowlabel':lowlabel,'value':value}
            
        return table_data
    
    #This function removes all unicode from a string.
    def removeNonAscii(self,s): 
        return "".join(filter(lambda x: ord(x)<128, s))
    
    def confirmTableData(self,table_object,filename):
        f = open(filename)
        reader = csv.reader(f,delimiter = ',')
        
        digicount_dictionary = {}
        
        for data in reader:
            digicount_dictionary[data[0]] = data[1:]
        
        f.close()
        
        for key in table_object:
            counter = 0
            for data in table_object[key]:
                test.verify(digicount_dictionary[key][counter] == table_object[key][data],"Confirm that the expected " + data + " data: " + digicount_dictionary[key][counter] + " is equal to " + table_object[key][data])
                counter += 1
                
    def confirmWholeBloodTableData(self,table_object,filename):
        f = open(filename)
        reader = csv.reader(f,delimiter = ',')
        
        digicount_dictionary = {}
        
        for data in reader:
            digicount_dictionary[data[0]] = data[1:]
        
        f.close()
        
        for key in table_object:
            counter = 0
            for data in table_object[key]:
                test.verify(digicount_dictionary[key][counter] == data,"Confirm that the expected table data: " + digicount_dictionary[key][counter] + " is equal to " + data)
                counter += 1
        

    def confirmAllTableData(self,table_object,filename):
        f = open(filename)
        reader = csv.reader(f,delimiter = ',')
        
        digicount_dictionary = {}
        
        for data in reader:
            #digicount_dictionary[data[0]] = data[1:]
            digicount_dictionary.setdefault(data[0],{})[data[1]] = {'highlabel':data[3], 'meanlabel':data[4],'lowlabel':data[5],'value':data[2]}
        
        f.close()
        
        for key in table_object:
            for level in table_object[key]:
                for data in table_object[key][level]:
                    test.verify(digicount_dictionary[key][level][data] == table_object[key][level][data],"Confirm that the expected key " + key + " level " + level + " data: " + data + " value: " + digicount_dictionary[key][level][data] + " is equal to " + table_object[key][level][data])
                    
    def tableDataToFile(self,table_data,filename):
        f = open(filename,'w')
        
        for key in table_data.keys():
            f.write(key + "," + 
                table_data[key]['lowlabel'] + "," + 
                table_data[key]['meanlabel'] + "," + 
                table_data[key]['highlabel'] + "\n")
            
        f.close()
        
    def wholebloodTableDataToFile(self,table_data,filename):
        f = open(filename,'w')
        
        for key in table_data.keys():
            f.write(key + ",")
            for index in range(len(table_data[key])):
                if index + 1 == len(table_data[key]):
                    f.write(table_data[key][index] + "\n")
                else:
                    f.write(table_data[key][index] + ",") 
            
        f.close()
        
    def tableDataAllToFile(self,table_data,filename):
        f = open(filename,'w')
        
        for key in table_data.keys():
            for level in table_data[key].keys():
                f.write(key + "," + level + "," + 
                    table_data[key][level]['value'] + "," +
                    table_data[key][level]['highlabel'] + "," + 
                    table_data[key][level]['meanlabel'] + "," + 
                    table_data[key][level]['lowlabel'] + "\n")
            
        f.close()
        
    def confirmTableTableData(self,filename):
        table_data = {}
        table_data1 = Tables.populateTableData(self,self.table_table_symbol)
        table_data2 = Tables.populateTableData(self,self.runs_table_symbol)
        
        for index in range(len(table_data1)):
            table_data[str(table_data1[index]['Parameter'])] = table_data2[index].values()[0]
        
        #This is just for recording purposes
        f = open(filename, 'w')
        
        for key in table_data:
            f.write(key + "," + table_data.get(key) + "\n")
            
        f.close()
        #End of recording
        
        f = open(filename, 'r')
        
        reader = csv.reader(f,delimiter = ',')
        
        for data in reader:
            test.verify(table_data[data[0]] == data[1],"Confirm that the expected 'rack number' " + data[1] + " is equal to the actual rack number " + table_data[data[0]])
            
        f.close()
        
    def populateReproducibilityTableData(self,right_table_object_symbol,left_table_object_symbol):
        table_data = []
        right_table = squish.findObject(right_table_object_symbol)
        left_table = squish.findObject(left_table_object_symbol)
        right_table_header = right_table.getTableHeader()
        left_table_header = left_table.getTableHeader()
        
        for row in range(right_table.getRowCount()):
            row_data = {}
            counter = 1
            for column in range(right_table.getColumnCount()):
                if "Rack" in right_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString():
                    header = right_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString().split("\n")[1] + " " + str(counter)
                    
                    row_data[header] = str(right_table.getValueAt(row,column))
                    counter += 1
            
            sd_counter = 1
            cv_counter = 1
            for column in range(left_table.getColumnCount()):
                if "SD" in left_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString():
                    header = left_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString() + " " + str(sd_counter)
                    sd_counter += 1
                elif "CV" in left_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString():
                    header = left_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString() + " " + str(cv_counter)
                    cv_counter += 1
                else:
                    header = left_table.getTableHeader().getColumnModel().getColumn(column).getHeaderValue().toString()
                
                row_data[header] = str(left_table.getValueAt(row,column))
                counter += 1

            table_data.append(row_data)
        
        return table_data        

