# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_juxt(unittest.TestCase):
    def setUp(self):
        self.hello = lambda *_: 'hello'
        self.bye = lambda *_: 'bye'

    def test_works_with_no_functions_and_no_values(self):
        eq(self, R.juxt([])(), ())

    def test_works_with_no_functions_and_some_values(self):
        eq(self, R.juxt([])(2, 3), ())

    def test_works_with_1_function_and_no_values(self):
        eq(self, R.juxt([self.hello])(), ('hello',))

    def test_works_with_1_function_and_1_value(self):
        eq(self, R.juxt([R.add(3)])(2), (5,))

    def test_works_with_1_function_and_some_values(self):
        eq(self, R.juxt([R.multiply])(2, 3), (6,))

    def test_works_with_some_functions_and_no_values(self):
        eq(self, R.juxt([self.hello, self.bye])(), ('hello', 'bye'))

    def test_works_with_some_functions_and_1_value(self):
        eq(self, R.juxt([R.multiply(2), R.add(3)])(2), (4, 5))

    def test_works_with_some_functions_and_some_values(self):
        eq(self, R.juxt([R.add, R.multiply])(2, 3), (5, 6))

    def test_retains_the_highest_arity(self):
        f = R.juxt([R.nAry(1, R.T), R.nAry(3, R.T), R.nAry(2, R.T)])
        eq(self, f.length, 3)

    def test_returns_a_curried_function(self):
        eq(self, R.juxt([R.multiply, R.add])(2)(3), (6, 5))


if __name__ == '__main__':
    unittest.main()
