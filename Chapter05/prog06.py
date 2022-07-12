from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")

display.clear()

values = [0, 1, 2, 3, 4]
print (values)
try:
    while True:
        for i in range(0, 5, 1):
            display.set_pixel(i, 0, values[i])
            values[i] = (values[i] + 1) % 10
            print(values)
        sleep(100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
