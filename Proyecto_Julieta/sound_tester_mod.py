from tkinter import *
from tkinter import Tk, Label, Button, Entry, Frame
from tkinter.ttk import *
from pygame import mixer
import random
from pathlib import Path
from PIL import ImageTk
from matplotlib import pyplot as plt
import pandas as pd


class SoundOption:
    DB_STEPS = 0.2
    DB_LEVELS = [db/10 for db in range(int(DB_STEPS * 10), 11, int(DB_STEPS * 10))]
    FREC_LEVELS = [125, 250, 500, 1000, 2000, 4000]

    def __init__(self, name: str, main_root: Path) -> None:
        """Constructor para las opciones de sonido. Debe haber iniciado """
        self.name = name
        self.main_root = main_root
        self.used_frecuencies = []
        self.frecuency = random.choice(self.FREC_LEVELS)
        self.volume = self.DB_LEVELS[0] # Comienza con el primer valor de los niveles (DB STEPS)
        self.results = {frec: {db_level: 0 for db_level in self.DB_LEVELS} for frec in self.FREC_LEVELS}
        self.finished = False

        # self.sounds_dict = {frec: mixer.Sound((main_root / "sounds" / f"{self.name}_{frec}.wav").__str__()) for frec in self.FREC_LEVELS}
        self.image = PhotoImage(file=(main_root / "images" / f"{self.name}.gif").__str__()) # need a root
    
    def play(self):
        """ Este metodo es para reproducir el sonido de este objeto segun el volumen seteado """
        mixer.init(self.frecuency)
        mixer.music.load((self.main_root / "sounds" / f"{self.name}.wav").__str__())
        mixer.music.set_volume(self.volume)
        mixer.music.play()
        # self.sounds_dict[self.frecuency].set_volume(self.volume)
        # self.sounds_dict[self.frecuency].play()
    
    def stop(self):
        mixer.music.stop()
        # self.sounds_dict[self.frecuency].stop()
    
    def add_volume(self):
        """ Añade un nivel mas de volumen al volumen existente, cada vez que se llama este metodo """
        if not self.volume >= self.DB_LEVELS[-1]:
            self.volume += self.DB_STEPS
        else:
            print("Max level reached!.")
    
    def correct_result(self):
        self.results[self.frecuency][self.volume] = 1
        self.used_frecuencies.append(self.frecuency)

        if len(self.used_frecuencies) == len(self.FREC_LEVELS):
            self.finished = True
            return

        self.volume = self.DB_LEVELS[0]
        self.frecuency = random.choice([frec for frec in self.FREC_LEVELS if frec not in self.used_frecuencies])

    def incorrect_result(self):
        if self.volume != self.DB_LEVELS[-1]:
            self.add_volume()
        else:
            print("Max Level Reached.!")
          

class Alert:
    def __init__(self, name: str, main_root: Path) -> None:
        self.name = name
        self.sound = mixer.Sound((main_root / "sounds" / f"{self.name}.wav").__str__())
        # Para reproducir el sonido tengo que meterme al objeto . sound . play()


class MainWindow(Frame):
    def __init__(self, master: Tk, window_title: str, sound_options_dict: dict, main_root: Path) -> None:
        self.main_dir = main_root
        master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
        master.wm_title(window_title)
        self.store_sounds_information(sound_options_dict)
        
        super().__init__(master, width=1152, height=1152)
        # variables
        # opcion que eligio el programa en random
        self.random_program_selection = None
        # Boton principal nombre
        self.start_button_name = StringVar(value="Iniciar Pruebas")
        # Ultima eleccion para no repetirla
        self.last_election_memory = None
        # Para activar el destructor en la proxima pulsacion
        self.is_the_final = False
        
        self.pack()

        # Generador de posiciones de figuras. Por ahora solo acepta 9 figuras pero las ultimas 3 medio mal por el ultimo boton de salida que debe correrse
        self.place_generator = ({
            "x": x * 338 + 138,
            "y": y * 260 + 120,
            "width": 200,
            "height": 210
            } for y in range(3) for x in range(3))
        
        self.create_widgets(master)

        # Window Background
        background = ImageTk.PhotoImage(file=(main_root / "fondo.png").__str__())
        # self.canvas1 = Canvas(master, width=1152, height=1152).create_image(
        #     0, 0, image=background, anchor="nw")

    def store_sounds_information(self, sound_options_dict: dict) -> None:
        self.sound_options_list = create_sound_options(sound_options_dict, self.main_dir)
        self.total_sound_options_list = self.sound_options_list[:]

    def create_buttons(self) -> None:
        """ Crea los botones de las opciones para cada uno de las imagenes """
        random.shuffle(self.total_sound_options_list)
        for sound_option in self.total_sound_options_list:
            self.__setattr__(f"{sound_option.name}_button", Button(
                                self,
                                image=self.__getattribute__(f"{sound_option.name}_image"),
                                command=self.option_pressed(sound_option),
                            ))
            self.__getattribute__(f"{sound_option.name}_button").place(**self.place_generator.__next__())
    
    def delete_buttons(self) -> None:
        """ elimina los botones de las opciones para cada uno de las imagenes """
        for sound_option in self.total_sound_options_list:
            self.__getattribute__(f"{sound_option.name}_button").destroy()
        self.place_generator = ({"x": x * 338 + 138,
                                 "y": y * 260 + 120,
                                 "width": 200,
                                 "height": 210
                                 } for y in range(3) for x in range(3))

    def create_widgets(self, root) -> None:
        # botones creados con imagenes
        for sound_option in self.total_sound_options_list:
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

    def graph_results(self, results_dict: dict) -> None:
        for name, res in results_dict.items():
            df = pd.DataFrame(res)
            df.plot(kind="line")
            print("\n\n", name)
            print(df)

        print(results_dict)
        plt.show()
        
    def finish_program(self):
        if self.is_the_final:
            self.master.destroy()
            return

        # en caso de el usuario haber acertado todas las figuras
        print("FINALIZAMOS CON TODAS LAS FRECUENCIAS")
        # en vez de imprimir esto, graficar...
        self.results_dict = {sound_option.name: sound_option.results for sound_option in self.total_sound_options_list}
        self.graph_results(self.results_dict)
        self.is_the_final = True

        root.destroy()

    def random_sound_selection(self):
        if self.sound_options_list == None:
            print("[ERROR]: Debes llamar al metodo 'store_sounds_information(sound_options_dict)' para poder ejecutar el programa.")
            root.destroy()

        if len(self.sound_options_list) == 0:
            self.finish_program()
            return
        
        # Seleccionamos uno random si hay mas de una opcion
        if len(self.sound_options_list) > 1:
            self.random_program_selection = random.choice([sound_option for sound_option in self.sound_options_list if sound_option != self.last_election_memory])
        else:
            # si solo hay una opcion, elegimos esta unica
            self.random_program_selection = self.sound_options_list[0]

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
            self.random_program_selection.stop()
            # esta funcioon se llama cuando se aprieta el boton
            if selection == self.random_program_selection:
                # reproducimos
                print("correct pressed:", selection.name)
                # selection.play()
                # alerts_dict["applause-1"].sound.play()
                
                # Guardo el resultado en mi diccionario
                selection.correct_result()
                # Elimino la opcion que ya fue correcta de las posibles opciones a realizar
                if selection.finished == True:
                    self.sound_options_list.remove(selection)

            elif self.random_program_selection != None:
                print("incorrect pressed:", selection.name)
                # alerts_dict["error"].sound.play()
                # si falla el programa sube progresivamente el sonido de la figura fallada de 0.2 en 0.2
                print("Adding volume from {}".format(self.random_program_selection.volume), end="")
                self.random_program_selection.incorrect_result()
                print(" to {}".format(self.random_program_selection.volume))


            # dejamos al programa sin eleccion
            self.random_program_selection = None
            # cambiamos nombre a boton principal
            if self.sound_options_list.__len__() == 0:
                self.start_button_name.set("Mostrar Resultados")
            else:
                self.start_button_name.set("Siguiente Sonido")
            # habilitamos el boton
            self.buttonst["state"] = NORMAL

            # Deshabilitamos todos los botones de opciones de sonido
            self.delete_buttons()
            
        return check_election


def create_sound_options(name_list: list, root_dir: Path) -> list:
    return [SoundOption(name, root_dir) for name in name_list]


if __name__ == "__main__":
    root = Tk()
    ROOT_DIR = Path(__file__).parent.absolute()

    # sonidos y su frecuencia
    # el limite de cuantos sonidos pueden tener esta en el generador de posiciones del window
    sounds_names_list = [
        "a",
        "m",
        "u",
        "s",
        "sh",
        "i"
    ]

    app = MainWindow(root, "Teste Lin", sounds_names_list, ROOT_DIR)
    app.mainloop()
