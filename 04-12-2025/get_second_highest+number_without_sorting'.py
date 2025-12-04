val=[2, 4, 55, 65, 72, 23, 13]
h=min(val)
s=min(val)
for i in val:
    if i>h:
        s=h
        h=i
    elif h>i>s:
        s=i
print(s)