from microbit import *
while True:
    if pin0.read_digital():
        pin1.write_digital(1)
        pin2.write_digital(0)
        pin15.write_digital(0)
        pin16.write_digital(0)
        sleep(1000)
    elif pin14.read_digital():
        pin1.write_digital(0)
        pin2.write_digital(1)
        pin15.write_digital(0)
        pin16.write_digital(0)
    elif pin12.read_digital():
        pin1.write_digital(0)
        pin2.write_digital(0)
        pin15.write_digital(1)
        pin16.write_digital(0)
    elif pin13.read_digital():
        pin1.write_digital(0)
        pin2.write_digital(0)
        pin15.write_digital(0)
        pin16.write_digital(1)
