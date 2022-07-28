from microbit import *
import radio
radio.config(group=20)
ball = Image("01110:"
              "11111:"
              "11111:"
              "11111:"
              "01110")
radio.on()
while True:
    display.show(ball)
    if button_a.is_pressed():
        radio.send("1")
        display.show("O")
        microbit.display.clear()
#        else:
#            radio.send("C")
        sleep(1000)
    if radio.receive() == 1:
        display.show(ball)
        sleep(1000)

#except KeyboardInterrupt as e:
#    print("Interrupted by the user...")
