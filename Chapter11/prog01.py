from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

shift = 0
values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

try:
    while True:
        for i in range(0, num_pixels, 1):
            curr_value = values[int((i + shift) % num_pixels)]
            ring[i] = [0, 110-curr_value, curr_value ]
        ring.show()
        sleep(1000)
        shift = shift + 1
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
