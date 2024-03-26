#!/usr/local/bin/python3

# Class definition for an item with name, price, and quantity attributes
class Item:
    def  __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price ({price}) must be greater than zero."
        assert quantity >= 0

        # Assign to self object
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

class Memory(Item):
    def __init__(self, name, price, quantity, memory):
        super().__init__(name, price, quantity)
        self.memory= memory


item2 = Memory("iPhone 14", 1000, 3, True )
print(item2.memory)
print (f"This iPhone: ({item2.name}) comes with 2 gigs of memory")

