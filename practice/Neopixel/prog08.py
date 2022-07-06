from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

def LightAll(col):
    for i in range(0, len(ring)):
        ring[i] = col
    ring.show()
    return 0

while True:

    for i in range(0, 255, 5):
        LightAll((i, 0, 0))
        sleep(20)

    for i in range(255, 0, -5):
        LightAll((i, 0, 0))
        sleep(20)

    for i in range(0, 255, 5):
        LightAll((0, i, 0))
        sleep(20)

    for i in range(255, 0, -5):
        LightAll((0, i, 0))
        sleep(20)
        
    for i in range(0, 255, 5):
        LightAll((0, 0, i))
        sleep(20)

    for i in range(255, 0, -5):
        LightAll((0, 0, i))
        sleep(20)