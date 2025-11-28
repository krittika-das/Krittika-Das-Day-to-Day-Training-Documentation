def expense_report_geenrator(name, amount):
    return f"""
            Name: {name},
            Amount to be paid: {amount}"""

i = int(input("How many data do you want?"))
for x in range(i):
    z=input("Enter your name:")
    k=int(input("Enter your amount:"))
    with open("reports.txt", "a") as f:
        f.write(expense_report_geenrator(z, k))