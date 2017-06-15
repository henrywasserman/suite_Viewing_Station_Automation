import test
import testData
import object
import objectMap
import squishinfo
import squish
import os

from config import Config

class Images:
    
    def __init__(self):
        workingdir = Config().getWorkingDir()
        self.images = workingdir + "/../data/images/"
        self.scripts = workingdir + "/../../scripts/"
        self.classpath = workingdir + "/../../imagecompare/bin"        
        
    def saveImage(self, imagename, object): 
        image = self.images + imagename
        if isinstance(object, str):
            objectimage = squish.grabWidget(squish.findObject(object))
        else:
            objectimage = squish.grabWidget(object)
            
        objectimage.save(image, "PNG")
        return image
    
    #image1 and image2 are filenames - 
    #same is a boolean, True for expecting the images to be the same, 
    #False for expecting the images to be different
    #True for expecting the images to be the same
    def compareImages(self,image1, image2, same):
        #image1 = self.images + image1
        #image2 = self.images + image2
        command = self.scripts + "imagecompare.sh " + self.classpath + " " + image1 + " " + image2 + " " + same
        
        result = os.system(command)
        
        if (same):
            if (result == 0):
                test.passes("Images are identical")
            elif (result == 256):
                test.fail("Images are different")
            elif(result == 512):
                test.fail("File Not Found")
            else:
                test.fail("Test failed for an unknown reason")
        else:
            if (result == 0):
                test.fail("Images are the identical")
            elif(result == 256):
                test.passes("Images are different")
            elif(result == 512):
                test.fail("File Not Found")
            else:
                test.fail("Test failed for an unknown reason")
                
    def compareImagesWithoutTesting(self,image1, image2, same):
        image1 = self.images + image1
        image2 = self.images + image2
        command = self.scripts + "imagecompare.sh " + self.classpath + " " + image1 + " " + image2 + " " + same
        
        result = os.system(command)
        return result
        
                
    def waitForImageToChange(self,imagename, object1,object2):
        result = False
        original_image = "original_" + imagename
        self.saveImage(original_image,object1)
        counter = 0
        while(True):
            if object.exists(object2):
                self.saveImage(imagename, object2)
                if self.compareImagesWithoutTesting(original_image, imagename, "true") != 0:
                    result = True
                    break
            squish.snooze(1.0)
            #Wait For 10 Seconds
            if counter == 100:
                break
            counter += 1
            
        return result