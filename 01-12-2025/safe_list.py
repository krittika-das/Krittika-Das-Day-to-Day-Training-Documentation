try:
    l=[1, 2, 3, 4, 5]
    for i in range(0, len(l)+1):
        print(l[i])
except IndexError:
    print("Reached end while parsing.")