def generate_letter(name, course):
    content=f"Welcome {name}! to the {course}!. We are very delighted to have you and expect a very healthy collaboration journey throughout!!!"
    c=f"certificate_{name}.txt"
    with open(c, "w") as f:
        f.write(content)

x=int(input("How many names are there?"))
for i in range(x):
    name=input("Enter your name")
    course=input("Enter your course")
    generate_letter(name, course)