def longest(s):
    k=s.split(" ")
    long=k[0]
    for i in k:
        if len(i)>len(long):
            long=i
    return long

print(longest("Hi how are you doing? Well, I am fine"))


