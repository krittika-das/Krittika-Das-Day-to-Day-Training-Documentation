inp={"a": 1, "b": 2, "c": 1}
inv={}
for k, v in inp.items():
    if v not in inv:
        inv[v]=[]
    inv[v].append(k)
print(inv)
