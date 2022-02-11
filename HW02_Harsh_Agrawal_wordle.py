#Pseudocode

"""
SET solution word
WHILE number of attempts run out or user wins
    CHECK if number of attempts remaining are 0
    WHILE input is not 5 letters, unseen word and alphabetic
        TAKE user input
    FOR each letter in the input word
        CHECK if correct letter is in correct position (primary)
    FOR each letter in the input word
        CHECK if correct letter is in incorrect position (secondary)
    CHECK if each letter is guessed correctly (User wins)
"""



#Game Introduction
print()
print("Welcome to wordle")
print()
print("Correct letters in correct positions will have a '+' under them, correct letters in incorrect positions will have a '^' under them and incorrect letters will have '-' under them.")
print("You will have 6 guesses.")
print()


solution = list("SOOON") # Solution variable
attempts = 6 # Number of attempts allowed
attemptList = [] # Records number of user's tried words

while True: # Runs the loop until number of attempts run out, or the user wins.
    if(attempts == 0): 
        print("Sorry, you lose. Better luck next time")
        print()
        break
    flag = 0 # Tracks number of letters rightly guessed in the correct position on each attempt to check if user has one
    result = ["","","","",""] # Assigns "+","-" or "^" depending on correct and incorrect letters and positions
    search = ["0","0","0","0","0"] # Used to check if a letter has been used, so same letter doesn't give 2 positive outputs.
    pos = 0 # Used to track the letter that is being used in the actual word to create result
    print("This is attempt number ",(7-attempts)) 
    print()
    while True: # Input from user until the correct type of input is provided (size, alphabetic, not previously used)
        userInput = list(input().upper())

        if(len(userInput) == 5):
            if("".join(userInput) not in attemptList):
                if("".join(userInput).isalpha()):
                    break
                else:
                    print("The word contains non alphabetic characters. (Please retry)")
            else:
                print("Word has been tried before. (Please retry)")
        else:
            print("Word length is not 5. (Please retry)")
    
    attemptList.append("".join(userInput))
    
    for i in range(5): # Checking for correct letters in correct positions first, to ensure highest priority
        if(userInput[i] == solution[i]):
            flag = flag + 1
            result[i] = ("+ ")
            search[i] = 1

    for i in range(5): # Checking for correct letters in incorrect position and lastly incorrect letters
        if(userInput[i] in solution and result[i] == ""):
            pos = "".join(solution).find(userInput[i])
            if(search[pos] == 1):
                result[i] = ("- ")
            else:
                result[i] = ("^ ")
                search[pos] = 1
        elif result[i] == "":
            result[i] = ("- ")


    print()
    print(" ".join(userInput))
    print("".join(result))
    print()
    if(flag == 5): # Checking if the user has won
        print("Congratulations! You win.")
        break
    attempts = attempts-1