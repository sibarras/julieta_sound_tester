#!/usr/bin/python
from tkinter import*
from PIL import Image
from PIL import ImageTk 
  
root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("a.png"))  
canvas.create_image(60, 20, anchor=NW, image=img) 
root.mainloop() 
