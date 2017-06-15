# -*- coding: utf-8 -*-
import shutil
import sys
import os
import __builtin__
import exceptions
import traceback

def main():
    try:
        step_counter = 166
        source(findFile("scripts", "BasicFunctionality/startup.py"))
        #shared = Startup("start_slow")
        shared = Startup()
    
        emptyrack_position_1 = getattr(shared.spritecanvas,"emptyrack_position_1")
        emptyrack_position_2 = getattr(shared.spritecanvas,"emptyrack_position_2")
        emptyrack_position_3 = getattr(shared.spritecanvas,"emptyrack_position_3")
        sample_2 = getattr(shared.spritecanvas,"sample_2")
        
        #166. Place an empty tube with no barcode in position 1 of the rack
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("After speaking with Hugh")
        test.log("TODO For now I am going to create a tube on the simulator with a misread and a random fail")
        shared.spritecanvas.bringToFront()
        shared.spritecanvas.moveEmptyRackToTheBelt()
        shared.spritecanvas.addMisreadToASample(sample_2[0],sample_2[1])
        shared.spritecanvas.addFailFailToASample(sample_2[0],sample_2[1])
        test.log("Now move sample to the empty rack")
        shared.spritecanvas.moveObjectAndSetAccessionNumber(sample_2[0],sample_2[1],emptyrack_position_1[0],emptyrack_position_1[1])
        
        #167. Place a whole blood (normal) sample and barcode in position 2 of the same rack.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.moveObjectAndSetAccessionNumber(sample_2[0],sample_2[1],emptyrack_position_2[0],emptyrack_position_2[1])
        
        #168. Place an empty tube without the cap in position 3 of the same rack
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.spritecanvas.addMisreadToASample(sample_2[0],sample_2[1])
        shared.spritecanvas.moveObjectAndSetAccessionNumber(sample_2[0],sample_2[1],emptyrack_position_3[0],emptyrack_position_3[1])
        
        #169. Click on the Analyzers main tab and run the two samples on the Analyzer.            
        #Confirm the empty tube with no barcode generates a Barcode misread and imaging failure notifications on the control Viewing Station.            
        #Confirm the Status Animation section on the Analyzers tab becomes active.            
        #Confirm that during processing a question mark is displayed over the blank tube in the rack animation.            
        #Confirm the Stain Pack and Slide Input items decrease by one in the Consumable Volumes section.            "(S) The Analyzer should correctly identify a tube with a missing cap, which will be represented in the rack status animation with a red-orange circle. I suggest placing an empty tube without a cap in position three of the rack, and observing that the Analyzer does not pick up the tube and that the Viewing Station displays it correctly.
        #[VM 02.27.14] - Added steps for testing with a tube that does not have a cap."
        #Confirm the Analyzer does not pick up the tube with missing cap            
        #Confirm that rack animation on Analyzers tab renders that tube in red color 
        test.log("Step #" + str(step_counter)); step_counter += 1    
        test.log("Get the current Stain Pack and Slide Input values")
        shared.bringViewingStationToTheFront()
        shared.analyzers.clickTab()
        stain_pack_value = shared.analyzers.getConsumableVolumesData("Stain Pack")
        slide_input_value = shared.analyzers.getConsumableVolumesData("Slide Input")
        
        shared.spritecanvas.runSampleRack()
        shared.bringViewingStationToTheFront()
        test.log("TODO - Consensus here is that simulator will not reliable generate an image failure error")
        #Confirm the empty tube with no barcode generates a Barcode misread and imaging failure notifications on the control Viewing Station.
        shared.qctab.confirmBarcodeReadFailure()
        shared.qctab.clickAcknowledgeButton()
        shared.qctab.confirmBarcodeReadFailure()
        shared.qctab.clickAcknowledgeButton()
        test.log("Currently only checking that two sample images appear")
        test.log("First the gray one and next anything other than the gray one.")
        #Confirm the Status Animation section on the Analyzers tab becomes active.
        test.log("TODO: I think this works if we slow down the analyzer - check this out later.")
        #test.verify(shared.analyzers.waitForSampleImageToChange() == True,"Confirm the Status Animation section on the Analyzers tab becomes active")
    
        #Confirm that during processing a question mark is displayed over the blank tube in the rack animation.
        shared.results.waitForNoPatientDataRows(2)
        shared.spritecanvas.selectAnalyzerSimulator()
        
        test.log("TODO: Not able to validate question marks.")
        test.log("The question marks in the simulator move around on the sample with each run")
        #test.vp("spritecanvas")
        
        shared.bringViewingStationToTheFront()
        shared.analyzers.clickTab()
        
        new_stain_pack_value = shared.analyzers.getConsumableVolumesData("Stain Pack")
        new_slide_input_value = shared.analyzers.getConsumableVolumesData("Slide Input")
        
        #Confirm the Stain Pack and Slide Input items decrease by one in the Consumable Volumes section.            "(S) The Analyzer should correctly identify a tube with a missing cap, which will be represented in the rack status animation with a red-orange circle. I suggest placing an empty tube without a cap in position three of the rack, and observing that the Analyzer does not pick up the tube and that the Viewing Station displays it correctly.
        test.verify(__builtin__.int(stain_pack_value) - 4 == __builtin__.int(new_stain_pack_value),"Confirm that the stain pack value has decreased by 1 for each sample")
        test.verify(__builtin__.int(slide_input_value) - 4 == __builtin__.int(new_slide_input_value),"Confirm that the stain pack value has decreased by 1 for each sample")
    
        test.log("TODO: Consenus is that we are nat able to simulate missing cap at this time")    
        #Confirm the Analyzer does not pick up the tube with missing cap            
        #Confirm that rack animation on Analyzers tab renders that tube in red color
    
        #170. When the second blood sample has finished processing, rerun the same sample through the Analyzer.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("We need to re-run the second sample")
        shared.spritecanvas.bringToFront()
        accession_number = shared.spritecanvas.getAccessionNumber(851,178)
        shared.spritecanvas.runSampleInOpenMode(851,178)
        
        #171. After the run has finished, go to the Results main tab. Select the last run of the patient sample noted above, open it for Review and press the "Release" button to release the sample.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.bringViewingStationToTheFront()
        shared.results.clickTab()
        shared.results.populateTableData()
        shared.results.doubleClickOnRowByAccessionNumber(accession_number)
        shared.results.clickReviewReleaseButton()
        
        #172. Select the Archives main tab and enter the accession number into the Search text field.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickTab()
        shared.archives.setSearchText(accession_number)
        
        #173. Press the "Search Archives" button            
        #Confirm the correct archived sample is displayed in the Archives table.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.confirmArchiveRecordsDisplayed()
        shared.archives.populateTableData()
        table_data = shared.archives.getTableData()
        test.verify(accession_number == table_data[0]["Accession #"],"Confirm that the first row displayed contains the accession number: " + accession_number)
    
        #174. Log out of the Viewing Station and then log back in.    
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.vadim.logout()
        shared.vadim.login()
        
        #175. Click to the Archives main tab and note that the archives table has a count of 0 number of sample in the table after the search text field.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickTab()
        shared.archives.populateTableData()
        table_data = shared.archives.getTableData()
        test.verify(len(table_data) == 0,"Confirm that the archive table is empty")
        
        #176. Go to the Results Queue, highlight 3 samples from the queue, and press the Archive button in the toolbar  to force archive.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.results.clickTab()
        shared.results.populateTableData()
        shared.results.selectTableRows(0,2)
        shared.results.clickArchiveButton()
        
        #177. Authenticate the "Archive samples" dialog, press the Archive button, and click over to the Archives main tab.
        test.log("Step #" + str(step_counter)); step_counter += 1
        test.log("From test plan dated 12/16/2013")
        shared.archives.authenticateArchiveSamplesDialog(shared.vadim)          
        shared.archives.clickTab()
        
        #178. Set the search date fields to the current date, press the Search Archives button, and observe that a text after the search field will say "[n] samples", where [n] is the total number of samples that are in the sample list. (Note: The total here is not necessarily 3 if additional archiving had been done on the same date.)
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.setSearchArchivesDatesToCurrentDate()
        shared.archives.clickSearchArchivesButton()
        shared.archives.confirmNumberOfSamplesText("4 samples")
        
        #179. Click and highlight one sample first and then press Command+A to highlight all of the samples in the list while noting the changes in the label.
        test.log("Step #" + str(step_counter)); step_counter += 1
        
        
        #180. Observe that if a sample is selected in the list, the text will instead display  “Selected [m] out of [n] samples”, where [m] is the number of sample(s) selected and [n] is the total number of samples.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.selectTableRows(0,0)
        shared.archives.confirmNumberOfSamplesText("Selected 1 out of 4 samples")
        shared.archives.selectAllRowsWithCommand_a()
        shared.archives.confirmNumberOfSamplesText("Selected 4 out of 4 samples")
        
        #181. Highlight only 1 sample in the table and observe the text will change to display "Selected 1 out of [n] samples".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.selectTableRows(0,0)
        shared.archives.confirmNumberOfSamplesText("Selected 1 out of 4 samples")
        
        #182. Now delete the search field and type in a non-existing barcode into the field.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.setSearchText("5555")
        
        #183. Press the Search Archives button and observe that the text now displays as "0 samples".
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.clickSearchArchivesButton()
        shared.archives.confirmNumberOfSamplesText("0 samples")
        
        #184. In the search text field, type in a valid barcode that was not highlighted in the archives table and press the Search Archives button.
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.setSearchText("XX0000")
        shared.archives.clickSearchArchivesButton()
        
        #185. Observe that when a row is not selected in the sample list and a valid barcode is queried then the text will display as "1 sample".            
        #Confirm the total number of samples will be shown at the top right of the table, in the form “[n] samples.”            
        #Confirm if lines of the table are selected, this will change to say “Selected [m] out of [n] samples.”            
        #Configuration Smoke Test
        test.log("Step #" + str(step_counter)); step_counter += 1
        shared.archives.confirmNumberOfSamplesText("1 sample")
        #Confirm the total number of samples will be shown at the top right of the table, in the form “[n] samples.”
        shared.archives.clickTab()
        shared.archives.confirmNumberOfSamplesText("1 sample")
    
        #Confirm if lines of the table are selected, this will change to say “Selected [m] out of [n] samples.”
        shared.archives.setSearchText("")
        shared.archives.clickSearchArchivesButton()
        shared.archives.selectTableRows(0,0)
        shared.archives.confirmNumberOfSamplesText("Selected 1 out of 4 samples")
    
        shared.archives.selectAllRowsWithCommand_a()
        shared.archives.confirmNumberOfSamplesText("Selected 4 out of 4 samples")

    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in lines:
            test.warn(line)
    finally:
        shared.system.terminateViewingStation()
        