from microbit import *
green = pin0
yellow = pin1
red = pin2
delay_green = delay_red = 5000
delay_yellow = 2000

def green_light():
    green.write_digital(1)
    yellow.write_digital(0)
    red.write_digital(0)

def yellow_light():
    green.write_digital(0)
    yellow.write_digital(1)
    red.write_digital(0)

def red_light():
    green.write_digital(0)
    yellow.write_digital(0)
    red.write_digital(1)

try:
    while True:
          green_light()
          sleep(delay_green)
          yellow_light()
          sleep(delay_yellow)
          red_light()
          sleep(delay_red)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")