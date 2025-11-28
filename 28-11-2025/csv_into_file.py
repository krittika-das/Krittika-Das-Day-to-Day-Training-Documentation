import csv


with open("trolly.csv", "r") as f:
    reader=csv.DictReader(f)
    inv="Invoice \n"
    inv += "Item \t Quantity \t Price \t Total \n"
    inv += "\n"
    for row in reader:
        item=row["item"]
        qty=float(row["quantity"])
        price=float(row["price"])
        amt=qty*price
        total=amt+price
        inv+=f"{item} \t {qty} \t {price}"
    inv+="\n"
    inv+=f"Total : {total}"

with open("invoice.txt","w") as f:
    f.write(inv)