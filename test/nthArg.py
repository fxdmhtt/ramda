# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_nthArg(unittest.TestCase):
    def test_returns_a_function_which_returns_its_nth_argument(self):
        eq(self, R.nthArg(0)('foo', 'bar'), 'foo')
        eq(self, R.nthArg(1)('foo', 'bar'), 'bar')

    def test_accepts_negative_offsets(self):
        eq(self, R.nthArg(-1)('foo', 'bar'), 'bar')
        eq(self, R.nthArg(-2)('foo', 'bar'), 'foo')
        eq(self, R.nthArg(-3)('foo', 'bar'), None)

    def test_returns_a_function_with_length_n_1_when_n_0(self):
        eq(self, R.nthArg(0).length, 1)
        eq(self, R.nthArg(1).length, 2)
        eq(self, R.nthArg(2).length, 3)
        eq(self, R.nthArg(3).length, 4)

    def test_returns_a_function_with_length_1_when_n_0(self):
        eq(self, R.nthArg(-1).length, 1)
        eq(self, R.nthArg(-2).length, 1)
        eq(self, R.nthArg(-3).length, 1)

    def test_returns_a_curried_function(self):
        eq(self, R.nthArg(1)('foo', 'bar'), R.nthArg(1)('foo')('bar'))
        eq(self, R.nthArg(2)('foo', 'bar', 'baz'), R.nthArg(2)('foo')('bar')('baz'))


if __name__ == '__main__':
    unittest.main()
