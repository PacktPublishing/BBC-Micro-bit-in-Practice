from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

shift = 0
values = [[0, 0, 0], [0, 0, 120], [0, 120, 0], [120, 0, 0],
          [120, 120, 120], [120, 120, 0], [120, 0, 120], [0, 120, 120],
          [0, 0, 0], [0, 0, 40], [0, 40, 0], [40, 0, 0]]

while True:
    for i in range(0, 12, 1):
        print(values[int((i + shift) % num_pixels)])
        ring[int(i)] = values[int((i + shift) % num_pixels)]
    print('--')
    ring.show()
    sleep(1000)
    shift = shift + 1
