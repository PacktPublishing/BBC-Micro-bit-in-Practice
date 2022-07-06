from microbit import *
from neopixel import NeoPixel

num_pixels = 12
foreground = [0x00, 0x00, 0x60]  # Hex color - red, green and blue
background = [0x00, 0x00, 0x00]

ring = NeoPixel(pin0, num_pixels)

while True:
    for i in range(0, num_pixels):
        ring[i] = foreground     # set pixel i to foreground
        ring.show()              # actually display it
        sleep(50)                # milliseconds
        ring[i] = background     # set pixel to background before moving on
        ring.show()