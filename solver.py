import helper
import wordle
import random

if __name__ == "__main__":
    
    f = open("5Letter.txt")
    words = f.read().split("\n")
    solution = list(words[random.randint(0, 1378)].upper())
    attempts = 6

    good=[]
    bad=[]
    first=""
    second=""
    third=""
    fourth=""
    fifth=""

    guess = "SALES"
    guesslist = []
    print("The solution for this round is " ,solution)
    print()

    while attempts > 0:
        print("Let's play round ",7-attempts)
        print("This round I will guess ",guess)
        result,flag = wordle.play(solution,guess)

        if flag == 5:
            print("Congratulations you win")
            break

        for i in range(5):
            if result[i] == " " and i == 0:
                first = guess[i]
            
            elif result[i] == " " and i == 1:
                second = guess[i]
            
            elif result[i] == " " and i == 2:
                third = guess[i]
            
            elif result[i] == " " and i == 3:
                fourth = guess[i]
            
            elif result[i] == " " and i == 4:
                fifth = guess[i]

            elif result[i] == "'":
                good.append(guess[i])

        for i in range(5):
            if result[i] == '"' and guess[i] not in good and guess[i] != first and guess[i] != second and guess[i] != third and guess[i] != fourth and guess[i] != fifth:
                bad.append(guess[i])
                
        attempts = attempts - 1
        guesslist.append(guess)
        print()
        guess = helper.printTop(guesslist,good,bad,first,second,third,fourth,fifth)
        

    else: 
        print("You run out of attempts, you lose")
