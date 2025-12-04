ll=[("a", 1), ("b", 2), ("c", 3), ("d", 4)]
keys=[]
valid=True

for k, v in ll:
    if k in keys:
        valid=False
        break
    keys.append(k)

if valid:
    re=dict(ll)
    print(re)
else:
    print("Not valid")