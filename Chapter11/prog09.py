from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

def demo(ring, num_pixels):
    n = num_pixels

    # cycle
    for i in range(4 * n):
        for j in range(n):
            ring[j] = [0, 0, 0]
        ring[i % n] = [255, 255, 255]
        ring.show()
        sleep(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            ring[j] = [0, 0, 128]
        if (i // n) % 2 == 0:
            ring[i % n] = [0, 0, 0]
        else:
            ring[n - 1 - (i % n)] = [0, 0, 0]
        ring.show()
        sleep(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            ring[j] = [val, 0, 0]
        ring.show()

    ring.clear()

try:
    while True:
        demo(ring, num_pixels)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")