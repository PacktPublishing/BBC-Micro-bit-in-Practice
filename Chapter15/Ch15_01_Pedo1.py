from microbit import *
steps_count=0
while True:
    if button_a.is_pressed():
        steps_count =0
        display.show(steps_count)
    if accelerometer.was_gesture('shake'):
        steps_count += 1
        display.show(steps_count)
        