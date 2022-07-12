from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
try:
    while True:
        if button_a.is_pressed():
            display.show(Image.HAPPY)
        elif button_b.is_pressed():
            display.show(Image.SAD)
        else:
            display.show(Image.HEART)
        sleep(100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")