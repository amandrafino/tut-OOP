#!/usr/local/bin/python3

# Class definition for an item with name, price, and quantity attributes
class Item:
    def  __init__(self, name, price, quantity=0):
        # Comment out or remove the print statement for production
        # print(f"An instance has been created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # Method to calculate total price using the item's price and quantity
    def calculate_total_price(self):
        return self.price * self.quantity

# Instantiate two items
item1 = Item("iPhoneSE", 100, 5)
item2 = Item("iPhone 14", 1000, 3)


# Demonstrating the use of attributes and methods
print(item1.name, item1.calculate_total_price())
print(item2.name, item2.calculate_total_price())


