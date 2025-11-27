with open("notes.txt", "r") as f:
    c=0
    for l in f:
        w=l.split(" ")
        c=c+len(w)
    print(c)