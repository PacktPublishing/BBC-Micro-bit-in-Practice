from microbit import *
rgb = [pin0, pin1, pin2]
counter = 7
try:
    while True:
        for i in range(len(rgb)):
            signal = int('{:03b}'.format(counter)[i])
            print(signal)
            rgb[i].write_digital(signal)
        print('------')
        if counter == 7:
            counter = 0
        else:
            counter = counter + 1
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
