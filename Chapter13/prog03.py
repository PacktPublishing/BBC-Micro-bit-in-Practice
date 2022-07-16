from microbit import *
import radio

try:
    radio.on()
    while True:
        if button_a.is_pressed():
            radio.send("A")
        elif button_b.is_pressed():
            radio.send("B")
        else:
            radio.send("C")
        sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")