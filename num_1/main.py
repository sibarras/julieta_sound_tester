
from sound_tester_mod import (
    Tk, Path, MainWindow
)

def main():
    root = Tk()
    ROOT_DIR = Path(__file__).parent.absolute()

    # sonidos y su frecuencia
    # el limite de cuantos sonidos pueden tener esta en el generador de posiciones del window
    sounds_names_dict = {
        "a": 500,
        "m": 125,
        "u": 250,
        "s": 4000,
        "sh": 2000,
        "i": 1000
    }

    app = MainWindow(root, "Teste Lin", sounds_names_dict, ROOT_DIR)
    app.mainloop()


if __name__ == "__main__":
    main()
