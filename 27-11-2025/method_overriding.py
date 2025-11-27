class Notification:
    def send(self, mesage):
        print("Sending sms: ", mesage)

class Email(Notification):
    def send(self, mesage):
        print("Sending email: ", mesage)

class SMS(Notification):
    def send(self, mesage):
        print("Sending sms: ", mesage)

x=Email()
x.send("Hello")

y=SMS()
y.send("This is to inform you")
