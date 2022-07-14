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
        for i in range(0, len(pins), 1):
            blink(pins[i], 100)
            if not (i-1)<0:
                blink(pins[i-1], 100)
        for i in range(len(pins)-1, -1, -1):
            blink(pins[i], 100)
            if not (i+1)>8:            
                blink(pins[i+1], 100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")