s={1, 2, 3, 4}
d={3, 4, 5}
m=s|d
x=s&d
for i in m:
    if i not in x:
        print(i)