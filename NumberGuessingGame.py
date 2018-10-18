import random

def pcGuesses():
    minGuess = 1
    maxGuess = 100
    solved = False
    guess = 50
    answer = str
    #print("Please enter your username:", " ")
    #username = input()

    while solved == False:
        guess = (maxGuess + minGuess) / 2
        guess = round(guess, 0)
        print("Is your number ", guess, end = "? (y/n)") 
        answer = input()

        if answer == "y":
            solved = True
        elif answer == "n":

            print("Was the guess too high? (y/n)")
            answer = input()

            if answer == "y":
                maxGuess = guess
            elif answer == "n":
                minGuess = guess
            else:
                print("Please use y or n as an answer.")
                input()   

        else: 
            print("Please use y or n as an answer.")
            input()

    print("Thank you for playing!")
    input()
 
#def userGuesses()


while True:
    print("Welcome to the Number Guessing Game.")
    print("Please input a menu selection:")
    print()
    print("1: PC guesses user's number")
    print("2: User guesses PC's number")
    print("3: Quit the program")
    answer = input()

    if answer == "1":
        pcGuesses()

    #elif answer == 2:
        #userGuesses()

    elif answer == "3":
        break

   