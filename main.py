class Item(object):
    # constructor
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} must be greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greate than zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("phone", 100, 5)
print(f"{item1.name}: ${item1.price}")
print(item1.calculate_total_price())

print("\n") # line break

item2 = Item("laptop", 1000, 2)
print(f"{item2.name}: ${item2.price}")
print(item2.calculate_total_price())

item2.has_numpad = False


"""# {{{
When you invoke a method on an instance in Python, the Py runtime
automatically passes the instance itself as the first argument
to the method. This argument is named (self) in the method's
parameter list.
This allows the methods to access and manipulate the instance's
attributes and other methods, facilitating Object Oriented 
behaviors and interactions within the class.
"""# }}}
