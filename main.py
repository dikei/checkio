__author__ = 'dikei'

import unittest
from test import atm_test

def test_atm():
    """
    Test for atm problem
    """
    atm_test.gen_atm_test()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(atm_test.AtmTest)
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    test_atm()
