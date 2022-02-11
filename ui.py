if __name__ == "__main__":
    print("Please run the wordle applcation.")

import dictionary

def printStats(attempts,flag=0):
    f = open("scores.txt", "r")
    data = f.read().split("\n")
    f.close()
    
    games = int(data[0]) + 1
    
    wins = int(data[1])
    if flag == 5:
        wins = wins+1

    attempt1 = int(data[2])
    attempt2 = int(data[3])
    attempt3 = int(data[4])
    attempt4 = int(data[5])
    attempt5 = int(data[6])
    attempt6 = int(data[7])

    print(attempts)

    if attempts == 6:
        print(attempt1)
        attempt1 = attempt1 + 1
        print(attempt1)
    elif attempts == 5:
        attempt2 = attempt2 + 1
    elif attempts == 4:
        attempt3 = attempt3 + 1
    elif attempts == 3:
        attempt4 = attempt4 + 1
    elif attempts == 2:
        attempt5 = attempt5 + 1
    elif attempts == 1:
        attempt6 = attempt6 + 1

    print()
    print("Total Number of Games Played:",games)
    print()
    print("Your win percentage is",int(wins * 100 /games),"%")
    print()
    print("Number of times you have won on the 1st attempt:",attempt1)
    print("Number of times you have won on the 2nd attempt:",attempt2)
    print("Number of times you have won on the 3rd attempt:",attempt3)
    print("Number of times you have won on the 4th attempt:",attempt4)
    print("Number of times you have won on the 5th attempt:",attempt5)
    print("Number of times you have won on the 6th attempt:",attempt6)

    f = open("scores.txt", "w")
    f.write(str(games) + "\n")
    f.write(str(wins) + "\n")
    f.write(str(attempt1) + "\n")
    f.write(str(attempt2) + "\n")
    f.write(str(attempt3) + "\n")
    f.write(str(attempt4) + "\n")
    f.write(str(attempt5) + "\n")
    f.write(str(attempt6))
    f.close()

def gameIntro(): # Introduce the game
    print()
    print("Welcome to wordle")
    print()
    print("Correct letters in correct positions will have a ' ' under them, correct letters in incorrect positions will have a '\'' under them and incorrect letters will have '\"' under them.")
    print("You will have 6 guesses.")
    print()


def printAttempts(attempts): # Give current attempt number
    print("This is attempt number ",(7-attempts),":",end="")

def userInputAndCheck(attemptList): # Take user input and check if it is valid
    while True: # Input from user until the correct type of input is provided (size, alphabetic, not previously used)
        userInput = list(input().upper())

        if(len(userInput) == 5):
            if("".join(userInput) not in attemptList):
                if("".join(userInput).isalpha()):
                    if(dictionary.checkWord("".join(userInput))):
                        break
                    else:
                        print("Not a valid dictionary word")
                else:
                    print("The word contains non alphabetic characters. (Please retry)")
            else:
                print("Word has been tried before. (Please retry)")
        else:
            print("Word length is not 5. (Please retry)")
    return userInput

def checkWin(attempts,flag=0): # Check if the user won or lost
    if(attempts == 0): 
        print("Sorry, you lose. Better luck next time")
        print()
        return True
    elif(flag == 5):
        print("Congratulations! You win.")
        print()
        return True
    return False

def printRound(userInput,result): # Print result of the round
    print()
    print("".join(userInput))
    print("".join(result))
    print()