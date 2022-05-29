from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
 
 
class GUI(Frame):
    img = None
    img_is_found = False
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
 
        self.file = Button(self, width=30, text='Browse', command=self.choose)
        self.label = Label(image=None, width=900, height=600)
        self.button2 = Button(self,width=30,text='Low Contrast',command=self.lowcontrast)
        self.button2.pack() 
        self.pack()
        self.label.pack()
        self.file.pack()
 
    def choose(self):
        ifile = filedialog.askopenfile(parent=self, mode='rb', title='Choose a file')
        if ifile:
            path = Image.open(ifile)
            self.image2 = ImageTk.PhotoImage(path)
            self.label.configure(image=self.image2)
            self.label.image = self.image2
            self.img = np.array(path)
            self.img = self.img[:, :, ::-1].copy()
            self.img_is_found = True
    def lowcontrast(self):
        file = self.img 
        img_af = Image.open(file)
        img_af = img_af.convert("L")
        
        img_af = ImageTk.PhotoImage(Image.fromarray(img_af))
        self.label.configure(image=img_af)
        self.label.image = img_af 
        


        
 
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
 
# root.attributes('-fullscreen', True)
gui = GUI(root)
gui.mainloop()