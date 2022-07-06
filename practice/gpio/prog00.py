from microbit import *
# 0, 1, 2, 8, 9, 12, 13, 14, 15, 16
display.enable(false)
while True:
    pin3.write_digital(1)  # turn pin0 (and the LED) on
    sleep(500)             # delay for half a second (500 milliseconds)
    pin3.write_digital(0)  # turn pin0 (and the LED) off
    sleep(500)
