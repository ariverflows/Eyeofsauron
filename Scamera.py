import picamera
from time import sleep
from gpiozero import MotionSensor

# Basic camera fucntions to record and take picture of "my precious"
class Eye:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.sensor = MotionSensor(4)

    def startPreview(self,time=0):
        self.camera.start_preview()

# filepath in the form of string 'video.h264'
    def startRecord(self, filePath, time=0):
        self.camera.start_recording(filePath)
        sleep(time)

    def stopRecord(self):
        self.camera.stop_recording()

    def stopPreview(self):
        self.camera.stop_preview()

# filepath in the form of a .jpg
    def snapPic(self, filepath):
        self.camera.capture(filepath)

    def MotionDetect(self, filepath):
        self.sensor.when_motion = snapPic(filepath)
        print("Motion Detected!")
