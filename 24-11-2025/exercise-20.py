#exercise 20: reverse a number
a=int(input("Enter a number: "))
rev=0
while(a>0):
    d=a%10
    rev=rev*10+d
    a=a//10
print(rev)
