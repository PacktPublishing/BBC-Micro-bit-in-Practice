from microbit import *
Temp = temperature()
while True:
    Temp = temperature()
    if Temp > 27:
        display.show("H")
        pin1.write_analog(255)
        sleep(1000)
    else:
        display.show("L")
        pin1.write_digital(0)
        sleep(1000)
    display.clear()
