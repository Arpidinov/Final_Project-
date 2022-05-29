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

        self.ifile = F.askopenfile(parent=self,mode='rb',title='Choose a file')
        limit = (590,350)
        if self.ifile:
            self.image = Image.open(self.ifile)
            self.image.thumbnail(limit)
            self.image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(200,150,anchor = 'center',image=self.image)
          
      
    def apply_filter(self):
        #self.pack_forget()
        self.applied = Image.open(self.ifile)
        self.applied = self.applied.convert("L")
        self.applied = ImageTk.PhotoImage(self.applied)
        self.canvas.create_image(200,150,anchor='center',image=self.applied)




if __name__ == '__main__':
    app = PhotoEditor()
    app.geometry("400x500")
    app.call('wm','iconphoto',app._w,PhotoImage(file='alatoo.png'))
    #app.resizable(False,False)
    app.mainloop()