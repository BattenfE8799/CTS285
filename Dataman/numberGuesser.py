"""
Dataman Number Guesser
"""

import random

def guessNumber():
    """
    Player guesses a random number known by the calculator
    """
    num = random.randint(0,100) # I used randint instead of seed, because it generates a random number in a range
    print("\nI have a number between 0 and 100. What is it?\n")
    guess = int(input("Your guess: "))
    tries = 1
    while guess != num:
        guessedWrong(num,guess)        
        guess = int(input("\nYour guess: "))
        tries += 1
    if guess == num:
        print("\nCorrect!")
        print("\nYou tried ", tries, " many times!\n")
        #send to if play again
    else:
        print("Something went wrong")
    
def guessedWrong(num,guess):
    """
    Cacluates if wrong answer is too high or too low and displays that
    """
    numLow = random.randint(0,(num - 1))
    numHigh = random.randint((num + 1), 100)
    if guess < num:
        print("\nToo Low...",numLow, " ? ",numHigh, "..Try Again..")
    elif guess > num:
        print("\nToo High...",numLow, " ? ",numHigh, "..Try Again..")
    
    
    
    
guessNumber()


    
    
