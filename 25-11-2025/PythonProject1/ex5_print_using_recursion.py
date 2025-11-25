def print_using_recursion(s):
    try:
        for i in s:
            print_using_recursion(i)
    except TypeError:
        print(s)


z=(10, (20, 30), (40, (50, 60)))
print_using_recursion(z)
