import ui
import dictionary

def wordle(solution,wordList):
    #Game Introduction
    ui.gameIntro()
    win = "False"

    testTest = 0

    print("Solution is ",solution,"\n")# Debug Line
    attempts = 6 # Number of attempts allowed
    attemptList = [] # Records number of user's tried words

    while True: # Runs the loop until number of attempts run out, or the user wins.
        if ui.checkWin(attempts):
            if flag == 5:
                win = "True"
            ui.printStats(attempts)
            break
        flag = 0 # Tracks number of letters rightly guessed in the correct position on each attempt to check if user has one
        result = ["","","","",""] # Assigns "+","-" or "^" depending on correct and incorrect letters and positions
        search = ["0","0","0","0","0"] # Used to check if a letter has been used, so same letter doesn't give 2 positive outputs.
        pos = 0 # Used to track the letter that is being used in the actual word to create result


        ui.printAttempts(attempts) # Current attempt number
        
        userInput = ui.userInputAndCheck(attemptList,wordList[testTest]) # Check if word is valid
        if userInput == "error1":
            return "Size error"
        elif userInput == "error2":
            return "Not alphabetic"
        elif userInput == "error3":
            return "Word has already been tried"
        elif userInput == "error4":
            return "Not a dictionary word"
        testTest = testTest + 1
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
            if flag == 5:
                win = "True"
            ui.printStats(attempts,flag)
            break
        
        attempts = attempts-1
    
    
    return win


if __name__ == "__main__":
    wordle()