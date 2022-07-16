from microbit import *

try:
    while True:
        if button_a.is_pressed():
            pin0.write_digital(1)
        else:
            pin0.write_digital(0)
        
        input = pin1.read_digital()
    
        if (input == 1):
            display.show(Image.HEART)
        else:
            display.show(Image.HAPPY)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")