# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_of(unittest.TestCase):
    def test_returns_its_argument_as_an_Array(self):
        eq(self, R.of(100), [100])
        eq(self, R.of([100]), [[100]])
        eq(self, R.of(None), [None])
        eq(self, R.of(None), [None])
        eq(self, R.of([]), [[]])


if __name__ == '__main__':
    unittest.main()
