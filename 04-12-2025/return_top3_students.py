x={'A': 33, 'B': 98, 'C': 87, 'K': 34}
print(sorted(x.items(), key=lambda x: x[1], reverse=True)[:3])