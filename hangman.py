import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
      |
      |
     ===''', '''
  +---+
  0   |
 /    |
      |
     ===''', '''
  +---+
  0   |
 / \  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']

words = 'philosopher goal rusty duck green rude shoulder moustache yawn repeat unsteady return bigotry revenge prejudice bulwark methodical garage frail attempt inaccurate soap majority vexatious restraint obvious green presentation undue pasture elder infatuation metaphysics outburst lilac buff mental comprehend topmost through raft duchess coldness burlesque tenure concur undecided part hat solemnity'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter: ')
        elif guess in alreadyGuessed:
            print('You already guessed this letter. Choose again.')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again
    print('Do you want to play again? (Y/N)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f"Yes! The secret word is '{secretWord}'! You win!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f"You have run out of guesses.\nAfter {str(len(missedLetters))} missed guesses and {str(len(correctLetters))} correct guesses, the word was '{secretWord}'")
            gameIsDone = True

    # Ask the player if they want to play again after game is done.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break