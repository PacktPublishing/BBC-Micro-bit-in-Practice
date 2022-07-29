from microbit import *

pot_val=pin0.read_analog()
print(pot_val)
 
while True:
     
    if pot_val <= 0:
        pin16.write_analog(pot_val)
    elif pot_val <= 400:
        pin1.write_analog(pot_val)
    elif pot_val <= 1000:
        pin2.write_analog(pot_val)
