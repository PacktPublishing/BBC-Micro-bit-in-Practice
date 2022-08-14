from microbit import *
import speech
import music
while True:
    direction = compass.heading()
    print(direction)
    if direction < 35 :
        speech.say("North")
        display.scroll("N")
        music.play("E8:4")
    elif direction == 90: 
        speech.say("East")
        display.scroll("E")
        music.play("D8:4")
    elif direction == 180: 
        speech.say("South")
        display.scroll("S")
        music.play("C8:2")
    elif direction == 270: 
        speech.say("West")
        display.scroll("W")
        music.play("B8:2")
