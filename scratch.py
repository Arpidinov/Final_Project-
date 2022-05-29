from PIL import Image, ImageTk 
from tkinter import filedialog as f

ifile = f.askopenfile(title='choose a file')

image = Image.open(ifile)
image.show()
