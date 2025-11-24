kl=[10, 20, 30, 40, 50]
print(kl)

fruits=["cherry", "apple", "tomato"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])

l=[]
for i in range(1, 21):
    l.append(i)
print(l)
for i in l:
    if i%2==0:
        print(i, " is even.")
    else:
        print(i, " is odd.")
