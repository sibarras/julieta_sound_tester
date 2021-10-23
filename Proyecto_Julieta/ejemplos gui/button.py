import tkinter as tk

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x100")

        self.buttonA = tk.Button(self.root,
                                 text="Original Text")

        self.buttonB = tk.Button(self.root,
                                text="Click to change text",
                                command=self.changeText)
        self.buttonA.pack(side=tk.LEFT)
        self.buttonB.pack(side=tk.RIGHT)
        self.root.mainloop()

    def changeText(self):
        self.buttonA.destroy()      

app=Test()