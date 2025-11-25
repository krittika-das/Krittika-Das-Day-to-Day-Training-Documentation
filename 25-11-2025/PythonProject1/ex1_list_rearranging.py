a=[2, -9, 7, 6, -66, -23, 9]
k=[]
for i in a:
    if i<=0:
        k.append(i)
for i in a:
    if i>0:
        k.append(i)
print(k)