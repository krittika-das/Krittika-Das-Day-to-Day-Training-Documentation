x=[23, 44, 56, 22, 28, 9, 6, 7]
off=[]
eve=[]
for i in x:
    if i%2==0:
        off.append(i)
    else:
        eve.append(i)
print(off)
print(eve)