from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk 

root  = Tk()
root.geometry('350x450')
root.resizable(False,False)
frame = Frame(root)
frame.pack(side='top',expand=True,fill='both')


class MainWindow:
    def __init__(self,main):
        self.main = main 
        main.title("Photo Editor")
        img = ImageTk.PhotoImage(Image.open('alatoo.png'))
        label1 = Label(frame,image=img)
        label1.image = img 
        label1.place(x=45,y=35)

      
        self.button_exit = Button(frame,text = 'EXIT',command = exit )
        self.button_exit.pack(side=BOTTOM)
        

  

        self.button_copyright = Button(frame,text = 'COPYRIGHT')
        self.button_copyright.pack(side=BOTTOM)


        self.button_test = Button(frame,text='Black&White').pack(side=BOTTOM)



  

MainWindow(root)
root.mainloop()
