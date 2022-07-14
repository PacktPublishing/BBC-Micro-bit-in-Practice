from microbit import *

red = pin0
green = pin1
blue = pin2

def glow(red_val, green_val, blue_val):
    red.write_digital(red_val)
    green.write_digital(green_val)
    blue.write_digital(blue_val)

try:
    while True:
        glow(0, 0, 0)
        sleep(1000)
        glow(0, 0, 1)
        sleep(1000)
        glow(0, 1, 0)
        sleep(1000)
        glow(0, 1, 1)
        sleep(1000)
        glow(1, 0, 0)
        sleep(1000)
        glow(1, 0, 1)
        sleep(1000)
        glow(1, 1, 0)
        sleep(1000)
        glow(1, 1, 1)
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")