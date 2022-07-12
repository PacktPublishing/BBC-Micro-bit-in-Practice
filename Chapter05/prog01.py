from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")
a = 'A'
display.show(a)
sleep(1000)
a = 'BBC'
display.show(a)
sleep(1000)
a = 'MicroPython'
display.show(a, delay=750, clear=True)
sleep(1000)
try:
    a = 'Micro:bit'
    display.show(a, delay=750, loop=True)
    sleep(1000)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")

print("Program ended..")
