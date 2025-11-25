s={"A": 85, "B": 92, "C": 78, "D": 92}
k=s.get("A")
for i in s.values():
    if i>k:
        k=i
print(k)