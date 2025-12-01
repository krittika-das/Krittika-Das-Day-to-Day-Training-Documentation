try:
    file=open("x.txt","r")
    print(file.read())
    file.write("Hello World")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")