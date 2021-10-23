from os import name, path
from tkinter import * 
from tkinter import Tk,Label,Button,Entry, Frame
from tkinter.ttk import *
from pygame import mixer
import random
from pathlib import Path
from PIL import ImageTk

mixer.init()  

root = Tk()
width= root.winfo_screenwidth()  
height= root.winfo_screenheight()
print (width)
print (width)


root.geometry("%dx%d" % (width, height)) 
#root.attributes('-fullscreen', True) 
root.wm_title("Teste Lin")


MAIN_ROOT = Path(__file__).parent.absolute()

# despues veo si hago otra cosa xd si ialgo asi para no tener que tenerlo separado.. algo como esto
# son gaas de jodr
class Object:
    def __init__(self, frecuency:int, filename: str, main_root: Path = MAIN_ROOT) -> None:
        
        self.name = filename
        self.sound = mixer.Sound((MAIN_ROOT / f"{self.name}.wav").__str__())
        self.frecuency = frecuency

        if not (self.name == "error" or self.name == 'applause-1'):
        	self.image = PhotoImage(file = (MAIN_ROOT / f"{self.name}.png").__str__())
		

objects = [
	Object('a'),
	Object('m'),
	Object('u'),
	Object('s'),
	Object('sh'),
	Object('i'),
	Object('error'),
	Object('applause-1'),
]

sounds = [obj.sound for obj in objects]

sound = mixer.Sound((MAIN_ROOT / "applause-1.wav").__str__())
sounda = mixer.Sound((MAIN_ROOT / "a.wav").__str__())
soundm = mixer.Sound((MAIN_ROOT / "m.wav").__str__())
soundu = mixer.Sound((MAIN_ROOT / "u.wav").__str__())
sounds = mixer.Sound((MAIN_ROOT / "s.wav").__str__())
soundsh = mixer.Sound((MAIN_ROOT / "sh.wav").__str__())
soundi = mixer.Sound((MAIN_ROOT / "i.wav").__str__())
sounde = mixer.Sound((MAIN_ROOT / "error.wav").__str__())

bg = ImageTk.PhotoImage(file = (MAIN_ROOT / "fondo.png").__str__())


class  window1(Frame):

	
	def __init__(self,master) -> None:
		super().__init__(master,width=1152, height=1152) 
		self.pack()
		self.create_widgets()
		self.canvas1 = Canvas(master,width=1152, height=1152).create_image(0,0, image = bg ,anchor="nw")


	def create_widgets(self)-> None:


		self.photo = [obj.image for obj in objects if obj.name == 'a'][0]
		self.photoimage = self.photo.subsample(3,3)
		self.button = Button(self, image = self.photoimage,command=self.selecciona).place(x=138,y=120,width=200, height=210)
  
		self.photo2 = [obj.image for obj in objects if obj.name == 'i'][0]
		self.photoimage2 = self.photo2.subsample(3,3)
		self.button2 = Button(self, image = self.photoimage2,command=self.seleccioni).place(x=476,y=120,width=200, height=210)
  
		self.photo3 = [obj.image for obj in objects if obj.name == 'm'][0]
		self.photoimage3 = self.photo3.subsample(3,3)
		self.button3 = Button(self, image = self.photoimage3,command=self.seleccionm).place(x=864,y=120,width=200, height=210)
  
		self.photo4 = [obj.image for obj in objects if obj.name == 'u'][0]
		self.photoimage4 = self.photo4.subsample(3,3)
		self.button4 = Button(self, image = self.photoimage4,command=self.seleccionu).place(x=138,y=380,width=200, height=210)
  
		self.photo5 = [obj.image for obj in objects if obj.name == 's'][0]
		self.photoimage5 = self.photo5.subsample(3,3)
		self.button5 = Button(self, image = self.photoimage5,command=self.seleccions).place(x=476,y=380,width=200, height=210)
  
		self.photo6 = [obj.image for obj in objects if obj.name == 'sh'][0]
		self.photoimage6 = self.photo6.subsample(3,3)
		self.button6 = Button(self, image = self.photoimage6,command=self.seleccionsh).place(x=864,y=380,width=200, height=210)
  
		self.buttonst = Button(self,text="Reproduce Sonido",command=self.soundeleccion).place(x=476,y=40,width=200, height=50)
		self.buttonexit = Button(self,text="salir",command=root.destroy).place(x=476,y=640,width=200, height=50)


	def soundeleccion(self):
		self.soundseleccion = random.choice([obj.name for obj in objects if obj.name not in ["error","applause-1"]]) 
		print ("el sonido seleccionado")
		print (self.soundseleccion)
		self.seleccionsonido()
		#self.buttonst['command']= self.buttonst.destroy()
  
		# que no se repita el mismo sonido en dos elecciones de random (Puedes filtrar basado en la ultima eleccion que tomaste)
		# Guarda la cantidad de aciertos y errores por frecuencia y por imagen. (Puede ser un diccionario. Hay que colocar frecuencia al objeto)
		# Hay que variar la frecuencia y los decibelios con lo que esta frecuencia se escucha. De menor a mayor con un rango definido. la freucnecia puede ser random
		# Cambiar el boton de iniciar test por el boton de siguiente sonido una vez iniciado el test.
		# self.buttons['command'] = self.buttons.destroy() ??
		


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
    
		if len([obj.sound.play() for obj in objects if obj.name == self.seleccion and obj.name == self.soundseleccion]) == 0:
			[obj.sound.play() for obj in objects if obj.name == 'error']

		if len([obj.sound.play() for obj in objects if obj.name == self.seleccion and obj.name == self.soundseleccion]) == 1:
			[obj.sound.play() for obj in objects if obj.name == 'applause-1']


	def seleccionsonido(self):
		[obj.sound.play() for obj in objects if obj.name == self.soundseleccion]



app = window1(root) 
app.mainloop()
