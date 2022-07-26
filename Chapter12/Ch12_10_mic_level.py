from microbit import *
imageX = Image("10001:"
              "01010:"
              "00100:"
              "01010:"
              "10001")
while True:
    display.show(imageX * microphone.sound_level())
