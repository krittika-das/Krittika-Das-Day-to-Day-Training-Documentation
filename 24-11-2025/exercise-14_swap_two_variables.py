#Exercise 14: swap two variables without using a third varible
a=int(input("Enter a: "))
b=int(input("Enter b: "))
a=a+b
b=a-b
a=a-b
print("After swap -> a= ", a, " , b= ", b)