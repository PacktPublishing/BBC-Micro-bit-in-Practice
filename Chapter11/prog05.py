from microbit import *
from neopixel import NeoPixel
num_pixels = 12
ring = NeoPixel(pin0, num_pixels)
try:
    while True:
        for i in range(0, num_pixels):
            ring[i] = [0, 0, 100]
            ring[i-1] = [0, 100, 0]
            ring[i-2] = [100, 0, 0]
            ring.show()
            sleep(50)
            ring.clear()
except KeyboardInterrupt as e:
    print("Interrupted by the user...")