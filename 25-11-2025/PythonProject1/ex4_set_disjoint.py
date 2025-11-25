a={1, 2, 3}
b={4, 2, 6}
s=set()
for i in a:
    if i in b:
        s.add(i)
if len(s)==0:
    print("Set is disjoint.")
else:
    print("Set is not disjoint.")