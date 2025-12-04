e={'A': 50000, 'B': 34000, 'C': 78000, 'D': 72900}
kiki=dict()
for k, v in e.items():
    if v >= 60000:
        kiki[k] = v
print(kiki)