s=(1, 11, 12, 23, 3,4)
x=int(input())
for i in range(0, len(s)):
    if s[i]==x:
        print("Index= ", (i+1))
        break
