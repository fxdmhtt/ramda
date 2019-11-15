# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_dec(unittest.TestCase):
    def test_decrements_its_argument(self):
        eq(self, R.dec(-1), -2)
        eq(self, R.dec(0), -1)
        eq(self, R.dec(1), 0)
        eq(self, R.dec(12.34), 11.34)
        eq(self, R.dec(-float('inf')), -float('inf'))
        eq(self, R.dec(float('inf')), float('inf'))


if __name__ == '__main__':
    unittest.main()
