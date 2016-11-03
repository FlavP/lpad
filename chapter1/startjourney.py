import random
import textwrap

occupants = ['enemy', 'friend', 'unoccupied']
huts = [random.choice(occupants) for i in range(5)]
width = 72
keep_playin = 'y'
whereTo = 0

continuity = True

while keep_playin == 'y':
    whereTo = int(input("Choose between five huts "))
    whereTo -= 1
    if huts[whereTo] == 'enemy':
        print("You lost, there is an enemy inside")
    elif huts[whereTo] == 'friend':
        print("You win, there is a friend inside")
    elif huts[whereTo] == 'unoccupied':
        print("You can rest, the place is empty")
    keep_playin = input("Do you want to continue? ")