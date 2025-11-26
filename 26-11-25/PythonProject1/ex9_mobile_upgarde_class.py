class Mobile:
    def __init__(self, name, brand, model, storage):
        self.name = name
        self.brand = brand
        self.model = model
        self.storage = storage
    def upgrade(self, sto):
        if self.storage < sto:
            self.storage = sto
        return self.storage

x=Mobile("Ronald", "Moto", "XE200", 15000)
x.upgrade(2000)
print(x.storage)
