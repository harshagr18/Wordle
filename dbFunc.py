import sqlite3

def createTable():
    con = sqlite3.connect('record.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE record (id integer primary key, first text, second text, third text, fourth text, fifth text, sixth text, attempts real)''')
    con.commit()
    con.close()

def createTable2():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE database (id integer primary key,date text, solution text, win text)''')
    con.commit()
    con.close()

def recordGame(gid, first, second, third, fourth, fifth, sixth, attempts):
    con = sqlite3.connect('record.db')
    cur = con.cursor()
    execute = "INSERT INTO record VALUES  ('"+ str(gid) +"','" +first+"', '"+second+"', '"+third+"', '"+fourth+"', '"+fifth+"', '"+sixth+"', '"+str(attempts)+"')"
    cur.execute(execute)
    con.commit()
    con.close()

def gameComplete(gid,date, solution, win):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    execute = "INSERT INTO database VALUES  ('" + str(gid) +"', '"+ date +"', '"+ solution +"', '"+ win +"')"
    cur.execute(execute)
    con.commit()
    con.close()