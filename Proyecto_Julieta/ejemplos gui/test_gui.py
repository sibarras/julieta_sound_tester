from guizero import App, Text, PushButton, Picture
from pygame import mixer

mixer.init()

sound = mixer.Sound('applause-1.wav')

app = App(title="Aplicacion")
welcome_message = Text(app, text="bienvenido al Test", size=40, font="Times New Roman", color="lightblue")

def display_sound():
	print("Button was pressed")
	sound.play()


button = PushButton(app, command=display_sound, text=Picture(app, image="avion.png"))

app.display()
