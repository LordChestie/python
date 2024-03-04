import random

NUM_DIGITS = 3
MAX_GUESS = 10

#you know i am eat that turkey

def getSecretNumber():
    # Returns a string of random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
