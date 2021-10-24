from os import name, path
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Frame
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from typing import Generator
from pygame import mixer
import random
from pathlib import Path
from PIL import ImageTk

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


class SoundOption:
    def __init__(self, name: str, frecuency: int = 60, main_root: Path = MAIN_ROOT) -> None:
        self.name = name
        self.frecuency = frecuency
        self.volume = db_levels[0]

        self.sound = mixer.Sound((main_root / f"{self.name}.wav").__str__())
        self.image = PhotoImage(
            file=(main_root / f"{self.name}.png").__str__())
    
    def play(self):
        # Cambiar para cada frecuencia...
        self.sound.set_volume(self.volume)
        self.sound.play()
    
    def add_volume(self):
        if not self.volume >= db_levels[-1]:
            self.volume += db_steps


class Alert:
    def __init__(self, name: str, main_root: Path = MAIN_ROOT) -> None:
        self.name = name
        self.sound = mixer.Sound((main_root / f"{self.name}.wav").__str__())

# sonidos y su frecuencia
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

sound_options_list = [SoundOption(name, frec) for name, frec in sound_options_dict.items()]
alerts_dict = {name: Alert(name) for name in alert_options_names}

db_steps = 0.2
db_levels = [db/10 for db in range(db_steps * 10, 11, db_steps * 10)]
results_dict = {sound_option.name: {db: 0 for db in db_levels} for sound_option in sound_options_list}

class window1(Frame):

    def __init__(self, master) -> None:
        super().__init__(master, width=1152, height=1152)
        
        # variables
        self.random_program_selection = None
        self.start_button_name = StringVar(value="Iniciar Pruebas")
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


    def create_widgets(self) -> None:
        # botones creados con imagenes
        for sound_option in sound_options_list:
            self.__setattr__(f"{sound_option.name}_photo", sound_option.image)
            self.__setattr__(f"{sound_option.name}_image", self.__getattribute__(f"{sound_option.name}_photo").subsample(3,3))
            self.__setattr__(f"{sound_option.name}_button", Button(self,
                                   image=self.__getattribute__(f"{sound_option.name}_image"),
                                   command=self.option_pressed(sound_option)))
            self.__getattribute__(f"{sound_option.name}_button").place(**self.place_generator.__next__())

        # boton principal
        self.buttonst = Button(self, textvariable=self.start_button_name, command=self.random_sound_selection, state=NORMAL)
        self.buttonst.place(x=476, y=40, width=200, height=50)
        
        # boton de salida
        self.buttonexit = Button(self, text="salir", command=root.destroy)
        self.buttonexit.place(x=476, y=640, width=200, height=50)

    def random_sound_selection(self):
        if len(sound_options_list) == 0:
            # en caso de el usuario haber acertado todas las figuras
            print("FINALIZAMOS CON TODAS LAS FRECUENCIAS")
            print(results_dict)
            root.destroy()
            return
        
        # Seleccionamos uno
        self.random_program_selection = random.choice([sound_option for sound_option in sound_options_list if sound_option != self.last_election_memory])
        # lo memorizamos para no repetirlo
        self.last_election_memory = self.random_program_selection
        print("random choice:", self.random_program_selection.name)
        
        # Reproducimos
        self.random_program_selection.play()
        #cambiamos nombre a boton
        self.start_button_name.set("Esperando respuesta...")
        # desactivamos el boton
        self.buttonst["state"] = DISABLED

    def option_pressed(self, selection: SoundOption):
        def check_election():
            if selection == self.random_program_selection:
                # reproducimos
                print("pressed:", selection.name)
                selection.play()
                alerts_dict["applause-1"].sound.play()
                
                # Guardo el resultado en mi diccionario
                results_dict[selection.name][selection.volume] += 1
                # Elimino la opcion que ya fue correcta de las posibles opciones a realizar
                sound_options_list.remove(selection)

            else:
                alerts_dict["error"].sound.play()
                # si falla el programa sube progresivamente el sonido de la figura fallada de 0.2 en 0.2
                selection.add_volume()

            # dejamos al programa sin eleccion
            self.random_program_selection = None
            # cambiamos nombre a boton principal
            self.start_button_name.set("Siguiente Sonido")
            # habilitamos el boton
            self.buttonst["state"] = NORMAL
            
        return check_election



if __name__ == "__main__":
    app = window1(root)
    app.mainloop()
