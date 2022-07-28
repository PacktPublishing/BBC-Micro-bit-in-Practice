from microbit import *
import radio

ball = Image("08880:"
              "88888:"
              "88888:"
              "88888:"
              "08880")
radio.on()
display.show(ball)
while True:
    if accelerometer.was_gesture('shake'):
        radio.send('ball')
        display.show(" ")
    incoming = radio.receive()
    if incoming == 'ball':
        display.show(ball)
