from tkinter import * 
from PIL import ImageTk, Image 


class MainWindow:

    def __init__(self,root):
        self.root = root 
        self.root.title('MyWindow')
        self.root.geometry('350x450')
        #self.root.resizable(False,False)
        img = PhotoImage(file = '/home/umut/Desktop/alatoo.png')
        self.root.call('wm', 'iconphoto',self.root._w, img)
        canvas = Canvas(self.root,width=600,height=400)
        canvas.pack()
        image = ImageTk.PhotoImage(Image.open('alatoo.png'))
        canvas.create_image(50,10,anchor = NW, image = image)
        canvas.pack()
        self.root.mainloop()
    def run(self):
        self.root.mainloop()


window = Tk()
a = MainWindow(window)
a.run()

