a={2: 77, 3: 89, 9: 90}
b={1: 97, 3: 88, 5: 32}

x={}
for k, v in a.items():
    x[k] = v

for k, v in b.items():
    if k in x:
        a=x[k]
        x[k]=[]
        x[k].append(a)
        x[k].append(v)
    else:
        x[k]=v

print(x)