from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
pattern0 = Image("00000:11111:22222:33333:44444")
display.show(pattern0)
