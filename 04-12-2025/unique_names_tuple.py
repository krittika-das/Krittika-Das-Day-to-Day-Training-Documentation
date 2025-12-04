n=('Ram', 'Geeta', 'Resham')
u=[]
for k in n:
    if k not in u:
        u.append(k)

u=tuple(u)
print(u)