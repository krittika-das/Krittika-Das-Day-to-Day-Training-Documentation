import csv

data=[
    ["item", "quantity", "price"],
    ["Pen", 10, 5],
    ["Notebook", 3, 40], ["Eraser", 5, 3]]

with open("trolly.csv", "w", newline="") as f:
    w=csv.writer(f)
    w.writerows(data)

