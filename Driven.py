#Related to TestDriven.py
class Product:
    def __init__(self, quantity = 0, price = 0.0):
        self.quantity = quantity
        self.price = price

    def purchase(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return quantity * self.price
        raise ValueError("Not enough product")
