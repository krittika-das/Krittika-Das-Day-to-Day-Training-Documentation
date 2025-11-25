a=[1, 2, 3, 2, 4, 1, 5, 1]
x=[]
for i in a:
    if a.count(i)>1:
        x.append(i)

n=[]
for z in x:
    if z not in n:
        n.append(z)

print(z)