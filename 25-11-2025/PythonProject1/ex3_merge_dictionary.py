a={'a': 1, 'b': 2}
b={'b': 3, 'c': 4}
merge={}
for k,v in a.items():
    merge[k]=v

for k,v in b.items():
    if k in merge:
        if type(merge[k])==list:
            merge[k].append(v)
        else:
            merge[k]=[merge[k],v]
    else:
        merge[k]=v
print(merge)