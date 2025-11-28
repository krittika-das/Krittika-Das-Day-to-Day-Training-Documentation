l=[9, 0, 6, 2, 8 ,8, 0, 5, 8, 6]
N=int(input("Enter no. of positions: "))
if N>len(l):
    N=N%len(l)+1
k=[]
for i in range(len(l)-N, len(l)):
    k.append(l[i])
for i in range(0, len(l)-N):
    k.append(l[i])
print(k)
