class Bank_Account:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return Bank_Account(self.balance + other.balance)

a1=Bank_Account(100)
a2=Bank_Account(200)
a3=a1+a2
print(a3.balance)