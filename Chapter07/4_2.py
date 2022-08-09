from microbit import *

while True:
    if pin0.read_digital():
        pin1.write_digital(1)
        sleep(1000)
    else:
        pin1.write_digital(0)
        sleep(500)
