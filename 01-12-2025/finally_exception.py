
try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing operation completed.") #use this block for memory managemnet in huge applications
