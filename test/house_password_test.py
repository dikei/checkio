from problems.house_password import checkio
from test.base_test import TestRoot

class TestHousePassword(TestRoot):

    def test_generator(self):
        cases = (
            (False, 'A1213pokl'),
            (True, 'bAse730onE'),
            (False, 'asasasasasasasaas'),
            (False, 'QWERTYqwerty'),
            (False, '123456123456'),
            (True, 'QwErTy911poqqqq')
        )
        for case in cases:
            yield self.check_equals, case[0], checkio(case[1])
