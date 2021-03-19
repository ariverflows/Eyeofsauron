import picamera
from time import sleep

# Basic camera fucntions to record and take picture of "my precious"
class Eye:
    def __init__(self):
        self.camera = picamera.PiCamera()

    def startPreview(self,time=0):
        self.camera.start_preview()

# filepath in the form of string 'video.h264'
    def startRecord(self, filePath):
        self.camera.start_recording(filePath)

    def stopRecord(self):
        self.camera.stop_recording()

    def stopPreview(self):
        self.camera.stop_preview()

# filepath in the form of a .jpg
    def snapPic(self, filepath):
        self.camera.capture(filepath)
