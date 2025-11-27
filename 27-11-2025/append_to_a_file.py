with open("notes.txt", "a") as f:
    f.write("This is an appended line \n")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)