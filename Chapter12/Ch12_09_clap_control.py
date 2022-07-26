from microbit import *
while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show("O")
        sleep(1000)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show("X")