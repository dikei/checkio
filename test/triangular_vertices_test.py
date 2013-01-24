from problems.triangular_vertices import checkio
from test.base_test import TestRoot

class TestTriangularVertices(TestRoot):

    def test_generator(self):
        cases = (
            (3, [1, 2, 3]),
            (0, [11, 13, 29, 31]),
            (4, [26, 11, 13, 24]),
            (6, [4, 5, 9, 13, 12, 7]),
            (0, [1, 2 ,3 , 4, 5]),
            (0, [47]),
            (0, [11, 13, 23, 25]),
            (0, [2, 3, 4, 6, 8, 5])
        )
        for case in cases:
            yield self.check_equals, case[0], checkio(case[1])
