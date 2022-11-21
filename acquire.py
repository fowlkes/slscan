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
        self.load_images()
        self.firstcycle = True 

        self.tk.attributes('-zoomed', True)  # maximize so we can see window
        self.imagepanel = Label(self.tk, image=self.img_list[0])
        self.imagepanel.pack()

        self.tk.bind("<Escape>", self.end_acquire)


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

    def load_images(self):
        self.img_list = []
        for i in range(1,len(sys.argv)):
            self.img_list.append(PhotoImage(file=sys.argv[i]))
        self.imgnum = 0

    def end_acquire(self, event=None):
        self.tk.attributes("-fullscreen", False)
        exit()

    def cycle(self):
        if (self.firstcycle):
          self.firstcycle = False
          self.tk.after(200,self.cycle)
          return

        print("capture %d" % self.imgnum)
        for image in self.cam0.grab_images(1): 
          image = cv2.cvtColor(image, cv2.COLOR_BAYER_RG2RGB_EA) 
          cv2.imwrite("grab/frame_C0_%02d.png" % self.imgnum, image) 
        for image in self.cam1.grab_images(1): 
          image = cv2.cvtColor(image, cv2.COLOR_BAYER_RG2RGB_EA) 
          cv2.imwrite("grab/frame_C1_%02d.png" % self.imgnum, image) 

        self.imgnum += 1
        if (self.imgnum >= len(self.img_list)):
          self.imgnum = 0;
          self.tk.after(500,self.end_acquire)
        else:
          nextimg = self.img_list[self.imgnum]
          self.imagepanel.configure(image=nextimg)
          self.imagepanel.image = nextimg
          self.tk.update()
          self.tk.after(200,self.cycle)

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.attributes("-fullscreen",True)
    w.tk.update()
    w.tk.after(1000,w.cycle())
    w.tk.mainloop()

#for key in cam.properties.keys():
#    try:
#        value = cam.properties[key]
#    except IOError:
#        value = '<NOT READABLE>'
#
#    print('{0} ({1}):\t{2}'.format(key, cam.properties.get_description(key), value))
#





