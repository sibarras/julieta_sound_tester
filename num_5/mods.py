import tkinter as tk
from tkinter import Tk
import random
import time
import pandas as pd


def rgb_to_hex(r: int, g: int, b: int) -> str:
    assert type(r) == int and type(g) == int and type(b) == int
    assert all([i < 256 for i in (r,g,b)])

    return "#%02x%02x%02x" % (r,g,b)

# yo pense que era el orden con que salian de izq a derecha
# Mira viejo
# si viejo, descargalo de l gihub
class Window(tk.Frame):
    MAX_COUNT = 5
    def __init__(self, master: Tk, window_title: str, color_options_dict: dict) -> None:
        self.color_dict = color_options_dict
        self.colors_list = [(name, hex_code) for name, hex_code in self.color_dict.items()]
        self.color_order = self.colors_list[:]
        self.current_ans = []
        self.counter = 0
        self.wait_time = 5
        self.results_dict = {}
        self.place_generator = self.reset_place_generator()
        self.start = time.time()

        master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
        master.wm_title(window_title)
        super().__init__(master, width=1152, height=1152)
        self.pack()
        # Boton principal
        self.main_button_text = tk.StringVar(value="Start Test")
        self.main_button = tk.Button(
            self,
            textvariable=self.main_button_text,
            command=self.next_color_order_generation,
            state=tk.NORMAL)
        self.main_button.place(x=476, y=40, width=200, height=50)
        
        # boton de salida
        self.buttonexit = tk.Button(self, text="salir", command=master.destroy)
        self.buttonexit.place(x=476, y=640, width=200, height=50)
        
        
    def next_color_order_generation(self):
        if self.counter >= self.MAX_COUNT:
            self.graph_results()
            self.master.destroy()
            return
        
        self.color_order = self.colors_list[:]
        random.shuffle(self.color_order)
        self.reset_place_generator()
        self.create_colors()
        self.main_button_text.set("Waiting...")
        self.main_button["state"] = tk.DISABLED
        self.wait_observation_time(self.wait_time)
        self.color_order = self.color_order[::-1]
        self.show_possible_options()

    def reset_place_generator(self) -> None:
        place_generator = ({"x": x * 338 + 138,
                                 "y": y * 260 + 120,
                                 "width": 200,
                                 "height": 210
                                 } for y in range(3) for x in range(3))
        self.place_generator = place_generator
        return self.place_generator

    def destroy_colors(self) -> None:
        """ elimina los botones de las opciones para cada uno de las imagenes """
        self.canv.destroy()
        
    def destroy_buttons(self) -> None:
        """ elimina los botones de las opciones para cada uno de las imagenes """
        for name, _ in self.colors_list:
            self.__getattribute__(f"{name}_button").destroy()

    def create_colors(self) -> None:
        self.canv = tk.Canvas(self, width=1152, height=1152)
        self.canv.pack()

        colors_sizes = ((x, y, x+w, y+h) for x, y, w, h in [tuple(val.values()) for val in self.place_generator])
        for name, hex_code in self.color_order:
            print(name, hex_code, "to be created!")
            self.canv.create_rectangle(*colors_sizes.__next__(), outline=hex_code, fill=hex_code)
            self.wait_observation_time(1)
        
    def create_buttons(self) -> None:
        for name, hex_code in self.color_dict.items():
            self.__setattr__(f"{name}_button", tk.Button(
                self,
                bg=hex_code,
                command=self.button_pressed(name)))
            self.__getattribute__(f"{name}_button").place(**self.place_generator.__next__())
    
    def wait_observation_time(self, time: int) -> None:
        """time to wait in seconds as input"""
        var = tk.IntVar()
        self.master.after(time * 1000, var.set, 1)
        print("waiting...")
        self.master.wait_variable(var)

    def show_possible_options(self) -> None:
        self.main_button_text.set("Selecciona en orden")
        self.destroy_colors()
        self.reset_place_generator()
        self.create_buttons()

    def button_pressed(self, button_name):
        def check_button(button_name=button_name) -> None:
            remaining = len(self.color_order)
            assert remaining > 0

            next_color, _ = self.color_order.pop()
            remaining -= 1
            
            if button_name != next_color:
                print("Bad option pressed", button_name)
                self.current_ans.append((next_color, False))
            
            else:
                print("Correct:", button_name)
                self.current_ans.append((next_color, True))
            
            self.__getattribute__(f"{button_name}_button").destroy()
            
            if remaining <= 0:
                success = all([ans for _, ans in self.current_ans])
                print("You have some fails in this color order." if not success else "Well done")
                self.wait_time = self.wait_time - 1 if success and self.wait_time > 1 else self.wait_time
                self.save_result()
                self.current_ans = []

                self.main_button_text.set("Siguiente Prueba" if self.counter < self.MAX_COUNT else "Ver Resultados")
                self.main_button["state"] = tk.NORMAL
                self.reset_place_generator()
        return check_button
    # xopa esperame.. esperame..
    def graph_results(self):
        df = pd.Dataframe(self.results_dict)
        print(df)
        # print(self.results_dict)

    def save_result(self):
        self.results_dict[self.counter] = {name: ans for name, ans in self.current_ans}
        self.counter += 1




if __name__ == "__main__":
    color_options_dict = {
        "blue": rgb_to_hex(0,0,255),
        "green": rgb_to_hex(0,255, 0),
        "red": rgb_to_hex(255,0,0),
    }
    
    print(color_options_dict)
    root = Tk()
    app = Window(root, "Practice", color_options_dict)
    app.mainloop()

# para que corras el archivo main.. no el mods.. como este