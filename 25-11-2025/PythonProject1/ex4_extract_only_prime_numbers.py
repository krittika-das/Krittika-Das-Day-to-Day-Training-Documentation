nums=[10, 11, 12, 13, 17, 18, 20, 23]
x=[]
c=0
for i in nums:
    for k in range(2,i):
        if i%k==0:
            c=c+1
    if c==0:
        x.append(i)
    c=0
print(x)

