from microbit import *
if not display.is_on():
    display.on()
else:
    print("Display is already on...")

display.clear()

values = [[0, 1, 2, 3, 4],
          [1, 2, 3, 4, 5],
          [2, 3, 4, 5, 6],
          [3, 4, 5, 6, 7],
          [4, 5, 6, 7, 8]]
print (values)

try:
    while True:
        for i in range(0, 5, 1):
            for j in range(0, 5, 1):
                display.set_pixel(i, j, values[i][j])
                values[i][j] = (values[i][j] + 1) % 10
                print(values)
        sleep(100)
except KeyboardInterrupt as e:
    print("Interrupted by the user...")