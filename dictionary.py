import random

def createWordList(): # Create list of 5 letter words, total 1379 words that are 5 letter in the list
    f = open("5Letter.txt", "r")
    data = f.read().split("\n")
    words = []
    for j in data:
        words.append(j)
    return words


def randomWord(): # Generate a random word for solution
    words = createWordList()
    f = open("UsedWords.txt","r+")
    data = f.read().split("\n")

    if (len(data)) >= 1378:
        print("Resetting wordlist")
        f.close()
        f.open("UsedWords.txt","w")
        f.close()
        randomWord()

    
    while True:
        solution = list(words[random.randint(0, 1378)].upper())
        if solution not in data:
            break

    f.write("\n"+"".join(solution))
    
    return solution

def checkWord(word): # Check if user entered word is valid
    words = createWordList()
    
    if word.upper() in words:
        return True
    else:
        return False
        
if __name__ == "__main__":
    print("Please run the wordle applcation.")
