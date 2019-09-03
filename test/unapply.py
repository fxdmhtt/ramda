# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest
import random
import math

class Test_unapply(unittest.TestCase):
    def test_returns_a_function_which_is_always_passed_one_argument(self):
        fn = R.unapply(lambda *arguments: len(arguments))
        eq(self, fn(), 1)
        eq(self, fn('x'), 1)
        eq(self, fn('x', 'y'), 1)
        eq(self, fn('x', 'y', 'z'), 1)

    def test_forwards_arguments_to_decorated_function_as_an_array(self):
        fn = R.unapply(lambda xs: '[' + str(list(xs))[1:-1].replace(' ', '') + ']')
        eq(self, fn(), '[]')
        eq(self, fn(2), '[2]')
        eq(self, fn(2, 4), '[2,4]')
        eq(self, fn(2, 4, 6), '[2,4,6]')

    def test_returns_a_function_with_length_0(self):
        fn = R.unapply(R.identity)
        eq(self, fn.length, 0)

    def test_is_the_inverse_of_apply(self):
        rand = lambda *_: \
            math.floor(200 * random.random()) - 100

        f = max
        g = R.unapply(R.apply(f))
        n = 1
        while n <= 100:
            a = rand();b = rand();c = rand();d = rand();e = rand()
            eq(self, f(a, b, c, d, e), g(a, b, c, d, e))
            n += 1

        f = lambda xs: '[' + str(list(xs))[1:-1].replace(' ', '') + ']'
        g = R.apply(R.unapply(f))
        n = 1
        while n <= 100:
            a = rand();b = rand();c = rand();d = rand();e = rand()
            eq(self, f([a, b, c, d, e]), g([a, b, c, d, e]))
            n += 1


if __name__ == '__main__':
    unittest.main()
