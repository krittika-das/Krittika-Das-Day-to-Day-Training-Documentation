with open ("products.txt") as file:
    data=file.readlines()

s=""
for x in data:
    y=x.split(" ")
    s=f"{y} \t \n"
    with open("catalog.txt", "a") as f:
        f.write(s)
