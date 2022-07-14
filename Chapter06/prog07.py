from microbit import *

counter_led_pins = [pin0, pin1, pin2, pin8]

counter = 0
try:
    while True:
        for i in range(4):
            signal = int('{:04b}'.format(counter)[i])
            print(signal)
            counter_led_pins[i].write_digital(signal)
        print('------')
        if counter == 15:
            counter = 0
        else:
            counter = counter + 1
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")