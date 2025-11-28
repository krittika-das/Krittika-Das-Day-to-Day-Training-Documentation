def writeman(message):
    with open("write_5_lines.txt", "a") as file:
        file.write(message)
        file.write("\n")

message=input("Enter your message: ")
writeman(message)
