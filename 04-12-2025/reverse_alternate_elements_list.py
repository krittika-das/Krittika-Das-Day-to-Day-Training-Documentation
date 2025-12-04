l=['one', 'two', 'three', 'four', 'five']
for i in range(len(l)):
    if i%2!=0:
        l[i]=l[i][::-1]
print(l)