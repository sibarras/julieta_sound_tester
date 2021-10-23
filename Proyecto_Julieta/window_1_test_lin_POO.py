from tkinter import * 
from tkinter import Tk,Label,Button,Entry, Frame
from tkinter.ttk import *
from pygame import mixer
import random

# Inicializo sonido y ventana
mixer.init()  

root = Tk()
width= root.winfo_screenwidth()  
height= root.winfo_screenheight() 


#root.geometry("%dx%d" % (width, height)) 
root.attributes('-fullscreen', True) 
root.wm_title("Teste Lin")

sound = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/applause-1.wav")
sounda = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/a.wav")
soundm = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/m.wav")
soundu = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/u.wav")
sounds = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/s.wav")
soundsh = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/sh.wav")
soundi = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/i.wav")
sounde = mixer.Sound("c:/Users/Dell/Documents/Proyecto_Julieta/error.wav")
  

class  window1(Frame):
	
	 def __init__(self,master) -> None:
		 super().__init__(master,width=1024, height=600) 
		 self.pack()
		 self.create_widgets()


	
	 def create_widgets(self)-> None:
         
		 self.photo = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/a.png")
		 self.photoimage = self.photo.subsample(3,3)
		 self.button = Button(self, image = self.photoimage,command=self.selecciona).place(x=10,y=80,width=200, height=210)
		 self.photo2 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/i.png")
		 self.photoimage2 = self.photo2.subsample(3,3)
		 self.button2 = Button(self, image = self.photoimage2,command=self.seleccioni).place(x=220,y=80,width=200, height=210)
		 self.photo3 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/m.png")
		 self.photoimage3 = self.photo3.subsample(3,3)
		 self.button3 = Button(self, image = self.photoimage3,command=self.seleccionm).place(x=440,y=80,width=200, height=210)
		 self.photo4 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/u.png")
		 self.photoimage4 = self.photo4.subsample(3,3)
		 self.button4 = Button(self, image = self.photoimage4,command=self.seleccionu).place(x=10,y=300,width=200, height=210)
		 self.photo5 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/s.png")
		 self.photoimage5 = self.photo5.subsample(3,3)
		 self.button5 = Button(self, image = self.photoimage5,command=self.seleccions).place(x=220,y=300,width=200, height=210)
		 self.photo6 = PhotoImage(file = r"c:/Users/Dell/Documents/Proyecto_Julieta/sh.png")
		 self.photoimage6 = self.photo6.subsample(3,3)
		 self.button6 = Button(self, image = self.photoimage6,command=self.seleccionsh).place(x=440,y=300,width=200, height=210)
		 self.buttonst = Button(self,text="Reproduce Sonido",command=self.soundeleccion).place(x=220,y=10,width=200, height=50)
		 self.buttonexit = Button(self,text="salir",command=root.destroy).place(x=220,y=520,width=200, height=50)


	 def soundeleccion(self):
		 self.soundseleccion = random.choice(["a","m","u","s","sh","i"])
		 print (self.soundseleccion)
		 self.seleccionsonido()
		 #self.buttonst.destroy()
		   


	 def selecciona(self)-> None:
		 print("Avion fue presionado")
		 self.seleccion = "a"
		 print (self.seleccion)
		 print (self.soundseleccion)
		 self.eleccion()

	 def seleccionm(self)-> None:
		 print("Helado fue presionado")
		 self.seleccion = "m"
		 print (self.seleccion)
		 print (self.soundseleccion)
		 self.eleccion()

	 def seleccionu(self)-> None:
		 print("Buho fue presionado")
		 self.seleccion = "u"
		 print (self.seleccion)
		 print (self.soundseleccion)
		 self.eleccion()

	 def seleccions(self)-> None:
		 print("Serpiente fue presionado")
		 self.seleccion = "s"
		 print (self.seleccion)
		 print (self.soundseleccion)
		 self.eleccion()

	 def seleccionsh(self)-> None:
		 print("Silencio fue presionado")
		 self.seleccion = "sh"
		 print (self.seleccion)
		 print (self.soundseleccion)
		 self.eleccion()

	 def seleccioni(self)-> None:
		 print("El raton fue presionado")
		 self.seleccion = "i"
		 print (self.seleccion)
		 print (self.soundseleccion)
		 self.eleccion()


	 def eleccion(self):
          if self.seleccion == "a" and self.soundseleccion == "a":
           sound.play()
          if self.seleccion == "m" and self.soundseleccion == "m":
           sound.play()
          if self.seleccion == "u" and self.soundseleccion == "u":
           sound.play()
          if self.seleccion == "s" and self.soundseleccion == "s":
           sound.play()
          if self.seleccion == "sh" and self.soundseleccion == "sh":
           sound.play()
          if self.seleccion == "i" and self.soundseleccion == "i":
           sound.play()
          else:
           sounde.play()
          # print (self.seleccion)
          # print (self.soundseleccion)		   
   

	
	 def seleccionsonido(self):
          if self.soundseleccion == "a":
           sounda.play()
          if self.soundseleccion == "m":
           soundm.play()
          if self.soundseleccion == "u":
           soundu.play()
          if self.soundseleccion == "s":
           sounds.play()
          if self.soundseleccion == "sh":
           soundsh.play()
          if self.soundseleccion == "i":
           soundi.play()


app = window1(root) 
app.mainloop()
