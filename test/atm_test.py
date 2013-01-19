from test.base_test import TestRoot
from problems.atm import checkio

class TestAtm(TestRoot):

    def test_generator(self):
        cases = (
            (57, [120, [10, 20, 30]]),
            (109, [120, [200, 10]]),
            (109, [120, [3, 10]]),
            (120, [120, [200, 119]]),
            (56, [120, [120, 10, 122, 2, 10, 10, 30, 1]])
        )
        for index, case in enumerate(cases):
            yield self.check_equals, case[0], checkio(case[1])
