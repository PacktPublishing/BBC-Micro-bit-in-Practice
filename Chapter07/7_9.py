from microbit import *
import music
import speech
while True:
    if pin2.read_digital() == 1:
        music.play("A2:5")
        speech.say("Hello Abhishek")
    elif pin1.read_digital() == 1:
        music.play("E1:7")
        speech.say("MicrooooooooooooooooPython")
    else:
        pass
