__author__ = 'dikei'

import unittest
from test import atm_test, spaceship_purchase_test

def test_atm():
    """
    Test for atm problem
    """
    atm_test.gen_test()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(atm_test.AtmTest)
    unittest.TextTestRunner().run(suite)

def test_spaceship_purchase():
    """
    Test for spaceship purchase problem
    """
    spaceship_purchase_test.gen_test()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(spaceship_purchase_test.SpaceshipPurchaseTest)
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    test_atm()
    test_spaceship_purchase()
