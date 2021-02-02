from tutorial10 import *
import unittest

class calculateTestCase(unittest.TestCase):
    def setUp(self):
        self.price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}

    def calculate_price(price, order1, order2, order3):    
        return sum(order1.values)
        return sum(order2.values)
        return sum(order3.values)

    def orderOne(self):
        
        order1 = {'book': 10}
        self.assertAlmostEqual(self.price(95 == calculate_price(price, order1)))

    def orderTwo(self):
        price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}
        order2 = {'book': 1, 'magazine': 3}
        self.assertAlmostEqual(self.price(26.5 == calculate_price(price, order2)))
   
    def orderThree(self):
        price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}
        order3 = {'magazine': 5, 'book': 10}
        self.assertAlmostEqual(self.price(114.75 == calculate_price(price, order3)))
    
    


if __name__ == "__main__":
    unittest.main()

print("Done")