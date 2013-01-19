from nose.tools import eq_

class TestRoot(object):

    def check_equals(self, expected, actual):
        eq_(expected, actual)
