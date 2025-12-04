class Payment:
    def process_payment(self):
        print("Processing Payment . . .")

class CreditCard(Payment):
    def process_payment(self):
        print("Processing Credit Card . . .")

class UPI(Payment):
    def process_payment(self):
        print("Processing UPI . . .")

p=CreditCard()
p.process_payment()

u=UPI()
u.process_payment()