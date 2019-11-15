# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_o(unittest.TestCase):
    def test_is_not_a_variadic_function(self):
        self.assertTrue(callable(R.o))
        eq(self, R.o.length, 3)

    def test_is_a_curried_function(self):
        eq(self, R.o(R.add(1), R.multiply(2), 10), R.o(R.add(1))(R.multiply(2))(10))

    def test_performs_right_to_left_function_composition(self):
        #    f :: Number -> ([Number] -> [Number])
        f = R.o(R.map, R.multiply)

        eq(self, f.length, 1)
        eq(self, f(10)([1, 2, 3]), [10, 20, 30])


if __name__ == '__main__':
    unittest.main()
