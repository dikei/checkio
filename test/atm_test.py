from test.testgen import test_generator

__author__ = 'dikei'

import unittest
from problems.atm import checkio


class AtmTest(unittest.TestCase):
    pass

def gen_test():
    cases = (
        (57, [120, [10, 20, 30]]),
        (109, [120, [200, 10]]),
        (109, [120, [3, 10]]),
        (120, [120, [200, 119]]),
        (56, [120, [120, 10, 122, 2, 10, 10, 30, 1]])
    )
    for index, case in enumerate(cases):
        test_name = "test_atm_{}".format(index)
        test_func = test_generator(case[0], case[1], checkio)
        setattr(AtmTest, test_name, test_func)
