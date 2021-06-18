def flower():
    f = open("Flowers.txt", "r")
    word= f.read().split()
    f_new = open("New_file.txt" , "w")
    Dif = []
    for w in word:
        if w not in Dif:
                Dif.append(w)

    Dif.sort(key=len)
    print(Dif)

    for w in Dif:
        f_new.write(w + " : " + str(len(w)) + "\n")
flower()