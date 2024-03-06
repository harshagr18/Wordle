import sqlite3
from tokenize import maybe

con = sqlite3.connect('database.db')
cur = con.cursor()
gamesPlayed = []
win = 0
loss = 0

print("Please enter the date u want to check in the format m/d/y , example 04/22/22")
mydate = input()

for row in cur.execute('SELECT * FROM database'):
    if row[1] == mydate:
        gamesPlayed.append(row)
        if row[3] == "Win":
            win += 1
        else:
            loss += 1
con.close()

print()
print("On ",mydate)
print()
print("Number of games won are ",win)
print("Number of games lost are ",loss)
print("Win percentage is ",(win/1000)*100,"%")
print("Loss percentage is ",(loss/1000)*100,"%")


# con = sqlite3.connect('record.db')
# cur = con.cursor()
# for row in cur.execute('SELECT * FROM record'):
#     print(row)
# con.close()