with open("squares.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i*i) + "\n")

with open("squares.txt", "r") as f:
    print(f.read())