from nose.tools import eq_

__author__ = 'dikei'

class TestRoot(object):

    def check_equals(self, expected, actual):
        eq_(expected, actual)
