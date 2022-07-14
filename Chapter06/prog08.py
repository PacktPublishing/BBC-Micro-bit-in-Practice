from microbit import *

pins = [pin0, pin1, pin2,
        pin8, pin9, pin12,
        pin13, pin14, pin15,
        pin16]

try:
    while True:
        for pin in pins:
            pin.write_digital(1)
        sleep(1000)
        for pin in pins:
            pin.write_digital(0)
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")