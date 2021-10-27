
from sound_tester_mod import (
    Tk, Path, MainWindow
)

def main():
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


if __name__ == "__main__":
    main()
