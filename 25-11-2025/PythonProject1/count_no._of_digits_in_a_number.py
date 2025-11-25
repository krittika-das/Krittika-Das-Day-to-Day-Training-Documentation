a=int(input("Enter a number: "))
c=0
while a>0:
    a=a//10
    c=c+1
print("No. of digits = ", c)