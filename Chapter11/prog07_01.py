from microbit import *
from random import randint
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

delay = 500

def glowAll():
    for i in range(0, len(ring)):
        ring[i] = (randint(0, 255),
                   randint(0, 255),
                   randint(0, 255))
    ring.show()
    return 0

try:
    while True:
        glowAll()
        sleep(500)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
