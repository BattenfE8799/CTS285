#M2HW1 Sprint 1-AnswerChecker
#CTS-285-0001
#Elizabeth Battenfield

"""
Main menu
"""

def main():
    """
    Main menu
    """
    keepGoing = True
    
    while keepGoing == True:
        print("\n","-"*8,"Menu","-"*8)
        print("\n1. Answer Checker \n2. to do")
        print("3. Memory Bank\n4. Number Guesser\n5. Exit")
        
        choice = int(input("What do you want to do?: "))
        
        if choice == 1:
            answerChecker()
        elif choice == 2:
            return
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
    
        
        
    
        
        
        




            
main()