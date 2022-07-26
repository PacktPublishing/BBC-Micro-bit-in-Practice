import music
from microbit import *
i = 0
def play_music(i):
    print(i)
    if i == 0: 
        music.play(music.DADADADUM)
    elif i == 1: 
        music.play(music.ENTERTAINER)
    elif i == 2: 
        music.play(music.PRELUDE)
    elif i == 3: 
        music.play(music.ODE)
    elif i == 4: 
        music.play(music.NYAN)
    elif i == 5: 
        music.play(music.RINGTONE)
    elif i == 6: 
        music.play(music.FUNK)
    elif i == 7: 
        music.play(music.BLUES)
    elif i == 8: 
        music.play(music.BIRTHDAY)
    elif i == 9: 
        music.play(music.WEDDING)
    
while True:
    if button_a.is_pressed():
        i = i+1
        sleep(1000)
    elif button_b.is_pressed():
        play_music(i)
    else:
        display.show(i)

    if i== 10:
        i = 0

        

