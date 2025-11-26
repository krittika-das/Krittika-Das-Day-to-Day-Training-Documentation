class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amt):
        self.balance += amt
        return self.balance
    def withdraw(self, amt):
        self.balance -= amt
        return self.balance
    def display_logs(self):
        print(self.name)
        print(self.balance)

x=Bank_account("Krittika", 15698)
x.deposit(5000)
x.withdraw(500)
x.display_logs()