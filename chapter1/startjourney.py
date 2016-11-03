import random
import textwrap

occupants = ['enemy', 'friend', 'unoccupied']
huts = [random.choice(occupants) for i in range(5)]
width = 72
keep_playin = 'y'
whereTo = 0

continuity = True

def letsFight():
    heroHealth = random.randint(40,50)
    orcHealth = random.randint(35,45)
    heroDamage = random.randint(4,6)
    orcDamage = random.randint(3,5)
    continueFight = True
    while continueFight is True:
        heroHealth -= orcDamage
        orcHealth -= heroDamage
        print("The enemy does {} damage and the hero has {} health left".format(orcDamage, heroHealth))
        print("The hero does {} damage and the enemy has {} health left".format(heroDamage, orcHealth))
        if heroHealth <= 0:
            print("You died")
            continueFight = False
        elif orcHealth <= 0:
            print("You are victorious")
            continueFight = False

def revealOccupant(hutsie, whatHut):
    if hutsie[whatHut] == 'enemy':
        print("You're in a battle now, bitch")
        letsFight()
    elif hutsie[whatHut] == 'friend':
        print("You win, there is a friend inside")
    elif hutsie[whatHut] == 'unoccupied':
        print("You can rest, the place is empty")

while keep_playin == 'y':
    whereTo = int(input("Choose between five huts "))
    whereTo -= 1
    revealOccupant(huts, whereTo)
    keep_playin = input("Do you want to continue? ")