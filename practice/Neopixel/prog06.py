from microbit import *
from neopixel import NeoPixel
from random import randint

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

while True:
    for pixel_id in range(0, len(ring)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)
        ring[pixel_id-1] = (0, 0, 0)
        ring[pixel_id] = (red, green, blue)
        ring.show()
        sleep(100)