import math
import re
from problems.anything import checkio
from test.base_test import TestRoot

class TestAnything(TestRoot):

    def test_generator(self):
        cases = (
            (checkio('Hello') < 'World'),
            (checkio(80) > 81),
            (checkio(re) >= re),
            (checkio(re) <= math),
            (checkio({}) != []),
            (checkio(5) == ord)
        )
        for case in cases:
            yield self.check_true, case
