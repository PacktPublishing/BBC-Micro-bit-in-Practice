from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

shift = 0
values = [[0, 0, 0], [0, 63, 0],
          [0, 0, 0], [63, 0, 0],
          [0, 0, 0], [0, 0, 63],
          [0, 0, 0], [0, 63, 0],
          [0, 0, 0], [63, 0, 0],
          [0, 0, 0], [0, 0, 63]]

try:
    while True:
        for i in range(0, num_pixels, 1):
            print(values[int((i + shift) % num_pixels)])
            ring[i] = values[int((i + shift) % num_pixels)]
        print('--')
        ring.show()
        sleep(250)
        shift = shift + 1
except KeyboardInterrupt as e:
    print("Interrupted by the user...")