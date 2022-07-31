from microbit import *
while True:
    if display.read_light_level() < 100:
        display.show("L")
        pin1.write_analog(255)
        sleep(1000)
    else:
        display.show("H")
        pin1.write_digital(0)
        sleep(1000)
