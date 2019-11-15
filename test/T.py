# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_T(unittest.TestCase):
    def test_always_returns_True(self):
        eq(self, R.T(), True)
        eq(self, R.T(10), True)
        eq(self, R.T(True), True)


if __name__ == '__main__':
    unittest.main()
