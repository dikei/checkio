from problems.spaceship_purchase import checkio
from test.base_test import TestRoot

__author__ = 'dikei'

import unittest


class TestSpaceshipPurchaseTest(TestRoot):

    def test_generator(self):
        cases = (
            (450, [150, 50, 1000, 100]),
            (700, [500, 300, 700, 100])
        )
        for index, case in enumerate(cases):
            yield self.check_equals, case[0], checkio(case[1])
