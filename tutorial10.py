class price:
    def __init__(self, order1, order2, order3, price = 0.0):
        self.order1 = order1
        self.order2 = order2
        self.order3 = order3
        self.price = price

    def purchase(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return quantity * self.price
        raise ValueError("Not enough product")