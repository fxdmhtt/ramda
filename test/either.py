# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_either(unittest.TestCase):
    def test_combines_two_boolean_returning_functions_into_one(self):
        even = lambda x: x % 2 == 0
        gt10 = lambda x: x > 10
        f = R.either(even, gt10)
        eq(self, f(8), True)
        eq(self, f(13), True)
        eq(self, f(7), False)

    def test_accepts_functions_that_take_multiple_parameters(self):
        between = lambda a, b, c: a < b and b < c
        total20 = lambda a, b, c: a + b + c == 20
        f = R.either(between, total20)
        eq(self, f(4, 5, 8), True)
        eq(self, f(12, 2, 6), True)
        eq(self, f(7, 5, 1), False)

    def test_does_not_evaluate_the_second_expression_if_the_first_one_is_True(self):
        T = lambda *_: True
        def Z(*_):
            nonlocal effect
            effect = 'Z got evaluated'
        effect = 'not evaluated'
        R.either(T, Z)()
        eq(self, effect, 'not evaluated')

    # def test_accepts_fantasy_land_applicative_functors(self):
    #     Just = S.Just
    #     Nothing = S.Nothing
    #     eq(self, R.either(Just(True), Just(True)), Just(True))
    #     eq(self, R.either(Just(True), Just(False)), Just(True))
    #     eq(self, R.either(Just(False), Just(False)), Just(False))
    #     eq(self, R.either(Just(True), Nothing()), Nothing())
    #     eq(self, R.either(Nothing(), Just(False)), Nothing())
    #     eq(self, R.either(Nothing(), Nothing()), Nothing())


if __name__ == '__main__':
    unittest.main()
