from microbit import *
'''if not display.is_on():
    display.on()
else:
    print("Display is already on...")
display.clear()
'''
try:
    while True:
        if button_a.is_pressed():
            print("Button A is pressed...")
        elif button_b.is_pressed():
            print("Button B is pressed...")
        else:
            print("No Button is pressed...")
        sleep(100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")