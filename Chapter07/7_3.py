from microbit import *

while True:
    if pin2.read_digital():
        pin0.write_digital(1)
        pin1.write_digital(0)
        sleep(1000)
    else:
        pin1.write_digital(1)
        pin0.write_digital(0)
