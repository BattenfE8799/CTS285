#M2HW1 Sprint 2- Memory Bank
#CTS-285-0001
#Elizabeth Battenfield

import time
import sys

def main():
    """
    Main menu
    """
    keepGoing = True
    
    while keepGoing == True:
        print("\n","-"*8,"Menu","-"*8)
        print("\n1. Answer Checker \n2. Memory Bank")
        print("3. Number Guesser\n5. Exit")
        
        choice = int(input("What do you want to do?: "))
        
        if choice == 1:
            answerChecker()
        elif choice == 2:
            memoryBank()
        elif choice == 3:
            return
        elif choice == 4:
            return
        elif choice == 5:
            print("Goodbye!")
            keepGoing = False
        else:
            print("Invlid choice... Please enter a valid choice.")
        
def answerChecker():
    """
    Enter an equation and solve it. Your score is kept
    """
    print("\n\n","-"*8,"Answer Checker","-"*8)
    print("\nTo play enter a math problem, and answer it.")
    print("\nIf you get it right I'll let you know!")
    print("\nAfter 10 problems, I will let you know your score!")
    print("\nIf you want to quit before that, \njust enter 'exit' when I ask for the symbol!")
    print("\n","~"*8,"Let's Play!","~"*8)
    
    keepGoing = True
    right = 0
    while keepGoing ==True:
        for i in range(10):
            x = int(input("Enter your first number: "))
            t = input("Enter + , - , / , or * or exit: ")
            y = int(input("Enter your second number: "))
            z = calculate(x,t,y)
            answer = int(input("Enter your answer: "))
            if answer == z:
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
            
def calculate(x,t,y):
    """
    Takes equation and calculates answer
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
    elif t == 'exit':
        exit
    
        
def memoryBank():
    """
    - Saves 10 math problems intered by user
    - displays those problems for user to answer
    - times the user on how long it takes for them to answer the questions
    - displays their score and time
    """
    print("\n\n","-"*8,"Memory Bank","-"*8)
    print("1. Enter 10 new problems")
    print("2. Answer the problems")
    print("3. exit")
    choice = int(input())
    if choice == 1:
        memBankProblems()
    elif choice == 2:
        memBankGame()
    elif choice == 3:
        goodBye()
        
def memBankProblems():
    print("Enter 10 math problems for us to remember!")
    with open('memBankFile.txt', mode='w') as file:
        for i in range(3):
            x = input("Enter your first number: ")
            t = input("Enter + , - , / , or * or exit: ")
            y = input("Enter your second number: ")
            print(x+t+y, file=file)
            
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
            if "+" in line:
                question = line.split("+")
                x = int(question[0])
                y = int(question[1])
                t = "+"
                z = calculate(x,t,y)
                print(z)
            elif "-" in line:
                question = line.split("-")
                x = int(question[0])
                y = int(question[1])
                t = "-"
                z = calculate(x,t,y)
            elif "/" in line:
                question = line.split("/")
                x = int(question[0])
                y = int(question[1])
                t = "/"
                z = calculate(x,t,y)
            elif "*" in line:
                question = line.split("*")
                x = int(question[0])
                y = int(question[1])
                t = "*"
                z = calculate(x,t,y)
                
            print("\n",x, t, y)
            count = 0
            while count != 2:
                answer = input("\nEnter your answer: ")
                if answer == 'exit':
                    goodBye()
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
                
def goodBye():
    return
    
    
    
    
        
        
        




            
main()