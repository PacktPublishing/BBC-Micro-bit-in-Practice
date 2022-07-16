from microbit import *
import radio

try:
    radio.on()
    while True:
        radio.send("Hello, World!")
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
