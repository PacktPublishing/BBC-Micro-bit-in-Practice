from microbit import *
import radio
radio.on()
my_vote = "Vote"
vote_count = 0
while True:
    my_vote = radio.receive()
    if my_vote == "Yes":
        vote_count = vote_count+1
        display.show(vote_count)
    elif my_vote == "No":
        vote_count = vote_count
        display.show(vote_count)