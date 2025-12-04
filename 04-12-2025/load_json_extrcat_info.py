import json
with open ("products.json", "r") as f:
    products = json.load(f)

for p in products:
    p["price"] = p["price"] - (p["price"]*0.10)

with open ("products.json", "w") as f:
    json.dump(products, f, indent=4)