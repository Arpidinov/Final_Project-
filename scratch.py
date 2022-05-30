
from tkinter import *
from PIL import Image, ImageTk

SWH = Tk()

SWH.geometry("1024x950+130+0")
SWH.title("ServiceWhiz.")

img = None

def printimage():
    global img
    load = Image.open("alatoo.png")
    render = ImageTk.PhotoImage(load)

    img = Button(SWH, image=render,command=imgpress)
    img.image = render
    img.place(x=0,y=0)
    return;

def imgpress():
    global img
    img.destroy()
    Label1 = Label(SWH, text="Image has been clicked",fg="#0094FF",font=('Arial',20)).pack()
    return;

SWTitle = Label(SWH, text="ServiceWhiz.",fg="#0094FF",font=('Arial',20)).pack()
MyButtonTest = Button(SWH, text="Click Me.",fg="White",bg="#0094FF",command=printimage).pack()

SWH.mainloop()
