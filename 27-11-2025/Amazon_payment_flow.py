class PaymentFlow:
    def __init__(self):
        self.total = 50000
    def check_balance(self, amt):
        if amt > self.total:
            print("Insufficient Funds. Please choose another payment method")
            return False
        return True
    def transaction_flow(self, amt):
        self.total -= amt
    def otp_payment(self, otp):
        print("OTP: ", otp)
    def display(self):
        print("Payment Balance", self.total)

class Paytm(PaymentFlow):
    def display(self):
        print("Paytm Balance", self.total)

class Phoepay(PaymentFlow):
    def display(self):
        print("PhonePe Balance", self.total)

class Gpay(PaymentFlow):
    def display(self):
        print("GPay Balance", self.total)

amz=PaymentFlow()
xi=1
while(xi>0):
    x = input("Choose the payment Application: 1 for Paytm, 2 for Phonepe and 3 for GPay!")
    w = int(input("Choose the amount you want to pay"))
    if amz.check_balance(w) is True:
        amz.transaction_flow(w)
        z=int(input("Enter OTP to proceed"))
        amz.otp_payment(z)
        if x==1:
            d=Paytm()
            print(d.display())
        elif x==2:
            d=Phoepay()
            print(d.display())
        else:
            d=Gpay()
            print(d.display())
        xi=xi-1

