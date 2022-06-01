

from tkinter import Button, messagebox
from tkinter import * 
from PIL import Image,ImageTk
from tkinter import filedialog as F 
from tkinter import Canvas, Text
import numpy as np
from sympy import limit 

img = None 

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
        self.resize = Image.open('alatoo.png')
        self.resize = self.resize.resize((150,150))
        

        self.alatoo = ImageTk.PhotoImage(self.resize)
        Label(self,image=self.alatoo).pack(side=TOP)
        Button(self,text = 'Black & White',command = lambda: main.switch_frame(Black)).pack()
        Button(self,text = 'Exit',command = exit).pack()
        Button(self,text="Copyright",command = lambda:main.switch_frame(Copyright)).pack()


class Black(Frame):
    def __init__ (self,main):
        Frame.__init__(self,main)
        self.label=Label(self,text = "Black & White filter")
        self.label.pack()
        
        self.configure()
        s=Button(self,text = 'Return to main page',fg = 'red',command = lambda: main.switch_frame(MainPage))
        s.pack(side=BOTTOM)
    def configure(self):
        self.label = Label(self)
        self.label.pack()
        Button(self,text='Open image',command=lambda:self.open_image()).pack()
        

        Button(self,text='Apply filter',command=lambda:self.apply_filter()).pack()
        Button(self,text='Save a file',command=lambda: self.save_file()).pack()

        
    def open_image(self):
        #self.label.config(image='')

        self.ifile = F.askopenfile(parent=self,mode='rb',title='Choose a file')
        self.limit = (450,350)
        if self.ifile:
            self.image = Image.open(self.ifile)
            self.image.thumbnail(self.limit)
            self.image = ImageTk.PhotoImage(self.image)
            self.label.config(image=self.image)

           
         
          
    def apply_filter(self):
        #self.label.config(image='')
       

  
        self.applied = Image.open(self.ifile)
        self.applied.thumbnail(self.limit)
        self.converted = self.applied.convert("L")
        self.applied = ImageTk.PhotoImage(self.converted)
        #self.canvas.create_image(20,20,anchor=NW,image=self.applied)
        self.label.config(image=self.applied)


    def save_file(self):
        global h 
        h = self.converted
      
        filename =F.asksaveasfile(initialdir='.',mode='w', defaultextension=".jpg",filetypes = (("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")))
        if filename:
            h.save(filename)

   
    
class Copyright(Frame):
        def __init__ (self,main):
            Frame.__init__(self,main)
            symbol = u"\u00A9"
            self.label=Label(self,text = "Copyright")
            self.label.pack()
     
            self.label = Label(self,text = f"Kind: Application\nWhere: Window, Linux\n Created : Sunday, 30 May 2022\n Version: 1.01\n Copyright: Copyright {symbol} 2022 Alatoo Inc. All rights reserved" )
            self.label.pack(pady=150)
            
            Button(self,text = 'Return to main page',fg = 'red',command = lambda: main.switch_frame(MainPage)).pack()




       
        


        
     
 

if __name__ == '__main__':
    app = PhotoEditor()
    app.geometry("400x500")
    app.call('wm','iconphoto',app._w,PhotoImage(file='alatoo.png'))
    #app.resizable(False,False)
 

    app.mainloop()
