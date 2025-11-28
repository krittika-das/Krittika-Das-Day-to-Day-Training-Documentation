stootal=0
inv=""
for i in range(3):
    name=input("Enter name of the product: ")
    quantity=int(input("Enter quantity: "))
    price=int(input("Enter price: "))
    inv=f"Name: {name}\nQuantity: {quantity}\nPrice: {price} \n"
    total=quantity*price
    inv+=f"Total price: {total} \n"
    stootal+=total
inv+=f"Subtotal: {stootal} \n"
with open("order_summary.txt","a") as f:
    f.write(inv)


