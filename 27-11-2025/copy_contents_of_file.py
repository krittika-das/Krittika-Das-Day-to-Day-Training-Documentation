src="notes.txt"

with open (src, "r") as f:
    fc=f.read()

with open("destination.txt", "w") as f:
    f.write(fc)

