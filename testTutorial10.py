#Related to tutorial10.py and you run this program only
from tutorial10 import *
import unittest

class calculateTestCase(unittest.TestCase):
    def setUp(self):
        self.price = {'book': 10.0, 'magazine': 5.5, 'newspaper': 2.0}

    def testProductsSuccess(self, order1):
        self.order1 = {'book': 10}
        self.assertAlmostEqual(self.price.purchase(5))       
    
    def testProductExact(self):
        self.assertAlmostEqual(self.price.purchase(10), 26.5, 2)

    def testProductFailure(self):
        self.assertAlmostEqual(self.price.purchase(15), 114.75, 2)

    def calculate_price(price, order):   
        

    def purchase():
        try:
            self.order1 = {'book': 10}
            self.order2 = {'book': 1, 'magazine': 3}
            self.order3 = {'magazine': 5, 'book': 10}
            assert(95 == calculate_price(price, order1))
            assert(26.5 == calculate_price(price, order2))
            assert(114.75 == calculate_price(price, order3))
        finally:
            print("all done")


def suite():
    suite = unittest.TestSuite()
    suite.addTest(calculateTestCase("testPurchaseSuccess"))
    suite.addTest(calculateTestCase("testPurchaseExact"))
    suite.addTest(calculateTestCase("testPurchaseFailure"))
    return suite

if __name__ == "__main__":
    suite = unittest.TestSuite()
    unittest.TextTestRunner(verbosity=2).run(suite(10, 5))