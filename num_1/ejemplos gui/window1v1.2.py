from tkinter import * 
from tkinter.ttk import *
from pygame import mixer
 
# Inicializo sonido y ventana
mixer.init()  
root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

sound = mixer.Sound('applause-1.wav')
  
# Adding widgets to the root window
Label(frame, text = 'Test lin', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  

photo = PhotoImage(file = r"a.png")
photoimage = photo.subsample(3, 3)

photo1 = PhotoImage(file = r"i.png")
photoimage1 = photo1.subsample(3, 3)

photo2 = PhotoImage(file = r"m.png")
photoimage2 = photo2.subsample(3, 3)

photo3 = PhotoImage(file = r"u.png")
photoimage3 = photo3.subsample(3, 3)

photo4 = PhotoImage(file = r"s.png")
photoimage4 = photo4.subsample(3, 3)

photo5 = PhotoImage(file = r"sh.png")
photoimage5 = photo5.subsample(3, 3)


def display_sound():
	print("Avion fue presionado")
	sound.play()

def display_sound1():
	print("Raton fue presionado")
	sound.play()

def display_sound2():
	print("Helado fue presionado")
	sound.play()
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Button(frame, image = photoimage, compound = LEFT, command=display_sound).pack(side = LEFT)
Button(frame, image = photoimage1, compound = RIGHT, command=display_sound1).pack(side = LEFT)  
Button(frame, image = photoimage2, compound = RIGHT, command=display_sound2).pack(side = LEFT)
Button(frame, image = photoimage3, compound = RIGHT, command=display_sound2).pack(side = BOTTOM)
Button(frame, image = photoimage4, compound = RIGHT, command=display_sound2).pack(side = LEFT)
Button(frame, image = photoimage5, compound = RIGHT, command=display_sound2).pack(side = LEFT)
mainloop()
