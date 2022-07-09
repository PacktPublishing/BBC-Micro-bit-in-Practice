from microbit import *
from random import randint
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

delay = 500

def glowAll():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    for i in range(0, len(ring)):
        ring[i] = (red, green, blue)
    ring.show()
    return 0

try:
    while True:
        glowAll()
        sleep(500)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
