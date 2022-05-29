from tkinter import Button, messagebox
from tkinter import * 
from PIL import Image,ImageTk
from tkinter import filedialog as F 
from tkinter import Canvas, Text
import numpy as np 
class PhotoEditor(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None 
        self.switch_frame(MainPage)
    
    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if self._frame is not None :
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
class MainPage(Frame):

    def __init__(self,main):
        Frame.__init__(self,main)
        Label(self,text="Main page").pack(side=TOP,fill='x',pady=5)
        self.alatoo = ImageTk.PhotoImage(Image.open('alatoo.png'))
        Label(self,image=self.alatoo).pack(side = TOP)
        Button(self,text = 'Black & White',command = lambda: main.switch_frame(Black)).pack()
        Button(self,text = 'Exit',command = exit).pack()


class Black(Frame):
    def __init__ (self,main):
        Frame.__init__(self,main)
        self.label=Label(self,text = "Black & White filter",)
        self.label.pack()
        
        self.configure()
        Button(self,text = 'Return to main page',fg = 'red',command = lambda: main.switch_frame(MainPage)).pack()
    def configure(self):
        self.canvas = Canvas(self,width=650,height=350)
        self.canvas.pack()
        Button(self,text='Open image',command= self.open_image,).pack()

        Button(self,text='Apply filter',command=self.apply_filter).pack()
    def open_image(self):
        ifile = F.askopenfile(parent=self,mode='rb',title='Choose a file')
        if ifile:
            path = Image.open(ifile)
            self.image2 = ImageTk.PhotoImage(path)
            self.label.configure(image=self.image2)
            self.label.image = self.image2 
            self.img = np.array(path)
            self.img = self.img[:,:,::-1].copy()
        self.image2.show()
        
            
  
      
    def apply_filter(self):
        canvas = Canvas(self,width=300,height=300)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open(self.image))

        canvas.creat_image(20,20,anchor=NW,image=img)



if __name__ == '__main__':
    app = PhotoEditor()
    app.geometry("400x500")
    app.call('wm','iconphoto',app._w,PhotoImage(file='alatoo.png'))
    #app.resizable(False,False)
    app.mainloop()