class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid")

    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance

acc=BankAccount("John",10000)
acc.deposit(100)
print(acc.get_balance())

acc.withdraw(200)
print(acc.get_balance())

acc.__balance=0
print(acc.get_balance())
print(dir(acc))
