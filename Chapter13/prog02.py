from microbit import *
import radio
radio.on()
try:
    while True:
        msg = radio.receive()
        if msg is not None:
            display.show(msg)
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")