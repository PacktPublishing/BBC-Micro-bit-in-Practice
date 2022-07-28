from microbit import *
import radio
radio.on()
my_vote = "Vote"
while True:
    if button_a.was_pressed():
        my_vote = "Yes"
        display.show(Image.YES)
        radio.send(my_vote)
    elif button_b.was_pressed():
        my_vote = "No"
        display.show(Image.NO)
        radio.send(my_vote)