import random
#import winsound

def playGame():
    print("Ok", name,", I will sound the speaker beep at a particular frequency and you must estimate the frequency.")

    playFrequency = random.randint(37, 8000)
    #winsound.Beep(playFrequency, 1)
    frequency = input("What frequency do you estimate that sound to have been? ")
    if frequency == playFrequency:
        input("You are correct!")
    else:
        print("Hard luck, the frequency was", playFrequency)
        input()

name = input("Please enter your name: ")
response = input("Do you want to take the estimate the frequency challenge? Enter y or n: ")

if response == "y":
    playGame()





