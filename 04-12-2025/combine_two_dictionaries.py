d1={"a":1,"b":2,"c":3}
d2={"b":1,"c":2,"f":3}
r={}
for k, v in d1.items():
    r[k]=v
for k, v in d2.items():
    if k in r:
        r[k]+=v
    else:
        r[k]=v
print(r)