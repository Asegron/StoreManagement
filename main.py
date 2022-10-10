import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class main:
    def __init__(self):
        self.logo = "paket.png" 
        self.window = tk()
        self.img = Image.open(self.filename)
        self.pic = ImageTk.PhotoImage(self.img)
        self.c = Canvas(self.window,
                            width=self.pic.width(),
                            height=self.pic.height())
        self.c.pack()
        self.window.mainloop()

main()








# Bestimmt die Eigenschaften des root
#root = tk.Tk()
#root.title("Store Managment")
#root.geometry("800x400")
#root.minsize(width=250, height=250)
#root.maxsize(width=800, height=800)
#root.resizable(width=True, height=True)

#image = Image.open("paket.png").resize((160, 160))
#photo = ImageTk.PhotoImage(image)

#label1 = tk.Label(root, text= "StoreManagement", image=photo , compound="bottom" )
#label1.pack()

#root.mainloop()