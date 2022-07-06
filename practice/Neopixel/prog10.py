from microbit import *
from neopixel import NeoPixel
import random

# Lighting up Random Pixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

while True:
    for count in range(int(random.randint(1, 3))):
        ring[(random.randint(0, num_pixels-1))] = ((random.randint(0, 32)),
                                                   (random.randint(0, 32)),
                                                   (random.randint(0, 32)))
        ring.show()
        sleep(200)
        ring.clear()
