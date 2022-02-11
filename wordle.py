import ui
import dictionary


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
ui.gameIntro()

solution = dictionary.randomWord() # Generate a random word
 
print("Solution is ",solution,"\n")# Debug Line
attempts = 6 # Number of attempts allowed
attemptList = [] # Records number of user's tried words

while True: # Runs the loop until number of attempts run out, or the user wins.
    if ui.checkWin(attempts):
        ui.printStats(attempts)
        break
    flag = 0 # Tracks number of letters rightly guessed in the correct position on each attempt to check if user has one
    result = ["","","","",""] # Assigns "+","-" or "^" depending on correct and incorrect letters and positions
    search = ["0","0","0","0","0"] # Used to check if a letter has been used, so same letter doesn't give 2 positive outputs.
    pos = 0 # Used to track the letter that is being used in the actual word to create result


    ui.printAttempts(attempts) # Current attempt number
    
    userInput = ui.userInputAndCheck(attemptList) # Check if word is valid
    attemptList.append("".join(userInput)) # Track used words
    
    for i in range(5): # Checking for correct letters in correct positions first, to ensure highest priority
        if(userInput[i] == solution[i]):
            flag = flag + 1
            result[i] = (" ")
            search[i] = 1

    for i in range(5): # Checking for correct letters in incorrect position and lastly incorrect letters
        if(userInput[i] in solution and result[i] == ""):
            pos = "".join(solution).find(userInput[i])
            if(search[pos] == 1):
                result[i] = ("\"")
            else:
                result[i] = ("'")
                search[pos] = 1
        elif result[i] == "":
            result[i] = ("\"")


    ui.printRound(userInput,result) # Show result of current input

    if ui.checkWin(attempts,flag): # Check if user has won / out of attempts
        ui.printStats(attempts,flag)
        break
    
    attempts = attempts-1
else:
    print("hi")