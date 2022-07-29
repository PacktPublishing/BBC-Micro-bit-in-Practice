from microbit import *

while True:
    pot_value=pin0.read_analog()
    print(pot_value)
    if pot_value <= 10:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
   
    sleep(125)
