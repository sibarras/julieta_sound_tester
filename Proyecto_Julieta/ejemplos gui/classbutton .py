from tkinter import *

cnt = 0


def MsgClick(event):
    children = root.winfo_children()
    for child in children:
        # print("type of widget is : " + str(type(child)))
        if str(type(child)) == "<class 'tkinter.Message'>":
            # print("Here Message widget will destroy")
            child.destroy()
            return

def MsgMotion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return


def ButtonClick(event):
    global cnt, msg
    cnt += 1
    msg = Message(root, text="you just clicked the button..." + str(cnt) + "...time...")
    msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    msg.bind("<Button-1>", MsgClick)
    msg.bind("<Motion>", MsgMotion)
    msg.pack()
    #print(type(msg)) tkinter.Message


def ButtonDoubleClick(event):
    import sys; sys.exit()


root = Tk()

root.title("My First GUI App in Python")
root.minsize(width=300, height=300)
root.maxsize(width=400, height=350)
button = Button(root, text="Click Me!", width=40, height=3)
button.pack()
button.bind("<Button-1>", ButtonClick)
button.bind("<Double-1>", ButtonDoubleClick)

root.mainloop()