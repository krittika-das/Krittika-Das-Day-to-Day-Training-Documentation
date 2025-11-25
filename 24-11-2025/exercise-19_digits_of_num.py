#exercise 19: count digits in a number
a=int(input("Input any number: "))
c=0
while a>0:
    a=a//10
    c+=1
print("Total digits: ", c)