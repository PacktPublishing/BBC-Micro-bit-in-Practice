from microbit import *
import music
while True:
    if accelerometer.get_z() > 800:
        music.play(music.DADADADUM)
        sleep(100)
