from microbit import *
pin_logo.set_touch_mode(pin_logo.CAPACITIVE)
set_timer = 0
while True:
    if pin_logo.is_touched():
        display.show(Image.HEART)
        sleep(50)
        set_timer = running_time()
    else:
        if set_timer > 0:
            time = running_time() - set_timer
            set_timer = 0
            display.clear()
            sleep(200)
            display.scroll(time / 1000)
    