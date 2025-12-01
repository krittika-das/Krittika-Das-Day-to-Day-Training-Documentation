try:
    n=int(input("Enter a number"))
    print(n/0)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Not possible")