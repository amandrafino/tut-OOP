import csv

class Item(object):
    pay_rate = 0.8 # entire Item namespace
    all = []
    # constructor
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations
        assert price >= 0, f"Price {price} must be greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greate than zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity


    def apply_discount(self):
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)




    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#print(Item.all)
#for instance in Item.all:
#    print(instance.name)

Item.instantiate_from_csv()

# namespace (class and instance){{{
#print(f"\nObject in the Item namespace: {Item.__dict__}\n")
#print(f"Objects in the item1 namespace: {item1.__dict__}")# }}}


"""# {{{
When you invoke a method on an instance in Python, the Py runtime
automatically passes the instance itself as the first argument
to the method. This argument is named (self) in the method's
parameter list.
This allows the methods to access and manipulate the instance's
attributes and other methods, facilitating Object Oriented 
behaviors and interactions within the class.
"""# }}}
