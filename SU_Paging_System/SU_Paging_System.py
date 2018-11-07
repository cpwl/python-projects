import random
clockedInStaff = ['Clara', 'Tom', 'Benny', 'Paige']     #test data
Main()



def Main():
    while True:
        

        selection = input()

        if selection == "1":
            pageStaff()
        elif selection == "2":
            logIn()
        elif selection == "3":
            logOut()
        elif selection == "4":
            clockIn()
        elif selection == "5":
            clockOut()
        elif selection == "6":
            break


def printMenu():
    print('SU PAGING SYSTEM')
    print('')
    print('The staff members currently on shift are:')
    print("\n".join(clockedInStaff))
    print('')
    print('Please select an option:')
    print("1: Page staff member")
    print("2: Log into till")
    print("3: Log out of till")
    print("4: Clock in")
    print("5: Clock out")


#def pageStaff():
    #print(clockedInStaff)

#def logIn():


#def logOut():


#def clockIn():


#def clockOut():

