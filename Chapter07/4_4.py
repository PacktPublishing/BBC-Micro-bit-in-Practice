from microbit import *
counter = 0
display.show(counter)
while True:
    if pin0.read_digital():
        counter = counter + 1
        display.show(counter)
        pin1.write_digital(1)
        sleep(1000)
    else:
        pin1.write_digital(0)
        sleep(1000)
