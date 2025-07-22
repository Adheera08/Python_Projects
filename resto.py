#Define the menu of restaurant
menu = {
   'Pizza':40,
   'Pasta':50,
   'Burger':60,
   'Coffee':70
}

#Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: 40")
print("Pasta: 50")
print("Burger: 60")
print("Coffee: 70")

order_total = 0
#70 + 40 = 110

item_1 = input("Enter the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print("Ordered item {item_1} is not available yet!")
another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of item {item_2} you want to add")
    if item_2 in menu:
        order_total += menu[item_2] #0 +70
        print(f"Item {item_2} has been added to order")
        
    else:
        print("Ordered item {item_2} is not available yet!")

print(f"Total bill {order_total}")