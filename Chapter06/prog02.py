from microbit import *
try:
    while True:
        
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        
        sleep(500)
        
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        
        sleep(500)
        
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        
        sleep(1500)
        
        pin0.write_digital(1)
        sleep(1500)
        pin0.write_digital(0)
        
        sleep(500)
        
        pin0.write_digital(1)
        sleep(1500)
        pin0.write_digital(0)
        
        sleep(500)
        
        pin0.write_digital(1)
        sleep(1500)
        pin0.write_digital(0)
        
        sleep(1500)
        
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        
        sleep(500)
        
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        
        sleep(500)
        
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        
        sleep(1500)
        
except KeyboardInterrupt as e:
    print("Interrupted by the user...")