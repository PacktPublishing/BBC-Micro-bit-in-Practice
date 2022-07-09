from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

for i in range(0, 120, 10):
    print(i)
    ring[int(i/10)] = [120-i, 0, i]

ring.show()
