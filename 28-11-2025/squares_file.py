with open("squares_file.txt", "a") as file:
    for i in range(1, 21):
        f=f"{i**2} \t"
        file.write(f)

