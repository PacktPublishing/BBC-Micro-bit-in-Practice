from microbit import *
Temp = temperature()
while True:
    display.show('.')
    Temp = temperature()
    if button_a.was_pressed():
        display.scroll(Temp)
    sleep(1000)
    display.clear()

