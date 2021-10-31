from mods import rgb_to_hex, Window, Tk

def main():
    color_options_dict = {
            "blue": rgb_to_hex(0,0,255),
            "green": rgb_to_hex(0,255, 0),
            "red": rgb_to_hex(255,0,0),
        }
        
    print(color_options_dict)
    root = Tk()
    app = Window(root, "Practice", color_options_dict)
    app.mainloop()

if __name__ == "__main__":
    main()