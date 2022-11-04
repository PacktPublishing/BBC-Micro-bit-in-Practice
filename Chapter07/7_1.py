from microbit import *
display.clear()
while True:
    if button_a.is_pressed(): #returns true or false
        display.show(Image.GHOST)
    elif button_b.is_pressed():#returns true or false
            display.show(Image.SKULL)
