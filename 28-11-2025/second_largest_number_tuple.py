k=(88, 72, 32, 11, 90, 76)
ki=max(k)
n=k[0]
for i in k:
    if i>n and i!=ki:
        n=i
print(n)
