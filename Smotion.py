# this will enable Sauron to scan for frodo and Sam
import Scamera
import os

def main():
    print("Starting Sauron")
    #SauronMotionDetected()
    SauronDeleteFiles()
    return

def SauronWatch():
    Sauron = Scamera.Eye()
    Sauron.startPreview()
    Sauron.startRecord('/home/pi/video.h264', 10)
    Sauron.stopRecord()
    Sauron.stopPreview()
    return

def SauronMotionDetected():
    Sauron = Scamera.Eye()
    Sauron.MotionDetect('/home/pi/imageDetected.jpg')
    return
#refactor later, removes images in bulk
def SauronDeleteFiles():
    countStart = input("enter count of Image range start: ")
    countEnd = input("enter count of Image range end: ")
    for image in range(int(countStart), int(countEnd) + 1):
        path = "/home/pi/imageDetected" + str(image) + ".jpg"
        os.remove(path)
    return

if __name__ == '__main__':
    main()
