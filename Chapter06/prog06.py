from microbit import *
display.on()
# 0, 1, 2, 8, 9, 12, 13, 14, 15, 16
# Display pins - 3, 4, 6, 7, 10
# Button Pins - 5, 11
# I2C Pins - 19, 20
# Test program for checking the pins
try:
    while True:
        pin9.write_digital(1)
        sleep(500)
        pin9.write_digital(0)
        sleep(500)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")