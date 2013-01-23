from problems.spaceship_landing_strip import checkio
from test.base_test import TestRoot

class TestSpaceshipLandingStrip(TestRoot):

    def test_generator(self):
        cases = (
            (1, ['G']),
            (4, ['GS','GS']),
            (2, ['GT','GG']),
            (9, ['GGTGG','TGGGG','GSSGT','GGGGT','GWGGG','RGTRT','RTGWT','WTWGR'])
        )
        for case in cases:
            yield self.check_equals, case[0], checkio(case[1])
