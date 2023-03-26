# GUESS THE NUMBER GAME 
import random
while 1:
    x=input("Do you want to play the game(y/n): ")
    while x=="y":
        number = (random.randint(1,100))
        score=10
        guess=int(input("Guess the number between 1 to 100: "))
        while guess!=number:
            if guess<number:
                score=score-1
                if (score>=1):
                    print("Buzz!! you guessed the number wrong. Think of a bigger number")
                    print("You have {} chances left".format(score))
                else:
                    print("Buzz!! you guessed it wrong")
                    print("Thank you. Better luck next time.")
                    exit()    
                guess=int(input("Guess the number between 1 to 100: "))  
            else:
                score=score-1
                if (score>=1):
                    print("Buzz!! you guessed the number wrong. Think of a smaller number")
                    print("You have {} chances left".format(score))
                else:
                    print("Buzz!! you guessed it wrong")
                    print("Thank you. Better luck next time.")
                    exit()
                guess=int(input("Guess the number between 1 to 100: "))
        print("Yes!! You guessed the correct number")
        break
    if x=="n":
        print("!!Thank you. Hope you liked the game!!")
        exit()

        
