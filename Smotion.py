# this will enable Sauron to scan for frodo and Sam
import Scamera.py

def main():
    print("Starting Sauron")
    Sauron = Scamera.Eye
    Sauron.startPreview()
    Sauron.snapPic('/home/pi')
    Sauron.stopPreview()
    return

if __name__ == '__main__':
    main()
