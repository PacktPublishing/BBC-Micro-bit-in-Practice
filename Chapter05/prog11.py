from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
display.show(Image.HEART)
