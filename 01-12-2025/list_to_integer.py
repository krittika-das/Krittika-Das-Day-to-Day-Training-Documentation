l=['1', '5', '9', 's', '8']
try:
    for i in range(len(l)):
        l[i]=int(l[i])
except ValueError:
    print("Value Error")
print(l)