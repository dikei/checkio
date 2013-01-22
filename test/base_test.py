from nose.tools import eq_, ok_

class TestRoot(object):

    def check_equals(self, expected, actual):
        eq_(expected, actual)

    def check_true(self, expression):
        ok_(expression)
