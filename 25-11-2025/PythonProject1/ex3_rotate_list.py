n=[2, 3, 4, 5, 6, 5 , 4, 6, 7]
k=[]
ni=int(input("Enter N: "))
for x in range(ni, len(n)):
    k.append(n[x])
for x in range(0, ni):
    k.append(n[x])
print(k)
