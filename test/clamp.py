# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_clamp(unittest.TestCase):
    def test_clamps_to_the_lower_bound(self):
        eq(self, R.clamp(1, 10, 0), 1)
        eq(self, R.clamp(3, 12, 1), 3)
        eq(self, R.clamp(-15, 3, -100), -15)

    def test_clamps_to_the_upper_bound(self):
        eq(self, R.clamp(1, 10, 20), 10)
        eq(self, R.clamp(3, 12, 23), 12)
        eq(self, R.clamp(-15, 3, 16), 3)

    def test_leaves_it_alone_when_within_the_bound(self):
        eq(self, R.clamp(1, 10, 4), 4)
        eq(self, R.clamp(3, 12, 6), 6)
        eq(self, R.clamp(-15, 3, 0), 0)

    def test_works_with_letters_as_well(self):
        eq(self, R.clamp('d', 'n', 'f'), 'f')
        eq(self, R.clamp('d', 'n', 'a'), 'd')
        eq(self, R.clamp('d', 'n', 'q'), 'n')


if __name__ == '__main__':
    unittest.main()
