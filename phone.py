from item import Item

# inheritance / child class
class Phone(Item):
    # constructor
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        # Run validations
        assert price >= 0, f"Price {price} must be greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} must be greate than zero!"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be greater than zero!"

#phone1 = Phone("JscPhonev10", 500, 5, 1)
#print(phone1.calculate_total_price())
#phone2 = Phone("JscPhonev20", 700, 5, 1)


