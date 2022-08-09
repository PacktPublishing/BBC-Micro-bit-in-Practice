from microbit import *

while True:
    if pin1.read_digital():
        pin0.write_digital(1)
        pin2.write_digital(0)
        sleep(1000)
    else:
        pin2.write_digital(1)
        pin0.write_digital(0)
