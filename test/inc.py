# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_inc(unittest.TestCase):
    def test_increments_its_argument(self):
        eq(self, R.inc(-1), 0)
        eq(self, R.inc(0), 1)
        eq(self, R.inc(1), 2)
        eq(self, R.inc(12.34), 13.34)
        eq(self, R.inc(-float('inf')), -float('inf'))
        eq(self, R.inc(float('inf')), float('inf'))


if __name__ == '__main__':
    unittest.main()
