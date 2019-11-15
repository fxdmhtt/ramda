# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_complement(unittest.TestCase):
    def test_creates_boolean_returning_function_that_reverses_another(self):
        even = lambda x: x % 2 == 0
        f = R.complement(even)
        eq(self, f(8), False)
        eq(self, f(13), True)

    def test_accepts_a_function_that_take_multiple_parameters(self):
        between = lambda a, b, c: a < b and b < c
        f = R.complement(between)
        eq(self, f(4, 5, 11), False)
        eq(self, f(12, 2, 6), True)

    # def test_accepts_fantasy_land_functors(self):
    #     Just = S.Just
    #     Nothing = S.Nothing
    #     eq(self, R.complement(Just(True)), Just(False))
    #     eq(self, R.complement(Just(False)), Just(True))
    #     eq(self, R.complement(Nothing()), Nothing())


if __name__ == '__main__':
    unittest.main()
