import csv
try:
    x=open("test.txt", "r", newline='')
    print(x.read())
    if not x.endswith(".csv"):
        raise ValueError("Error")
except FileNotFoundError:
    print("File not found")