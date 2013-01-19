from problems.battery_loading import checkio
from test.base_test import TestRoot

class TestBattery(TestRoot):

    def test_generator(self):
        cases = (
            (0, [10, 10]),
            (10, [10]),
            (3, [5, 8, 13, 27, 14]),
            (1, [5, 5, 6, 5]),
            (9, [12, 30, 30, 32, 42, 49]),
            (0, [1, 1, 1, 3])
        )
        for case in cases:
            yield self.check_equals, case[0], checkio(case[1])
