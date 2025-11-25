s={2, 4, 6, 8, 10}

target=int(input("Enter the target sum: "))

pairs=set()

for  x in s:
    y=target-x
    if y in s:
        pairs.add(tuple(sorted((x,y))))

print(pairs)