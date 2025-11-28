x=[2, 3, 3, 4, 5, 6, 6, 7, 9, 9]
s=set(x)
for i in s:
    c=x.count(i)
    if c==2:
        print(i)
