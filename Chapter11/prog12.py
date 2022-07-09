from microbit import *
from neopixel import NeoPixel

num_pixels = 12
ring = NeoPixel(pin0, num_pixels)

def rainbow(np, num, offset, bright=1):
    rb = ((127, 0, 0), (127, 63, 0), (127, 127, 0), (0, 127, 0),
          (0, 127, 127), (0, 0, 127), (63, 0, 127), (127, 0, 0))
    for i in range(num):
        t = 7*i/num
        t0 = int(t)
        r = round((rb[t0][0] + (t-t0)*(rb[t0+1][0]-rb[t0][0]))*bright) >> 2
        g = round((rb[t0][1] + (t-t0)*(rb[t0+1][1]-rb[t0][1]))*bright) >> 2
        b = round((rb[t0][2] + (t-t0)*(rb[t0+1][2]-rb[t0][2]))*bright) >> 2
        ring[(i+offset)%num] = (r, g, b)
        
n = 0
try:
    while True:
        rainbow(ring, num_pixels, offset = n)
        ring.show()
        n = n + 1
        sleep(200)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")