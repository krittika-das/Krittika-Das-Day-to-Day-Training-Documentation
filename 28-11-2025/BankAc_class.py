class banca:
    def __init__(self,amt):
        self.amt=amt
    def deposit(self,a):
        self.amt=self.amt-a
        return self.amt
    def withdraw(self,b):
        self.amt=self.amt+b
        return self.amt

x=banca(5000)
print("New amt after withdraw: ", x.deposit(500))
print("New amt after withdraw: ", x.withdraw(1239))