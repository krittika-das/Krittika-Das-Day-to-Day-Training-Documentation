a=input("Enter a string: ")
s=""
for i in a:
    if i not in s:
        c=0
        for x in a:
            if x==i:
                c+=1
        print(i, " = " , c)
        s+=i