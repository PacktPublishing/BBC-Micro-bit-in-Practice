from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

red = (0x0f, 0, 0)
green = (0, 0x0f, 0)
blue = (0, 0, 0x0f)


def LightAll(col):
    for i in range(0, len(ring)):
        ring[i] = col
    ring.show()
    return 0

while True:
    LightAll(red)
    sleep(1000)
    LightAll(green)
    sleep(1000)
    LightAll(blue)
    sleep(1000)
