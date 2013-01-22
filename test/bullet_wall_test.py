from problems.bullet_wall import checkio
from test.base_test import TestRoot

class TestBulletWall(TestRoot):

    def test_generator(self):
        cases = (
            (True, [[0, 0], [0, 2], [5, 1], [3, 1]]),
            (False, [[0, 0], [0, 2], [3, 1], [5, 1]]),
            (True, [[0, 0], [2, 2], [6, 0], [3, 1]]),
            (False, [[6, 0], [5, 5], [4, 0], [5, 6]]),
            (True, [[0, 0], [1, 1], [3, 3], [2, 2]]),
            (False, [[0, 0], [1, 1], [3, 2], [2, 1]]),
            (True, [[9, 7], [2, 5], [5, 3], [2, 5]]),
            (False, [[0, 0], [1, 1], [2, 2], [3, 3]])
        )
        for case in cases:
            yield self.check_equals, case[0], checkio(case[1])
