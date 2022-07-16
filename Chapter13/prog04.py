import radio, random
from microbit import *

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]
print(flash)

try:
    radio.on()
    while True:
        if button_a.was_pressed():
            radio.send('flash')
            print("Sent the flash message!")
        if radio.receive() == 'flash':
            sleep(random.randint(50, 1000))
            display.show(flash, delay=100, wait=False)
            sleep(random.randint(50, 1000))
            radio.send('flash')
except KeyboardInterrupt as e:
    print("Interrupted by the user..")