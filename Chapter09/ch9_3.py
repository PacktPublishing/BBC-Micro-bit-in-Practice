from microbit import *
x = pin0.read_analog()
print(x)
sleep(1000)
while True:
    y = pin0.read_analog()
    if y < x-50:# here 50 indicates sensitivity
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
        print(y)
