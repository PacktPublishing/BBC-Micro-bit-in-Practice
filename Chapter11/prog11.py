from microbit import *
from neopixel import NeoPixel
import random

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

r = 0
dir = 1
while True:
    for i in range(num_pixels):
        ring[i] = (r, 0, 0)
        ring.show()
        sleep(15)
        r = r + dir
        if r == 0 or r == num_pixels:
            dr = 0 - dir
        ring.clear()
