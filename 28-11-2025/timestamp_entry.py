from datetime import datetime

def write_logs(message):
    with open('log.txt','a') as f:
        k=f"{message} logged at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
        f.write(k)

message=input("Enter your message: ")
write_logs(message)