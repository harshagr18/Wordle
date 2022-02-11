if __name__ == "__main__":
    print("Please run the wordle applcation.")

import HW03_Harsh_Agrawal_dictionary as dictionary

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