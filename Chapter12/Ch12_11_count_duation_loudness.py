from microbit import *
microphone.set_threshold(SoundEvent.LOUD, 200)
set_timer = 0
while True:
    if microphone.was_event(SoundEvent.LOUD):
        set_timer = running_time()
        display.show(Image.HEART)

    if microphone.was_event(SoundEvent.QUIET):
        if set_timer > 0:
            time = running_time() - set_timer
            set_timer = 0
            display.clear()
            sleep(200)
            display.scroll(time / 1000)