# Dragon Realm - Choose a door: One door has a friendly dragon and one door has a hungry dragon.

import random

def game():
    print('''Welcome to Dragon Realm
You are in a land full of dragons.
In front of you, you see two caves.
One cave has a friendly dragon inside
that will share his treasure with you.
The other cave has a hungry dragon inside
that will eat you....''')
    choice = input('Which cave will you enter? (1 or 2) ')

    print('''You approach the cave...
It is dark and spooky...
A large dragon jumps out at you! He opens his jaws and...''')

    dragon = random.randint(1, 3)

    if int(choice) == dragon:
        print('Gobbles you down in one bite!')
    else:
        print("says, 'Hello there. Please enjoy my treasure.'")
    playAgain = input('Do you want to play again? (Y/N) ')
    if playAgain.lower() == 'n':
        exit()
    else:

game()
