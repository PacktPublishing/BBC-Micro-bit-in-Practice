from microbit import *
import music
tempo = 90
while True:
    music.set_tempo(bpm=tempo)
    music.play(['C4:4', 'r:1'])
    if button_a.was_pressed():
        tempo = tempo + 5
    if button_b.was_pressed():
        tempo = tempo -5