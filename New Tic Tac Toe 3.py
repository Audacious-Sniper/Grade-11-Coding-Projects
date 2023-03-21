import random
spaces = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
def board():
    print( str(spaces[1]) + "|" + str(spaces[2]) + "|" + str(spaces[3]))
    print( str(spaces[4]) + "|" + str(spaces[5]) + "|" + str(spaces[6]))
    print( str(spaces[7]) + "|" + str(spaces[8]) + "|" + str(spaces[9]))
        #Inserts bar between ints for board look.

def ComputerPick():
    #Computer's choice
    ComputerChoice = random.randint(1, 9)
    if spaces[ComputerChoice] == "X" or spaces[ComputerChoice] == "0":
        ComputerPick()
    else:
        spaces[ComputerChoice] = "0"

def winchecker():
    if spaces[1] and spaces[2] and spaces[3] == "X":
        print("Winner!")
        return False
        #tells board to give back to loop
    elif spaces[4] and spaces[5] and spaces[6] == "X":
        print("Winner!")
        return False
    elif spaces[7] and spaces[8] and spaces[9] == "X":
        print("Winner!")
        return False
    elif spaces[1] and spaces[4] and spaces[7] == "X":
        print("Winner!")
        return False
    elif spaces[3] and spaces[6] and spaces[9] == "X":
        print("Winner!")
        return False
    elif spaces[1] and spaces[5] and spaces[9] == "X":
        print("Winner!")
        return False
    elif spaces[3] and spaces[5] and spaces[7] == "X":
        print("Winner!")
        return False

    elif spaces[1] and spaces[2] and spaces[3] == "0":
        print("You Lose!")
        return False
        #tells board to give back to loop
    elif spaces[4] and spaces[5] and spaces[6] == "0":
        print("You Lose!")
        return False
    elif spaces[7] and spaces[8] and spaces[9] == "0":
        print("You Lose!")
        return False
    elif spaces[1] and spaces[4] and spaces[7] == "0":
        print("You Lose!")
        return False
    elif spaces[3] and spaces[6] and spaces[9] == "0":
        print("You Lose!")
        return False
    elif spaces[1] and spaces[5] and spaces[9] == "0":
        print("You Lose!")
        return False
    elif spaces[3] and spaces[5] and spaces[7] == "0":
        print("You Lose!")
        return False
    else:
        return True

while True:
    #Loop statement
    board()
    #Player's Choice
    userchoice = input("Please select a location to place an X : ")
    spaces[int(userchoice)] = "X"
    if winchecker() == False:
        break
    #finds locations of number
    ComputerPick()

