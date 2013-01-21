from problems.cipher_map import checkio
from test.base_test import TestRoot

class TestCipherMap(TestRoot):

    def test_generator(self):
        cases = (
            ('icantforgetiddqd', [
                [
                    'X...',
                    '..X.',
                    'X..X',
                    '....'
                ],
                [
                    'itdf',
                    'gdce',
                    'aton',
                    'qrdi'
                ]
            ]),
            ('rxqrwsfzxqxzhczy', [
                [
                    '....',
                    'X..X',
                    '.X..',
                    '...X'
                ],
                [
                    'xhwc',
                    'rsqx',
                    'xqzz',
                    'fyzr'
                ]
            ])
        )
        for case in cases:
            yield self.check_equals, case[0], checkio(case[1])
