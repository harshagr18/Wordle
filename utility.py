if __name__ == "__main__":
    f = open("words.txt", "r")
    data = f.read().split("\n")
    words = []
    for j in data:
        if len(j) == 5:
            words.append(j)

    f.close()
    f = open("5Letter.txt","w")
    for i in words:
        temp = i.upper() + "\n"
        f.write(temp)
else:
    print("Please run utility module directly, not for imports.")