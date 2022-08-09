from microbit import *
import random
pins = [pin0, pin1, pin2, pin16] 
Start = 10
Stop = 200
while True :
    cycle = random.randrange(Start, Stop)
    while True:
        pins[0].write_digital(1)
        pins[1].write_digital(0)
        pins[2].write_digital(0)
        pins[3].write_digital(0)
        sleep(10)
        pins[0].write_digital(0)
        pins[1].write_digital(1)
        pins[2].write_digital(0)
        pins[3].write_digital(0)
        sleep(10)
        pins[0].write_digital(0)
        pins[1].write_digital(0)
        pins[2].write_digital(1)
        pins[3].write_digital(0)
        sleep(10)
        pins[0].write_digital(0)
        pins[1].write_digital(0)
        pins[2].write_digital(0)
        pins[3].write_digital(1)
        sleep(10)
