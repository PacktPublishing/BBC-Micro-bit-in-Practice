from microbit import *
while True:
    if display.read_light_level() < 100:
        display.show(Image(
        "88888:"
        "88888:"
        "88888:"
        "88888:"
        "88888"))
    else:
        display.clear()
    sleep(5000)
