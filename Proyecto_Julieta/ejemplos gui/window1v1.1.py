from tkinter import * 
from tkinter.ttk import *
from pygame import mixer
 
# Inicializo sonido y ventana
mixer.init()  
root = Tk()
root.geometry("1024x600")

sound = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/applause-1.wav")
  
# Adding widgets to the root window
Label(root, text = 'Test lin', font =(
  'Verdana', 15)).grid(row=1,column=2, pady = 10)

class  window1(Frame):
	
	 def __init__(self,master) -> None:
		 super().__init__(master,width=320, height=170)
		 self.master = master
		 self.pack()
		 self.create_widgets()
	
	def create_widgets(self)-> None:
		self.photo = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/a.png")
		self.photoimage = self.photo.subsample(3,3)
		self.button = Button(self, image = self.photoimage,command=self.display_sound).place(x=10,y=10,width=100, height=30)
		self.photo2 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/i.png")
		self.photoimage2 = self.photo2.subsample(3,3)
		self.button2 = Button(self, image = self.photoimage,command=self.display_sound).place(x=10,y=10,width=100, height=30)
	
	def display_sound(self)-> None:
		print("Avion fue presionado")
		sound.play()


#photo1 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/i.png")
#photoimage1 = photo1.subsample(3, 3)

#photo2 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/m.png")
#photoimage2 = photo2.subsample(3, 3)

#photo3 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/u.png")
#photoimage3 = photo3.subsample(3, 3)

#photo4 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/s.png")
#photoimage4 = photo4.subsample(3, 3)

#photo5 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/sh.png")
#photoimage5 = photo5.subsample(3, 3)




#def display_sound1():
#	print("Raton fue presionado")
#	sound.play()

#def display_sound2():
#	print("Helado fue presionado")
#	sound.play()
# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
#Button(root, image = photoimage,command=display_sound).grid(row=2,column=1)
#Button(root, image = photoimage1,command=display_sound1).grid(row=3,column=1) 
#Button(root, image = photoimage2,command=display_sound2).grid(row=2,column=2)
#Button(root, image = photoimage3,command=display_sound2).grid(row=3,column=2)
#Button(root, image = photoimage4, command=display_sound2).grid(row=2,column=3)
#Button(root, image = photoimage5, command=display_sound2).grid(row=3,column=3)

root.wm_title("Suma de numeros")
app = window1(root) 
app.mainloop()
