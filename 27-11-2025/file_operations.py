with open("sample.txt", "w") as f:
    f.write("Hello, I am Krittika. \n")
    f.write("Okay.")

with open("sample.txt", "r") as f:
    content = f.read()
    print(content)