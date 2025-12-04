with open("sample.txt", "r") as f:
    lines = f.readlines()

mid=len(lines)//2

f=lines[:mid]
s=lines[mid:]

with open("fh.txt", "w") as f11:
    f11.writelines(f)

with open("sh.txt", "w") as s11:
    s11.writelines(s)