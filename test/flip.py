# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_flip(unittest.TestCase):
    def test_returns_a_function_which_inverts_the_first_two_arguments_to_the_supplied_function(self):
        f = lambda a, b, c: a + ' ' + b + ' ' + c
        g = R.flip(f)
        eq(self, f('a', 'b', 'c'), 'a b c')
        eq(self, g('a', 'b', 'c'), 'b a c')

    def test_returns_a_curried_function(self):
        f = lambda a, b, c: a + ' ' + b + ' ' + c
        g = R.flip(f)('a')
        eq(self, g('b', 'c'), 'b a c')

    def test_returns_a_function_with_the_correct_arity(self):
        f2 = lambda a, b:{ a + ' ' + b}
        f3 = lambda a, b, c: a + ' ' + b + ' ' + c
        eq(self, R.flip(f2).length, 2)
        eq(self, R.flip(f3).length, 3)


if __name__ == '__main__':
    unittest.main()
