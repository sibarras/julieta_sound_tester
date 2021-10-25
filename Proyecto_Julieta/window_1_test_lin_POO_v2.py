from os import name, path
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Frame
from tkinter.ttk import *
from pygame import mixer
import random
from pathlib import Path
from PIL import ImageTk
from matplotlib import pyplot as plt

mixer.init()
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width)
print(width)


root.geometry("%dx%d" % (width, height))
#root.attributes('-fullscreen', True)
root.wm_title("Teste Lin")


MAIN_ROOT = Path(__file__).parent.absolute()
background = ImageTk.PhotoImage(file=(MAIN_ROOT / "fondo.png").__str__())

# Soporta desde 0.0 a 1.0
DB_STEPS = 0.2
DB_LEVELS = [db/10 for db in range(int(DB_STEPS * 10), 11, int(DB_STEPS * 10))]

class SoundOption:
    def __init__(self, name: str, frecuency: int, main_root: Path = MAIN_ROOT) -> None:
        self.name = name
        self.frecuency = frecuency
        self.volume = DB_LEVELS[0] # Comienza con el primer valor de los niveles (DB STEPS)

        self.sound = mixer.Sound((main_root / "sounds" / f"{self.name}.wav").__str__())
        self.image = PhotoImage(
            file=(main_root / "images" / f"{self.name}.gif").__str__())
    
    def play(self):
        """ Este metodo es para reproducir el sonido de este objeto segun el volumen seteado """
        self.sound.set_volume(self.volume)
        self.sound.play()
    
    def add_volume(self):
        """ Añade un nivel mas de volumen al volumen existente, cada vez que se llama este metodo """
        if not self.volume >= DB_LEVELS[-1]:
            self.volume += DB_STEPS
        else:
            print("Max level reached!.")


class Alert:
    def __init__(self, name: str, main_root: Path = MAIN_ROOT) -> None:
        self.name = name
        self.sound = mixer.Sound((main_root / "sounds" / f"{self.name}.wav").__str__())
        # Para reproducir el sonido tengo que meterme al objeto . sound . play()

# sonidos y su frecuencia
# el limite de cuantos sonidos pueden tener esta en el generador de posiciones del window
sound_options_dict = {
    "a": 20,
    "m": 30,
    "u": 40,
    "s": 50,
    "sh": 60,
    "i": 70
}

# alertas para el programa
alert_options_names = ["error", "applause-1"]

# Opciones de sonido
total_sound_options_list = [SoundOption(name, frec) for name, frec in sound_options_dict.items()]
sound_options_list = total_sound_options_list[:]
# Opciones de alerta
alerts_dict = {name: Alert(name) for name in alert_options_names}

# Conteo de aciertos de cada una de las opciones
# { nombre de la opcion: { nivel de volumen: 0 | 1 }}
results_dict = {sound_option.name: {db: 0 for db in DB_LEVELS} for sound_option in sound_options_list}

class window1(Frame):
    def __init__(self, master) -> None:
        super().__init__(master, width=1152, height=1152)
        
        # variables
        # opcion que eligio el programa en random
        self.random_program_selection = None
        # Boton principal nombre
        self.start_button_name = StringVar(value="Iniciar Pruebas")
        # Ultima eleccion para no repetirla
        self.last_election_memory = None
        
        self.pack()

        # Generador de posiciones de figuras. Por ahora solo acepta 9 figuras pero las ultimas 3 medio mal por el ultimo boton de salida que debe correrse
        self.place_generator = ({"x": x * 338 + 138,
                                 "y": y * 260 + 120,
                                 "width": 200,
                                 "height": 210
                                 } for y in range(3) for x in range(3))
        
        self.create_widgets()
        self.canvas1 = Canvas(master, width=1152, height=1152).create_image(
            0, 0, image=background, anchor="nw")


    def create_buttons(self) -> None:
        """ Crea los botones de las opciones para cada uno de las imagenes """
        for sound_option in total_sound_options_list:
            self.__setattr__(f"{sound_option.name}_button", Button(
                                self,
                                image=self.__getattribute__(f"{sound_option.name}_image"),
                                command=self.option_pressed(sound_option),
                            ))
            self.__getattribute__(f"{sound_option.name}_button").place(**self.place_generator.__next__())
    
    def delete_buttons(self) -> None:
        """ elimina los botones de las opciones para cada uno de las imagenes """
        for sound_option in total_sound_options_list:
            self.__getattribute__(f"{sound_option.name}_button").destroy()
        self.place_generator = ({"x": x * 338 + 138,
                                 "y": y * 260 + 120,
                                 "width": 200,
                                 "height": 210
                                 } for y in range(3) for x in range(3))

    def create_widgets(self) -> None:
        # botones creados con imagenes
        for sound_option in total_sound_options_list:
            self.__setattr__(f"{sound_option.name}_photo", sound_option.image)
            self.__setattr__(f"{sound_option.name}_image", self.__getattribute__(f"{sound_option.name}_photo").subsample(3,3))

        # boton principal
        self.buttonst = Button(self,
                                textvariable=self.start_button_name,
                                command=self.random_sound_selection, state=NORMAL)
        self.buttonst.place(x=476, y=40, width=200, height=50)
        
        # boton de salida
        self.buttonexit = Button(self, text="salir", command=root.destroy)
        self.buttonexit.place(x=476, y=640, width=200, height=50)

    def finish_program(self):
        # en caso de el usuario haber acertado todas las figuras
        print("FINALIZAMOS CON TODAS LAS FRECUENCIAS")
        # en vez de imprimir esto, graficar...
        print(results_dict)
        root.destroy()


    def random_sound_selection(self):
        if len(sound_options_list) == 0:
            self.finish_program()
            return
        
        # Seleccionamos uno random si hay mas de una opcion
        if len(sound_options_list) > 1:
            self.random_program_selection = random.choice([sound_option for sound_option in sound_options_list if sound_option != self.last_election_memory])
        else:
            # si solo hay una opcion, elegimos esta unica
            self.random_program_selection = sound_options_list[0]

        # lo memorizamos para no repetirlo
        self.last_election_memory = self.random_program_selection
        print("random choice:", self.random_program_selection.name)
        
        # Reproducimos
        self.random_program_selection.play()
        #cambiamos nombre a boton
        self.start_button_name.set("Esperando respuesta...")
        # desactivamos el boton
        self.buttonst["state"] = DISABLED

        # habilitamos todos los botones de opciones de sonido
        self.create_buttons()

    def option_pressed(self, selection: SoundOption):
        # creo el boton con la seleccion que le pase como argumento
        
        def check_election():
            # esta funcioon se llama cuando se aprieta el boton
            if selection == self.random_program_selection:
                # reproducimos
                print("correct pressed:", selection.name)
                # selection.play()
                # alerts_dict["applause-1"].sound.play()
                
                # Guardo el resultado en mi diccionario
                results_dict[selection.name][selection.volume] += 1
                # Elimino la opcion que ya fue correcta de las posibles opciones a realizar
                sound_options_list.remove(selection)

            elif self.random_program_selection != None:
                print("incorrect pressed:", selection.name)
                # alerts_dict["error"].sound.play()
                # si falla el programa sube progresivamente el sonido de la figura fallada de 0.2 en 0.2
                print("Adding volume from {}".format(self.random_program_selection.volume), end="")
                self.random_program_selection.add_volume()
                print(" to {}".format(self.random_program_selection.volume))


            # dejamos al programa sin eleccion
            self.random_program_selection = None
            # cambiamos nombre a boton principal
            if sound_options_list.__len__() == 0:
                self.start_button_name.set("Mostrar Resultados")
            else:
                self.start_button_name.set("Siguiente Sonido")
            # habilitamos el boton
            self.buttonst["state"] = NORMAL

            # Deshabilitamos todos los botones de opciones de sonido
            self.delete_buttons()
            
        return check_election



if __name__ == "__main__":
    app = window1(root)
    app.mainloop()
