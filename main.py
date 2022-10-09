import tkinter as tk
from tkinter import Image, ImageTk
from PIL import Image, ImageTk

# Bestimmt die Eigenschaften des root
root = tk.Tk()
root.title("StoreManagment")
root.geometry("800x400")
root.minsize(width=250, height=250)
root.maxsize(width=800, height=800)
root.resizable(width=True, height=True)

image = Image.open("package.png").resize((300, 100))
photo = ImageTk.PhotoImage("package.png")

label1 = tk.Label(root, text= "Hallo Welt")
label1.pack()

root.mainloop()