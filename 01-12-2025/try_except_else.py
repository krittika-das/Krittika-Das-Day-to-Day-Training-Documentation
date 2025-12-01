try:
    n=int(input("Enter a number: "))
    x=50/n
except ZeroDivisionError:
    print("Division by zero is no possible")
else:
    print("Successful!", print(x))
