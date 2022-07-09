from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)
delay = 1
step = 1

def glowAll(col):
    for i in range(0, len(ring)):
        ring[i] = col
    ring.show()
    return 0

try:
    while True:
        for i in range(0, 255, step):
            glowAll((i, 0, 0))
            sleep(delay)
        for i in range(255, 0, -step):
            glowAll((i, 0, 0))
            sleep(delay)
        for i in range(0, 255, step):
            glowAll((0, i, 0))
            sleep(delay)
        for i in range(255, 0, -step):
            glowAll((0, i, 0))
            sleep(delay)       
        for i in range(0, 255, step):
            glowAll((0, 0, i))
            sleep(delay)
        for i in range(255, 0, -step):
            glowAll((0, 0, i))
            sleep(delay)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
