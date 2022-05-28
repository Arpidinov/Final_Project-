#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("300x500")

#Create a canvas
canvas= Canvas(win, width= 300, height= 500)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("alatoo.png"))

#Add image to the Canvas Items
canvas.create_image(20,10,anchor=NW,image=img)

win.mainloop()