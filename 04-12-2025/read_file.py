f="sample.txt"
with open(f, "r") as file:
    text=file.read()

c=len(text)
words=len(text.split())
lines=text.count("\n")+1

print("Characters: ",c)
print("Words: ",words)
print("Lines: ",lines)