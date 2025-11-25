#Exercise 17: sum of first n natural numbers
s=0
n=int(input("Enter: "))
for i in range(1, n+1):
    s+=i
print(s)