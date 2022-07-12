from microbit import *
try:
    while True:
        sleep(5000)
        print("Button A has been pressed " + str(button_a.get_presses()) + " times.")
        print("Button B has been pressed " + str(button_b.get_presses()) + " times.")
except KeyboardInterrupt as e:
    print("Interrupted by the user...")