s={"Wheat": 120, "Sourdough": 90, "Flour": 200, "Banana": 89}
m=s.copy()
for k,v in s.items():
    if v<100:
        m.pop(k)
print(m)