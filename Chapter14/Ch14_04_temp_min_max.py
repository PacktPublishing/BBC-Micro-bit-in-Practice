from microbit import *
Temp = temperature()
MAX = Temp
MIN = Temp
while True:
    display.show('.')
    Temp = temperature()
    if Temp < min:
        min = Temp
    if Temp > max:
        max = Temp
    if button_a.was_pressed():
        display.scroll(MAX)
    if button_b.was_pressed():
        display.scroll(MIN)
    sleep(1000)
    display.clear()
