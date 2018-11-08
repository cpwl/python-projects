

def Main():
    while True:
        printMenu()
        selection = input() 
        if selection == "1":
            clear
            pageStaff(availableStaff) 
        elif selection == "2":
            clear
            logIn(availableStaff)
        elif selection == "3":
            clear
            logOut()
        elif selection == "4":
            clear
            clockIn()
        elif selection == "5":
            clear
            clockOut()
        elif selection == "6":
            break


def printMenu():
    print('\n' * 40)
    print('SU PAGING SYSTEM')
    print('\n' * 2)
    print('Staff members available to be paged:')
    print("\n".join(availableStaff))
    print('\n' * 2)
    print('Please select an option:')
    print("1: Page staff member")
    print("2: Log into till")
    print("3: Log out of till")
    print("4: Clock in")
    print("5: Clock out")
    print("6: Quit")


def pageStaff(availableStaff):
    answer = input("Which staff member would you like to page? ")
    foundStaff = False    
    for staff in availableStaff:
        if answer == staff:
            foundStaff = True
            # Send signal to staff members phone #
            print("A message has been sent to ", staff)
            availableStaff = [x for x in availableStaff if x != staff]
    
    if foundStaff == False:
        print("Staff member could not be found.")

def logIn(availableStaff):
    answer = input("Please enter your name: ")
    for staff in availableStaff:
        if answer == staff:
            print("Hello ", staff, ", you are now logged in.")
            availableStaff = [x for x in availableStaff if x != staff]
            input()
            

def logOut():
    answer = input("Please enter your name: ")
    for staff in clockedInStaff:
        if answer == staff:
            print(staff, " is now logged out.")
            availableStaff.append(staff)
            input()

def clockIn():
    answer = input("Please enter your name: ")
    for staff in clockedInStaff:
        if staff == answer:
            print("That user is already clocked in.")
            input()
            return
    clockedInStaff.append(answer)
    availableStaff.append(answer)

def clockOut():
    answer = input("Please enter your name: ")
    for staff in clockedInStaff:
        if answer == staff:
            print("You are now clocked out.")

            input()
            return


import random
import os
clear = lambda: os.system('clear') # allows the interpreter to clear the runtime console
clockedInStaff = ['Clara', 'Tom', 'Benny', 'Paige']     # test data
availableStaff = ['Clara', 'Tom', 'Benny', 'Paige']
Main()
