import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *
import pypylon
import cv2 

#
# asus P3b :  1280x800
#

class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.init_cameras()
        self.tk.attributes('-zoomed', True)  # maximize so we can see window
        self.imagepanel = Label(self.tk, text="calibrate")
        self.imagepanel.pack()
        self.tk.bind("<Escape>", self.end_acquire)
        self.tk.bind("<Key>", self.snap)
        self.imgnum = 0;

    def init_cameras(self):
        available_cameras = pypylon.factory.find_devices()
        print('Available cameras are', available_cameras)
        self.cam0 = pypylon.factory.create_device(available_cameras[0])
        self.cam1 = pypylon.factory.create_device(available_cameras[1])
        print('Camera info of camera object:', self.cam0.device_info)
        print('Camera info of camera object:', self.cam1.device_info)
        self.cam0.open()
        self.cam1.open()
        # Hard code exposure time
        self.cam0.properties['ExposureTime'] = 200000.0
        self.cam0.properties['Gain'] = 0.0
        self.cam1.properties['ExposureTime'] = 200000.0
        self.cam1.properties['Gain'] = 0.0

    def end_acquire(self, event=None):
        exit()

    def snap(self, event=None):
        print("capture %d" % self.imgnum)
        for image in self.cam0.grab_images(1): 
          image = cv2.cvtColor(image, cv2.COLOR_BAYER_RG2RGB_EA) 
          cv2.imwrite("calib/frame_C0_%02d.png" % self.imgnum, image) 
        for image in self.cam1.grab_images(1): 
          image = cv2.cvtColor(image, cv2.COLOR_BAYER_RG2RGB_EA) 
          cv2.imwrite("calib/frame_C1_%02d.png" % self.imgnum, image) 

        self.imgnum += 1

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.update()
    w.tk.mainloop()






