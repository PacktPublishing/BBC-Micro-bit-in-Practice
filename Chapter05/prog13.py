from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
display.show(Image.ALL_CLOCKS)
display.show(Image.ALL_ARROWS)
