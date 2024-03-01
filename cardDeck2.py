import random

# A deck of cards, no jokers []
cards = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['❤', '♠', '💎', '♣']

# card values, no jokers {}
card_dict = dict(enumerate(cards, start = 2))
card_values = dict((j, i) for (i, j) in enumerate(cards, start = 2))
theBoard = {'left': ' ', 'right': ' '}


def war():
    player = card_dict[random.randint(2,14)], random.choice(suits)
    computer = card_dict[random.randint(2,14)], random.choice(suits)
    while True:
        print(f"Your card | Computer card")
        print(f"{player[0]} {player[1]} | {computer[0]} {computer[1]}")
        if card_values[player[0]] > card_values[computer[0]]:
            print("You win the war...")
            print('''
            Here are your winnings...
            {
            ''')
            return
        elif card_values[player[0]] < card_values[computer[0]]:
            print("You lost the war..")
            print('''
            Here are your losses...
            {
            ''')
            return
        elif card_values[player[0]] == card_values[computer[0]]:
            war(redraw)


def printBoard(board):
    playerRecord = 0
    computerRecord = 0
    while True:
        game = input("Press any key to draw, 'Q' to quit: " )
        if game.lower() == 'q':
            break
        else:
            print(f"Your card | Computer card")
            player = card_dict[random.randint(2,14)], random.choice(suits)
            computer = card_dict[random.randint(2,14)], random.choice(suits)
            print(f"{player[0]} {player[1]} | {computer[0]} {computer[1]}")
            if card_values[player[0]] > card_values[computer[0]]:
                print("You win!!")
                playerRecord += 1
                print(f"Wins: {playerRecord} Losses: {computerRecord}")
            elif card_values[player[0]] < card_values[computer[0]]:
                print("You lose.")
                computerRecord += 1
                print(f"Wins: {playerRecord} Losses: {computerRecord}")
            elif card_values[player[0]] == card_values[computer[0]]:
                print("War were declared.")
                war()
printBoard(theBoard)

