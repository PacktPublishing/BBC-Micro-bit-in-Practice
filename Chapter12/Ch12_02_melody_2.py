import music
from microbit import *
while True:
    if button_a.is_pressed():
        display.show("1")
        music.play(music.FUNK)        
    elif button_b.is_pressed():
        display.show("2")
        music.play(music.DADADADUM)
    else:
        display.show("O")