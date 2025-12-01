try:
    a=int(input())
    b=int(input())
    print(a+b)
    print(a/b)
    print(a-b)
    print(a*b)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid entry")