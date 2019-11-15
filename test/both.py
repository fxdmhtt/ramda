# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_both(unittest.TestCase):
    def test_combines_two_boolean_returning_functions_into_one(self):
        even = lambda x: x % 2 == 0
        gt10 = lambda x: x > 10
        f = R.both(even, gt10)
        eq(self, f(8), False)
        eq(self, f(13), False)
        eq(self, f(14), True)

    def test_accepts_functions_that_take_multiple_parameters(self):
        between = lambda a, b, c: a < b and b < c
        total20 = lambda a, b, c: a + b + c == 20
        f = R.both(between, total20)
        eq(self, f(4, 5, 11), True)
        eq(self, f(12, 2, 6), False)
        eq(self, f(5, 6, 15), False)

    def test_does_not_evaluate_the_second_expression_if_the_first_one_is_False(self):
        F = lambda: False
        def Z():
            nonlocal effect
            effect = 'Z got evaluated'
        effect = 'not evaluated'
        R.both(F, Z)()
        eq(self, effect, 'not evaluated')

    # def test_accepts_fantasy_land_applicative_functors(self):
    #     Just = S.Just
    #     Nothing = S.Nothing
    #     eq(self, R.both(Just(True), Just(True)), Just(True))
    #     eq(self, R.both(Just(True), Just(False)), Just(False))
    #     eq(self, R.both(Just(True), Nothing()), Nothing())
    #     eq(self, R.both(Nothing(), Just(False)), Nothing())
    #     eq(self, R.both(Nothing(), Nothing()), Nothing())


if __name__ == '__main__':
    unittest.main()
