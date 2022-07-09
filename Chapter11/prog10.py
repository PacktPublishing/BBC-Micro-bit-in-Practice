from microbit import *
from neopixel import NeoPixel
import random
num_pixels = 12
ring = NeoPixel(pin0, num_pixels)
try:
    while True:
        ring[(random.randint(0, num_pixels-1))] = ((random.randint(0, 32)),
                                                    (random.randint(0, 32)),
                                                    (random.randint(0, 32)))
        ring.show()
        sleep(200)
        ring.clear()
except KeyboardInterrupt as e:
    print("Interrupted by the user...")