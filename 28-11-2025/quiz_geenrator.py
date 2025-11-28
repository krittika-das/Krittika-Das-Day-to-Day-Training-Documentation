def generator(question):
    with open("quiz_geenrator.txt", "a") as a:
        quest=question+"\n"+"Answer: \n"
        a.write(quest)

x=input("Enter the question ")
generator(x)