from microbit import *
while True:
    Tilt_x= accelerometer.get_x()
    print("Tilt_x ", Tilt_x)
    sleep(1000)
