import random
import winsound
import sys

def playGame():
    print("Ok", name,", I will sound the speaker beep at a particular frequency and you must estimate the frequency.")
    playFrequency = random.randint(37, 8000)
    winsound.Beep(playFrequency,1)
    frequency = input("What frequency do you estimate that sound to have been? ")
    if frequency == playFrequency:
        input("You are correct!")
    else:
        print("Hard luck, the frequency was", playFrequency)
        input()


validName = False
while validName == False:
    name = input("Please enter your name: ")
    if len(name) < 1:
        print("No name entered. Please try again.")
    else:
        validName = True

i = 1
while True:
    response = input("Do you want to take the estimate the frequency challenge? Enter y or n: ")
    if response == "y":
        playGame()
        i = i + 1
    elif response == "n":
        break
    else:
        input("Please enter y or n.")
    if i >= 10:
        input("You have exceeded your estimate limit!")
        break
