from problems.speech_module import checkio
from test.testgen import test_generator

__author__ = 'dikei'

import unittest


class SpeechModuleTest(unittest.TestCase):
    pass

def gen_test():
    cases = (
        ('four', 4),
        ('one hundred forty three', 143),
        ('twelve', 12),
        ('one hundred one', 101),
        ('two hundred twelve', 212),
        ('forty', 40)
    )
    for index, case in enumerate(cases):
        test_name = "test_speech_{}".format(index)
        test_func = test_generator(case[0], case[1], checkio)
        setattr(SpeechModuleTest, test_name, test_func)
