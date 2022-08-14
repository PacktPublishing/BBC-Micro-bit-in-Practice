from microbit import *
while True:
    sleep(120)
    print(accelerometer.get_values())
    movement = accelerometer.current_gesture()
    if movement == "shake":
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY) 
