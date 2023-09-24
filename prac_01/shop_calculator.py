number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
item_number = 0
for i in range(number_of_items):
    item_number += 1
    price_of_item = float(input(f"Price of item {item_number}: $"))
    total_price += price_of_item
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
