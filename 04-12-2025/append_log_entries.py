from datetime import datetime
with open('logmessage.txt', 'a') as f:
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{time} - logged Now \n")

