from microbit import *
pin_logo.set_touch_mode(pin_logo.CAPACITIVE)

while True:
    if pin_logo.is_touched():
        display.show(Image.HEART)
    else:
        display.show(" ")
    