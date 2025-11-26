class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_Item(self, name, price):
        self.items.append((name, price))
        print(name, " added to cart.")

    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(name, " removed from cart.")
                return
            print(name, " not found in cart.")

    def total_cost(self):
        total=0
        for item in self.items:
            total = total + item[1]
        return total

    def apply_discount(self, percent):
        total=self.total_cost()
        discount_amt= total* (percent/100)
        final_price=total-discount_amt
        return final_price

    def display(self):
        if not self.items:
            print("Cart is empty.")
            return
        print("Items in Cart:")
        for name, price in self.items:
            print(name, "-", price)

cart=ShoppingCart()
cart.add_Item("Milkshake", 100)
cart.add_Item("Pizza", 250)
print()
cart.display()
print()

print("Total Cost: ", cart.total_cost())
print()
print("Final Price after 10% discount: ", cart.apply_discount(10))
print()
cart.remove_item("Milkshake")
cart.display()
