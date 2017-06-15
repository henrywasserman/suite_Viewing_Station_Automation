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

from tables import Tables

class Graphs(__builtin__.object):

    def getGraphData(self,symbol_object):
        #TODO: need to revisit this so I can acquire all the data points on each line.
        graph_object = squish.findObject(symbol_object)
        components = graph_object.getComponents()
        
        graph_data = {}
        for range_index in range(components.length):
            component = components.at(range_index)
            glines_field = component.getClass().getDeclaredField("graphableLines")
            glines_field.setAccessible(True)
            graphablelines = glines_field.get(component)
                    
            statistic_field = component.getClass().getDeclaredField("statistic")
            statistic_field.setAccessible(True)
            statistic = statistic_field.get(component)
            
            line_array = graphablelines.keySet().toArray()
            line_data = []
            for key_index in range(graphablelines.size()):
                graphableline = graphablelines.get(line_array.at(key_index))
                
                size_field = graphableline.getClass().getDeclaredField("size")
                size_field.setAccessible(True)
                size = size_field.get(graphableline)
                
                for index in range(size.intValue()):
                    
                    value = graphableline.getValue(index)
                    date = graphableline.getDate(index)                
                    statistics = graphableline.getLineStatistics()
                    cv = statistics.cv
                    mean = statistics.mean
                    n = statistics.n
                    rmsd = statistics.rmsd
                    sd = statistics.sd
                    line_data.append({"mean":round(mean,2),"SD":round(sd,1)})
            
            graph_data[statistic.displayname] = (line_data[:])
                
        return graph_data
    
    def getAllGraphData(self,symbol_object,parameter="all"):        
        
        digigraph_pattern = re.compile("^C\d+")
        
        graph_object = squish.findObject(symbol_object)
        components = graph_object.getComponents()
        
        graph_data = {}
        line_data = []
        for component_index in range(components.length):
            component = components.at(component_index)
            glines_field = component.getClass().getDeclaredField("graphableLines")
            glines_field.setAccessible(True)
            graphablelines = glines_field.get(component)
                    
            statistic_field = component.getClass().getDeclaredField("statistic")
            statistic_field.setAccessible(True)
            statistic = statistic_field.get(component)
            display_name = statistic.displayname
            
            if "all" not in parameter:
                if parameter not in display_name:
                    continue
            
            line_array = graphablelines.keySet().toArray()
            
            for key_index in range(graphablelines.size()):
                graphableline = graphablelines.get(line_array.at(key_index))
                                
                statistics = graphableline.getGraphLine().getLineStatistics(statistic)
                graphline = graphableline.getGraphLine().toString()
                #cv = statistics.cv
                #mean = statistics.mean
                #n = statistics.n
                #rmsd = statistics.rmsd                
                #field_size = graphableline.getClass().getDeclaredField("size")
                #field_size.setAccessible(True)
                #size = field_size.get(graphableline)
                
                size = graphableline.getGraphLine().getSize(statistic)
                
                if "trendline" in graphableline.getGraphLine().getFamilyName():
                    type = "population"
                #This is looking for C and some numbers #########
                elif digigraph_pattern.match(graphableline.getGraphLine().getFamilyName()):
                    type = str(graphableline.getGraphLine().getLotID(0).getType()).split(' ')[0]
                else:
                    type = graphableline.getGraphLine().getFamilyName()
                    
                for point_index in range(size):
                    point_inspector = graphableline.getGraphLine().inspect(statistic,point_index)
                    sds = point_inspector.getSdiString()
                    value = round(graphableline.getValue(point_index),2)
                    excluded = graphableline.getGraphLine().isExcluded(statistic,point_index)
                    date = graphableline.getDate(point_index)
                    cause = point_inspector.getCause()
                    visible = graphableline.getGraphLine().isVisible()
                    
                    if "population" not in type:
                        processing_mode = point_inspector.getProcessingMode().toString()
                    else:
                        processing_mode = "na"
                    
                    line_data.append({"value":value,"SDs":sds, "cause":cause, "processing_mode":processing_mode, "visible":visible, "excluded":excluded})
                                    
                graph_data.setdefault(graphline,{})    
                graph_data[graphline].setdefault(display_name,{})[type] = line_data[:]
                line_data = []
                
        return graph_data
    
    
    def getGraphPoints(self,graph_object):
        graph_object = squish.findObject(graph_object)
        components = graph_object.getComponents()
        
        points = {}
        for component_index in range(components.length):
            component = components.at(component_index)
            glines_field = component.getClass().getDeclaredField("graphableLines")
            glines_field.setAccessible(True)
            graphablelines = glines_field.get(component)
            
            statistic_field = component.getClass().getDeclaredField("statistic")
            statistic_field.setAccessible(True)
            statistic = statistic_field.get(component)
            display_name = statistic.displayname
                    
            statistic_field = component.getClass().getDeclaredField("statistic")
            statistic_field.setAccessible(True)
            statistic = statistic_field.get(component)
            
            line_array = graphablelines.keySet().toArray()
            
            for key_index in range(graphablelines.size()):
                graphableline = graphablelines.get(line_array.at(key_index))
                
                field_xs = graphableline.getClass().getDeclaredField("xs")
                field_ys = graphableline.getClass().getDeclaredField("ys")
                
                field_xs.setAccessible(True)
                field_ys.setAccessible(True)
                
                xs = field_xs.get(graphableline)
                ys = field_ys.get(graphableline)
                
                if str(xs) == '<null>':
                    continue
                
                for index in range(xs.length):
                    points.setdefault(display_name,{})
                    points[display_name].setdefault('xs',[]).append(xs.at(index))
                    
                for index in range(ys.length):
                    points.setdefault(display_name,{})
                    points[display_name].setdefault('ys',[]).append(ys.at(index))

        return points

    
    def confirmGraphData(self,graph_dict, filename):
        f = open(filename)
        reader = csv.reader(f,delimiter = ',')
        digicount_dictionary = {}
        for data in reader:
            #For each available point on the line.
            digicount_dictionary.setdefault(data[0],{})
            digicount_dictionary[data[0]].setdefault(data[1],{})
            digicount_dictionary[data[0]][data[1]].setdefault(data[2],[])
            digicount_dictionary[data[0]][data[1]][data[2]].append(
                {'SDs':data[3],
                 'value':data[4],
                 'visible':data[5],
                 'processing_mode':data[6],
                 'excluded':data[7],
                 'cause':data[8],
                 })
        
        f.close()
        
        passed = True
        for key in graph_dict:
            for level in graph_dict[key]:
                for type in graph_dict[key][level]:
                    for index in range(len(graph_dict[key][level][type])):
                        for data_key in graph_dict[key][level][type][index].keys():
                            if not str(digicount_dictionary[key][level][type][index][data_key]) == str(graph_dict[key][level][type][index][data_key]):
                                passed = False 
                                test.verify(str(digicount_dictionary[key][level][type][index][data_key]) == str(graph_dict[key][level][type][index][data_key]),"Confirm that for " + data_key +  " the expected  value data: " + str(digicount_dictionary[key][level][type][index][data_key]) + " is equal to " + str(graph_dict[key][level][type][index][data_key]))
        test.verify(passed,"Confirm that all points on the graph passed the verification tests")
            
    def graphDataToFile(self,graph_data, filename):
        f = open(filename, 'w')
        
        for graph_data_key in graph_data.keys():
            for level_key in graph_data[graph_data_key].keys():
                for type_key in graph_data[graph_data_key][level_key].keys():
                    for index in range(len(graph_data[graph_data_key][level_key][type_key])):
                        data = graph_data[graph_data_key][level_key][type_key][index]
                        f.write(str(graph_data_key) + "," + level_key + "," + type_key + "," +
                                str(data['SDs']) + "," +
                                str(data['value']) + "," +
                                str(data['visible']) + "," +
                                str(data['processing_mode']) + "," +
                                str(data['excluded']) + "," +
                                str(data['cause']) + "\n")
                                
        f.close()
        
    def confirmBootstrapText(self,symbol_object):
        
        graph_object = squish.findObject(symbol_object)
        components = graph_object.getComponents()
        
        for component_index in range(components.length):
            component = components.at(component_index)
            glines_field = component.getClass().getDeclaredField("graphableLines")
            glines_field.setAccessible(True)
            graphablelines = glines_field.get(component)
                    
            statistic_field = component.getClass().getDeclaredField("statistic")
            statistic_field.setAccessible(True)
            statistic = statistic_field.get(component)
            
            line_array = graphablelines.keySet().toArray()
            
            for key_index in range(graphablelines.size()):
                graphableline = graphablelines.get(line_array.at(key_index))
                                
                statistics = graphableline.getGraphLine().getLineStatistics(statistic)
                size = graphableline.getGraphLine().getSize(statistic)
                                
                for point_index in range(size):
                    point_inspector = graphableline.getGraphLine().inspect(statistic, size - point_index - 1 )
                    cause = point_inspector.getCause()
                    expected_cause = "Bootstrap " + str(point_index + 1) + " of 10"
                    test.verify(expected_cause == cause, "Confirm that the the expected cause " + expected_cause + " is equal to the actual cause " + cause )                    

