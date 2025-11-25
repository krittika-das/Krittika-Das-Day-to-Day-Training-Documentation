a=[0, 3, 0, 5, 7, 0, 9]
x=[]
for i in a:
    if i!=0:
        x.append(i)
for i in a:
    if i==0:
        x.append(i)
print(x)