x=input("Enter a string: ")
s=""
for a in x:
    if a not in "%!@#$^&*(){}[]|:;<>/?":
        s=s+a
print("Updated string: ", s)