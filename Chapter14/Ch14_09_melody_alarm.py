from microbit import *
import music
status = 0
while True:
    if (display.read_light_level()<100):
        display.show("N")
        sleep(100)
        if (button_a.is_pressed()):
            status = 1
            while status == 1: 
                display.show("L")
                music.play(music.RINGTONE)
                if (button_b.is_pressed()):
                    display.show("Good Morning")
                    status = 0
                    sleep(1000)