from matrix7seg import Matrix7seg
from microbit import spi, pin0, sleep
seg_display = Matrix7seg(spi, pin0)

i = 0
try:
    while True:
        seg_display.write_number(i)
        seg_display.show()
        sleep(1000)
        i = i + 1
        if i > 9:
            i = 0
except exception:
    print("Interrupted by user...")
