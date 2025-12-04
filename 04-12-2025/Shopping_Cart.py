class Shopping_Cart:
    def __init__(self):
        self.items = []
        self.total_items = 0
    def add_item(self, name, price):
        self.items.append(name)
        self.total_items += price
    def remove_items(self, name, price):
        if name in self.items:
            self.items.remove(name)
            self.total_items -= price
    def discount_apply(self, percent):
        self.total_items = self.total_items - (self.total_items * (percent / 100))

c=Shopping_Cart()
c.add_item("Shirt", 1300)
c.add_item("Bag", 2300)
c.discount_apply(10)
print('Total: ', c.total_items)