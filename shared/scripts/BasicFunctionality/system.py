import os
import subprocess
import commands
import glob
import squish
import __builtin__

class System:
    
    def __init__(self):
        self.viewing_station = 0
    
    #TODO Right now this is dependent on having the USB drive disk1 until
    #we find a better way to do this.
    def mountUSBDrive(self):
        usb_drive_info = commands.getoutput("diskutil list | grep Apple_HFS")
        m = re.search('disk.*$',usb_drive_info)
        usb_drive = m.group(0)
        result = commands.getoutput("diskutil mount /dev/" + usb_drive)
        m = re.search('.*Volume\s+(.*)\son',result)
        drive_name = m.group(1)
        return drive_name
    
    #TODO Right now this is dependent on having the USB drive disk1 until
    #we find a better way to do this
    def unmountUSBDrive(self):
        usb_drive_info = commands.getoutput("diskutil list | grep Apple_HFS")
        m = re.search('disk.*$',usb_drive_info)
        usb_drive = m.group(0)
        result = commands.getoutput("diskutil unmount /dev/" + usb_drive)
        if result.find("failed") != -1:
            result = commands.getoutput("diskutil unmount force /dev/" + usb_drive)
            
    def isUSBDriveMounted(self,directory):
        return os.path.exists(directory)
            
    def deleteFile(self,file):
        if os.path.exists(file):
            os.remove(file)
            
    def deleteFilesInDirectory(self,directory):
        filelist = glob.glob()
            
    def confirmFileExists(self,file):
        return os.path.exists(file)
    
    def pdfTojpg(self,input_file):
        user = os.environ['USER']
        commands.getoutput("/usr/bin/gs -dNOPAUSE -sDEVICE=jpeg -dFirstPage=1 -dLastPage=237 -sOutputFile=/Users/Shared/PDFwriter/" + user + "/image%d.jpg -dJPEGQ=100 -r300x300 -q " + input_file + " -c quit")
        
    def terminateViewingStation(self):
        result = commands.getoutput("ps -ef | grep \"ViewingStation.jar\" | grep -v grep")
        if result.find("\n") > -1:
            pid = result.split('\n')[1].strip().split()[1]
        else:
            pid = result.strip().split()[1]
            
        os.kill(__builtin__.int(pid),9)
        
    def startViewingStation(self,parameter=""):
        subprocess.call(["rm", "-rf /Users/" + os.environ["USER"] + "/Desktop/newData/config1"])
        subprocess.call(["rm", "-rf /Users/" + os.environ['USER'] + '/Desktop/newData/config2'])
        
        self.viewing_station = subprocess.Popen(os.environ['SQUISH_PREFIX'] + "/bin/start.sh " + parameter,shell=True)
        
        attached= False
        for i in range(30):
            try:
                squish.attachToApplication("ViewingStation")
                test.log("Attaching succeeded")
                attached = True
                break
            except:
                test.log("Viewing Station not ready to attach, retrying...")
                snooze(1.0)
                
        if not attached:
            test.fail("Could not attach to Viewing Station after " + str(i) + " tries")
            
    def attachToViewingStation(self):
        attached= False
        for i in range(30):
            try:
                squish.attachToApplication("ViewingStation")
                test.log("Attaching succeeded")
                attached = True
                break
            except:
                test.log("Viewing Station not ready to attach, retrying...")
                snooze(1.0)
                
        if not attached:
            test.fail("Could not attach to Viewing Station after " + str(i) + " tries")
        