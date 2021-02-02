#Related to Driven.py and you run this program only
from Driven import *
import unittest

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.p = Product(10, 2.50) #there are 10 products available and each costs 2.50

    def testPurchaseSuccess(self):
        #p = Product(10, 2.50) #We don't need this line of code with the built-in setUp() function, called test fixture
        self.assertAlmostEqual(self.p.purchase(9), 22.5, 2) #but we need to add self. in front of p.purchase()

    def testPurchaseExact(self):
        #p = Product(10, 2.50)
        self.assertAlmostEqual(self.p.purchase(10), 25, 2)
    
    def testPurchaseFailure(self):
        #p = Product(10, 2.50)
        with self.assertRaises(ValueError):
            self.p.purchase(11)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ProductTestCase("testPurchaseSuccess"))
    suite.addTest(ProductTestCase("testPurchaseExact"))
    suite.addTest(ProductTestCase("testPurchaseFailure"))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())