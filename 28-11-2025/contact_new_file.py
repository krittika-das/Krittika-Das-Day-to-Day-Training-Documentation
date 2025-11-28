import csv

with open("contacts.csv",'r') as csvfile:
    x=csv.DictReader(csvfile)
    with open("contacts.txt",'a') as out:
        for row in x:
            line=f"Name:  {row['Name']} | Phone: {row['Phone']} \n"
            out.write(line)