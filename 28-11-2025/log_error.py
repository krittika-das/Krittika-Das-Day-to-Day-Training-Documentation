from datetime import datetime

def log_error(messages):
    timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    x=f"Error logged: at {timestamp}"
    with open("error_log.txt", "a") as f:
        f.write(f"{x}\n")

x=input("Enter your message if error: ")
log_error(x)

