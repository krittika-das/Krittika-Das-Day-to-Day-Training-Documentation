s=input("Enter a string")
vow=0
con=0
dig=0
for a in s:
    if a in 'aeiouAEIOU':
        vow+=1
    elif a.isdigit():
        dig+=1
    else:
        con+=1
print("Vowels: ", vow, "Consonents: ", con, "Digits: ", dig)
