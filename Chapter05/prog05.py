from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")

display.clear()

k = 0
for i in [0, 1]:
    for j in range(0, 5, 1):
        #print (j, i, k)
        display.set_pixel(j, i, k)
        k = k + 1

print(display.get_pixel(0, 0))
print(display.get_pixel(0, 1))