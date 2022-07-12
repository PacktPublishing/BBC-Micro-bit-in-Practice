from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
pattern = [Image.HEART, Image.XMAS, Image.PACMAN,
           Image.TARGET, Image.TSHIRT]
display.show(pattern)
