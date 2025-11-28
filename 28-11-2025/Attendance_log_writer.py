from datetime import datetime
x=int(input("What is the total strength of the class? "))
for i in range(x):
    name=input("Enter the name:")
    attendance=input("Enter the attendance:")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("attendance.log", "a") as f:
        f.write("Name: "+name+","+"Timestamp:" + timestamp +"Attendance: "+ attendance+"\n")