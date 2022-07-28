from microbit import *
import random
import radio
selected = 0
my_move = 0
opp_move = 0
SCISSORS = Image("88008:"
                 "88080:"
                 "88800:"
                 "88080:"
                 "88008")
radio.on()
while True:
    display.show(" ")
    if button_a.was_pressed():
        my_move = random.randint(0, 2)
        if my_move == 0:
            display.show(Image.SQUARE)
        elif my_move == 1:
            display.show(Image.HEART)
        else:
            display.show(SCISSORS)
        sleep(1000)    
    if button_b.was_pressed():
        selected = 1
        radio.send(str(my_move))
    
    opp_move = radio.receive()
    if my_move == 0:
        if opp_move == '0':
            display.show(Image.ASLEEP)
        elif opp_move == '1': 
            display.show(Image.YES)
        else: 
            display.show(Image.NO)
    elif my_move == 1:
        if opp_move == '0':
            display.show(Image.YES)
        elif opp_move == '1': 
            display.show(Image.ASLEEP)
        else: 
            display.show(Image.NO)
    else: 
        if opp_move == '2':
            display.show(Image.NO)
        elif opp_move == '1': 
            display.show(Image.YES)
        else: 
            display.show(Image.ASLEEP)
