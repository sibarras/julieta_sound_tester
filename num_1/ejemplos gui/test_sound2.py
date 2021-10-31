import time
from pygame import mixer

file = 'test.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()
time.sleep(10)

