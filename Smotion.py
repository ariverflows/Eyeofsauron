# this will enable Sauron to scan for frodo and Sam
import Scamera

def main():
    print("Starting Sauron")
    SauronMotionDetected()
    return

def SauronCapture():
    Sauron = Scamera.Eye()
    Sauron.startPreview()
    Sauron.snapPic('/home/pi/image.jpg')
    Sauron.stopPreview()
    return

def SauronWatch():
    Sauron = Scamera.Eye()
    Sauron.startPreview()
    Sauron.startRecord('/home/pi/video.h264', 10)
    Sauron.stopRecord()
    Sauron.stopPreview()
    return

def SauronMotioDetected():
    Sauron = Scamera.Eye()
    Sauron.MotionDetect('/home/pi/imageDetected.jpg')
    return

if __name__ == '__main__':
    main()
