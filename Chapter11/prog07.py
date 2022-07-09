from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

red = [31, 0, 0]
green = [0, 31, 0]
blue = [0, 0, 31]
delay = 500

def glowAll(col):
    for i in range(0, len(ring)):
        ring[i] = col
    ring.show()
    return 0

try:
    while True:
        glowAll(red)
        sleep(500)
        glowAll(green)
        sleep(500)
        glowAll(blue)
        sleep(500)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
