#M2HW1 Sprint 2- Memory Bank
#CTS-285-0001
#Elizabeth Battenfield

import time
import sys
import random

def main():
    """
    Main menu
    """
    keepGoing = True
    
    while keepGoing == True:
        print("\n","-"*8,"Menu","-"*8)
        print("\n1. Answer Checker \n2. Memory Bank")
        print("3. Number Guesser\n4. Exit")
        
        choice = int(input("What do you want to do?: "))
        
        if choice == 1:
            answerChecker() 
        elif choice == 2:
            memoryBank()
        elif choice == 3:
            guessNumber()
        elif choice == 4:
            print("Goodbye!")
            keepGoing = False
        else:
            print("Invlid choice... Please enter a valid choice.")
    sys.exit() # I use this to exit program, because I still dont know another way to end it before its done.
    
def problem(prob):
    """
    Takes user input and breaks problem up for calculation
    """
    if "+" in prob: 
        question = prob.split("+") #splits the string by the symbol
        x = int(question[0])
        y = int(question[1])
        t = "+"
        z = calculate(x,t,y)
        return z,x,t,y
    elif "-" in prob:
        question = prob.split("-") #splits the string by the symbol
        x = int(question[0])
        y = int(question[1])
        t = "-"
        z = calculate(x,t,y)
        return z,x,t,y
    elif "/" in prob:
        question = prob.split("/") #splits the string by the symbol
        x = int(question[0])
        y = int(question[1])
        t = "/"
        z = calculate(x,t,y)
        return z,x,t,y
    elif "*" in prob:
        question = prob.split("*") #splits the string by the symbol
        x = int(question[0])
        y = int(question[1])
        t = "*"
        z = calculate(x,t,y)
        return z,x,t,y
        
def calculate(x,t,y):
    """
    Takes seperated equation and calculates answer
    """
    
    if t == "+":
        z = x + y
        return z
    elif t == "-":
        z = x - y
        return z
    elif t == "/":
        z = x/y
        return z
    elif t == "*":
        z = x*y
        return z
        
        
def answerChecker():
    """
    Enter an equation and solve it. Your score is kept
    """
    print("\n\n","-"*8,"Answer Checker","-"*8)
    print("\nTo play enter a math problem, and answer it.")
    print("\nIf you get it right I'll let you know!")
    print("\nAfter 10 problems, I will let you know your score!")
    print("\nIf you want to quit before that, \njust enter 'exit'!")
    print("\n","~"*8,"Let's Play!","~"*8)
    
    keepGoing = True
    right = 0
    while keepGoing ==True:
        for i in range(10):
            prob = input("Enter your math problem! ")
            z,x,t,y = problem(prob)
            answer = input("Enter your answer: ")
            if answer == 'exit':
                main()
            elif int(answer) == z:
                print("You got it right!")
                right += 1
            else:
                print("You got it wrong...")
        print("-"*8,right," out of 10","-"*8)
        print("Do you want to go again? y/n")
        again = input()
        if again == 'y':
            keepGoing = True
        else:
            keepGoing = False
            
    
def memoryBank():
    """
    - Saves 10 math problems intered by user
    - displays those problems for user to answer
    - times the user on how long it takes for them to answer the questions
    - displays their score and time
    """
    
    keepGoing = True
    
    while keepGoing == True:
        print("\n\n","-"*8,"Memory Bank","-"*8)
        print("1. Enter 10 new problems")
        print("2. Answer the problems")
        print("3. exit")
        
        choice = int(input("What do you want to do?: "))
    
        if choice == 1:
            memBankProblems()
        elif choice == 2:
            memBankGame()
        elif choice == 3:
            keepGoing == False
        else:
            print("Invalid entry...Please try again!")
    main()    
        
        
def memBankProblems():
    """
    - Saves 10 math problems intered by user into txt file
    """
    print("\n\n","~"*8,"Memory Bank Problems","~"*8)
    print("\nEnter 10 math problems for me to remember!")
    with open('memBankFile.txt', mode='w') as file:
        for i in range(3):
            prob = input("Enter your math problem: n+n ")
            print(prob, file=file)
            
    return

def memBankGame():
    print("\n\n","~"*8,"Memory Bank Game","~"*8)
    print("Enter your answer for each problem shown!")
    print("You have 2 tries for each problem!")
    print("If you want to quit type 'exit'.")
    print("At the end of the game, I will tell you your score!")
    print("Good luck!")
    start = time.time()
    score = 0
    outOf = 0
    with open('memBankFile.txt', mode='r') as file:   
        for line in file:
            outOf += 1
            z,x,t,y = problem(line)
            print("\n",x, t, y)
            count = 0
            while count != 2:
                answer = input("\nEnter your answer: ")
                if answer == 'exit':
                    main()
                else:
                    answer = int(answer)
                    if answer == z:
                        print('Correct!')
                        count = 2
                        score += 1
                        print(score, outOf)
                    else:
                        print("Wrong Answer. Try again.")
                        count +=1
                        print(score, outOf)
    end = time.time()
    timeLapsed = end - start
    print("~"*4,"Score: ",score," out of ",outOf,"-"*4, round(timeLapsed), ' seconds')
                
    
def guessNumber():
    """
    Player guesses a random number known by the calculator
    """
    print("\n\n","~"*8,"Number Guesser","~"*8)
    print("\nI will have a number between 0 and 100, you try to guess it!")
    print("\nI will let you know if its too low or too high!")
    print("\nI will also let you know two numbers its between!")
    print("\nEnter 'exit' to end the game!")
    print("\nLet's Play!\n")
    keepGoing = True
    
    while keepGoing == True:
        
        num = random.randint(0,100) # I used randint instead of seed, because it generates a random number in a range
        print("\nI have a number between 0 and 100. What is it?\n")
        guess = input("Your guess: ")
        if guess == 'exit':
            main()
        guess = int(guess)
        tries = 1
        while guess != num:
            guessedWrong(num,guess)        
            guess = input("\nYour guess: ")
            if guess == 'exit':
                main()
            guess = int(guess)
            tries += 1
        if guess == num:
            print("\nCorrect!")
            print("\nYou tried ", tries, " many times!\n")
            print("\n Do you want to play again? y/n ")
            choice = input()
            if choice =='y':
                keepGoing == True
            elif choice == 'n':
                main()
        else:
            print("Something went wrong")
    main()
    
def guessedWrong(num,guess):
    """
    Cacluates if wrong answer is too high or too low and displays that
    """
    numLow = random.randint(0,(num - 1))
    numHigh = random.randint((num + 1), 100)
    if guess < num:
        print("\nToo Low...",numLow, " ? ",numHigh, "...Try Again..")
    elif guess > num:
        print("\nToo High...",numLow, " ? ",numHigh, "...Try Again..")        
        
        
if __name__ == "__main__":
    main()