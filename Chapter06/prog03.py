from microbit import *
try:
    while True:
        
        pin0.write_digital(1)
        pin1.write_digital(0)
        sleep(500)
        
        pin1.write_digital(1)
        pin0.write_digital(0)
        sleep(500)
        
except KeyboardInterrupt as e:
    print("Interrupted by the user...")