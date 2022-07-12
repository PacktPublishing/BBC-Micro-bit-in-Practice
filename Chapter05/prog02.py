from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
a = 1
display.show(a)
sleep(1000)
a = 1234
display.show(a)
sleep(1000)
a = 3.14
display.show(a, delay=750, clear=True)
sleep(1000)
try:
    a = 3.1416
    display.show(a, delay=750, loop=True)
    sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")
print("Program ended..")
