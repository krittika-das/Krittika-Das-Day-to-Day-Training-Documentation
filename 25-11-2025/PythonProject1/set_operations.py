a={1, 2, 3, 4}
b={3, 4, 5, 6}
print(a | b) #union
print(a & b) #intersection
print(a - b) #set difference
print(a ^ b) #symmetric difference

#memebership operator
s={10, 20, 30}
print(20 in s)

#traversal
for item in {4, 8, 12}:
    print(item)

#unique elements
nums=[1,2,3,4,5]
unique=list(set(nums))
print(unique)

