from microbit import *
while True:
    lightLevel = display.read_light_level()
    display.scroll(lightLevel)
    sleep(2000)
