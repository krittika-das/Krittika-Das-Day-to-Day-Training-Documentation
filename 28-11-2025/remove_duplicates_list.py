l=[2, 2, 1, 3, 4, 3, 5, 4, 2]
x=[]
for i in l:
    if i not in x:
        x.append(i)
print(x)