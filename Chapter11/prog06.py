from microbit import *
from neopixel import NeoPixel
from random import randint

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

try:
    while True:
        for i in range(0, len(ring)):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)
            ring[i-1] = [0, 0, 0]
            ring[i] = [red, green, blue]
            ring.show()
            sleep(100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")