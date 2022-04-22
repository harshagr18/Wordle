import solver
import dbFunc
from datetime import date

today = date.today()

if __name__ == "__main__":

    dbFunc.createTable()
    dbFunc.createTable2()

    #"+ gid +", " +first+", "+second+", "+third+", "+fourth+", "+fifth+", "+sixth+", "+attempts+")
    #"+ gid +", " +solution+", "+win+")"

    #recordGame(gid, first, second, third, fourth, fifth, sixth, attempts)
    #gameComplete(gid, solution, win)
    

    for i in range(1000):
        print("Game being played is number: ",i+1)
        todayDate = today.strftime("%m/%d/%y")
        win,guesses,attempts,solution,gid = solver.playGame()
        solution = "".join(solution)
        for _ in range(6-attempts):
            guesses.append("NONE")

        dbFunc.recordGame(gid,guesses[0],guesses[1],guesses[2],guesses[3],guesses[4],guesses[5],attempts)
        dbFunc.gameComplete(gid,todayDate, solution, win)