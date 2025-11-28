a={1, 2, 3}
b={3, 4, 5}
k=set()
for i in a:
    if i not in b:
        k.add(i)
for i in b:
    if i not in k:
        k.add(i)

print(k)

