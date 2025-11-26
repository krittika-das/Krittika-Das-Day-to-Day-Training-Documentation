class bank_account():
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def deposit(self, amt):
        self.balance+=amt

    def withdraw(self, amt):
        if amt<self.balance:
            self.balance-=amt
        else:
            print("Insufficient funds")

    def get_balance(self):
        print("Name: ",self.name, " Current Holdings: ", self.balance)

b1=bank_account("Krittika", 20000)
x=int(input("Enter amount to be added:"))
b1.deposit(x)
y=int(input("Enter amount to be withdrawn:"))
b1.withdraw(y)
b1.get_balance()