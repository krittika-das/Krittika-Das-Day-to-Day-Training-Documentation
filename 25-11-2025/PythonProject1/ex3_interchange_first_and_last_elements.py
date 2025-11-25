x=['a', 'b', 'c', 'd', 'e']
a=x[0]
x[0]=x[len(x)-1]
x[len(x)-1]=a
print(x)