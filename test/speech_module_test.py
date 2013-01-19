from test.base_test import TestRoot
from problems.speech_module import checkio

class TestSpeechModule(TestRoot):

    def test_generator(self):
        cases = (
            ('four', 4),
            ('one hundred forty three', 143),
            ('twelve', 12),
            ('one hundred one', 101),
            ('two hundred twelve', 212),
            ('forty', 40)
        )
        for index, case in enumerate(cases):
            yield self.check_equals, case[0], checkio(case[1])
