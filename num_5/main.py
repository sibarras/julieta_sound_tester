import tkinter as tk
from tkinter import Tk
master = Tk()

w = tk.Canvas(master, height=1000, width=1000)
w.create_rectangle(0, 0, 500, 500, fill="blue", outline="blue")


master.mainloop()