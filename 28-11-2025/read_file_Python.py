with open("pythonfile.txt","r") as file:
    c=0
    content=file.readlines()
    for i in content:
        if "Python" in i:
            c=c+1
    print(c, " lines.")