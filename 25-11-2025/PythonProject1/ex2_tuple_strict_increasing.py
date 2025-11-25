x=[1, 4, 5, 67, 29, 99]
z=1
for i in range(0, len(x)-1):
    if x[i+1]<x[i]:
        z=0
        break
if z==1:
    print("Strictly increasing")
else:
    print("Not strictly increasing")