def remove_duplicates(lst):
    s=set()
    r=[]
    for x in lst:
        if x not in s:
            r.append(x)
            s.add(x)
    return r

print(remove_duplicates([1,2,3,4,5,6,7,8,9,10])) 