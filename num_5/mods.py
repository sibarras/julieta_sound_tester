import tkinter as tk
from tkinter import Tk
from pathlib import Path
import random
import time


def rgb_to_hex(r: int, g: int, b: int) -> str:
    assert type(r) == int and type(g) == int and type(b) == int
    assert all([i < 256 for i in (r,g,b)])

    return "#%02x%02x%02x" % (r,g,b)


class Window(tk.Frame):
    MAX_COUNT = 10
    def __init__(self, master: Tk, window_title: str, color_options_dict: dict) -> None:
        self.color_dict = color_options_dict
        self.colors_list = [(name, hex_code) for name, hex_code in self.color_dict.items()]
        self.color_order = self.colors_list[:]
        self.current_ans = []
        self.counter = 0
        self.results_dict = {}
        self.place_generator = self.reset_place_generator()

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
        self.buttonexit = tk.Button(self, text="salir", command=root.destroy)
        self.buttonexit.place(x=476, y=640, width=200, height=50)
        
        
    def next_color_order_generation(self):
        random.shuffle(self.colors_list)
        self.color_order = self.colors_list[:]
        self.reset_place_generator()
        self.create_colors()
        self.main_button_text.set("Waiting...")
        self.main_button["state"] = tk.DISABLED
        self.wait_observation_time()
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
        for name, _ in self.colors_list:
            self.__getattribute__(f"{name}_color").destroy()
        self.reset_place_generator()

    def destroy_buttons(self) -> None:
        """ elimina los botones de las opciones para cada uno de las imagenes """
        for name, _ in self.colors_list:
            self.__getattribute__(f"{name}_button").destroy()
        self.reset_place_generator()

    def create_colors(self) -> None:
        for name, hex_code in self.color_order:
            self.__setattr__(f"{name}_color", tk.Frame(self, bg=hex_code))
            self.__getattribute__(f"{name}_color").place(**self.place_generator.__next__())

    def create_buttons(self) -> None:
        for name, hex_code in self.color_dict.items():
            self.__setattr__(f"{name}_button", tk.Button(
                self,
                bg=hex_code,
                command=self.button_pressed(name)))
            self.__getattribute__(f"{name}_button").place(**self.place_generator.__next__())
    
    def wait_observation_time(self) -> None:
        time.sleep(5)

    def show_possible_options(self) -> None:
        self.main_button_text.set("Press the colors in the rigth order")
        self.destroy_colors()
        self.reset_place_generator()
        self.create_buttons()

    def button_pressed(self, button_name):
        def check_button(button_name=button_name) -> None:
            assert self.color_order.__len__ > 0

            next_color, _ = self.color_order.pop()
            if button_name != next_color:
                print("Bad option pressed", button_name)
                self.current_ans.append((next_color, False))
                return
            
            print("Correct:", button_name)
            self.current_ans.append((next_color, True))

            if self.color_order.__len__() == 0:
                success = all([ans for _, ans in self.current_ans])
                print("You have some fails in this color order." if not success else "Well done")
                self.save_result()
                self.current_ans = []

                self.main_button_text.set("Next Test")
                self.main_button["state"] = tk.NORMAL
                self.destroy_buttons()
                self.reset_place_generator()
        return check_button
    
    def graph_results(self):
        print(self.results_dict)

    def save_result(self):
        self.results_dict[self.counter] = {name: ans for name, ans in self.current_ans}
        self.counter += 1

        if self.counter <= self.MAX_COUNT:
            self.graph_results()
            self.master.destroy()


if __name__ == "__main__":
    color_options_dict = {
        "red": rgb_to_hex(0,0,255)
    }
    
    print(color_options_dict)
    root = Tk()
    app = Window(root, "Practice", color_options_dict)
    app.mainloop()