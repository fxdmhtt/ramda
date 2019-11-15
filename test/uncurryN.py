# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_uncurryN(unittest.TestCase):
    def setUp(self):
        self.a2 = lambda a: \
            lambda b: \
                a + b

        self.a3 = lambda a: \
            lambda b: \
                lambda c: \
                    a + b + c

        self.a3b = lambda a: \
            lambda b: \
                lambda c, *arguments: \
                    a + b + c + (len(arguments) > 0 and arguments[0] or 0) + (len(arguments) > 1 and arguments[1] or 0)

        self.a4 = lambda a: \
            lambda b: \
                lambda c: \
                    lambda d: \
                        a + b + c + d

    def test_accepts_an_arity(self):
        uncurried = R.uncurryN(3, self.a3)
        eq(self, uncurried(1, 2, 3), 6)

    def test_returns_a_function_of_the_specified_arity(self):
        eq(self, R.uncurryN(2, self.a2).length, 2)
        eq(self, R.uncurryN(3, self.a3).length, 3)
        eq(self, R.uncurryN(4, self.a4).length, 4)

    def test_forwards_extra_arguments(self):
        g = R.uncurryN(3, self.a3b)

        eq(self, g(1, 2, 3), 6)
        eq(self, g(1, 2, 3, 4), 10)
        eq(self, g(1, 2, 3, 4, 5), 15)

    def test_works_with_ordinary_uncurried_functions(self):
        eq(self, R.uncurryN(2, lambda a, b: a + b)(10, 20), 30)
        eq(self, R.uncurryN(3, lambda a, b, c: a + b + c)(10, 20, 30), 60)

    def test_works_with_ramda_curried_functions(self):
        eq(self, R.uncurryN(2, R.add)(10, 20), 30)

    def test_returns_a_function_that_supports_placeholder(self):
        g = R.uncurryN(3, self.a3)
        _ = R.__

        eq(self, g(1)(2)(3), 6)
        eq(self, g(1)(2, 3), 6)
        eq(self, g(1, 2)(3), 6)
        eq(self, g(1, 2, 3), 6)

        eq(self, g(_, 2, 3)(1), 6)
        eq(self, g(1, _, 3)(2), 6)
        eq(self, g(1, 2, _)(3), 6)

        eq(self, g(1, _, _)(2)(3), 6)
        eq(self, g(_, 2, _)(1)(3), 6)
        eq(self, g(_, _, 3)(1)(2), 6)

        eq(self, g(1, _, _)(2, 3), 6)
        eq(self, g(_, 2, _)(1, 3), 6)
        eq(self, g(_, _, 3)(1, 2), 6)

        eq(self, g(1, _, _)(_, 3)(2), 6)
        eq(self, g(_, 2, _)(_, 3)(1), 6)
        eq(self, g(_, _, 3)(_, 2)(1), 6)

        eq(self, g(_, _, _)(_, _)(_)(1, 2, 3), 6)
        eq(self, g(_, _, _)(1, _, _)(_, _)(2, _)(_)(3), 6)


if __name__ == '__main__':
    unittest.main()
