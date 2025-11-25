numbers=(33, 20, 30, 60, 50)
maxi=numbers[0]
mini=numbers[0]
for i in numbers:
    if i>maxi:
        maxi=i
    elif i<mini:
        mini=i
print(maxi)
print(mini)