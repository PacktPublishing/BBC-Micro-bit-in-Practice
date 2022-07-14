from microbit import *
counter = 0
try:
    while True:
        if counter % 2 == 0:
            led1 = pin0
            led2 = pin1
        else:
            led1 = pin1
            led2 = pin0
        led1.write_digital(1)
        led2.write_digital(0)
        sleep(500)
        counter = counter + 1
except KeyboardInterrupt as e:
    print("Interrupted by the user...")