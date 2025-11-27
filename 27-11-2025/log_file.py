from datetime import datetime
m="Application Started"
t=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

entry=f"{t} - {m} \n"

with open("log.txt", "a") as f:
    f.write(entry)

with open("log.txt", "r") as f:
    print(f.read())