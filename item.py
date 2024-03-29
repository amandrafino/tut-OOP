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

    # decorator changes this method to a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )


    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"




