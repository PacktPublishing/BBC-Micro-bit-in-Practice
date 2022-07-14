from microbit import *
pins = [pin0, pin1, pin2,
        pin8, pin9, pin12,
        pin13, pin14, pin15,
        pin16]

def blink(pin, duration):
    pin.write_digital(1)
    sleep(duration)
    pin.write_digital(0)
    sleep(duration)

try:
    while True:
        for pin in pins:
            blink(pin, 100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")