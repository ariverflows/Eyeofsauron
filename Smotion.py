# this will enable Sauron to scan for frodo and Sam
import Scamera

def main():
    print("Starting Sauron")
    SauronCapture()
    return

def SauronCapture():
    Sauron = Scamera.Eye()
    Sauron.startPreview(20)
    Sauron.snapPic('/home/pi/image.jpg')
    Sauron.stopPreview()
    return

def SauronWatch():
    Sauron = Scamera.Eye()
    Sauron.startPreview()
    Sauron.stopPreview()
    return

if __name__ == '__main__':
    main()
