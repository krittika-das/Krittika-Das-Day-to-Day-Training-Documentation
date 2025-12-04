class User:
    def __init__(self, name):
        self.name = name
    def delete_user(self, user):
        print("Normal user not allowed to be deleted")

class Admin(User):
    def delete_user(self, user):
        print("Admin has deleted user: ", user.name)

u1=User("Rohan")
a1=Admin("Admin1")
a1.delete_user(u1)
u1.delete_user(a1)