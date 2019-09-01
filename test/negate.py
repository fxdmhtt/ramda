# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_negate(unittest.TestCase):
    def test_negates_its_argument(self):
        eq(self, R.negate(-float('nan')), float('nan'))
        eq(self, R.negate(-1), 1)
        eq(self, R.negate(-0), 0)
        eq(self, R.negate(0), -0)
        eq(self, R.negate(1), -1)
        eq(self, R.negate(float('nan')), -float('nan'))


if __name__ == '__main__':
    unittest.main()
