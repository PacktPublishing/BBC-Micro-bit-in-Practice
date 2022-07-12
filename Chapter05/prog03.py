from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.scroll(3.14)
display.scroll("Micro:bit", delay=300, monospace=True, loop=True)