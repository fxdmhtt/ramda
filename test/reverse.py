# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_reverse(unittest.TestCase):
    def test_reverses_arrays(self):
        eq(self, R.reverse([]), [])
        eq(self, R.reverse([1]), [1])
        eq(self, R.reverse([1, 2]), [2, 1])
        eq(self, R.reverse([1, 2, 3]), [3, 2, 1])

    def test_reverses_strings(self):
        eq(self, R.reverse(''), '')
        eq(self, R.reverse('a'), 'a')
        eq(self, R.reverse('ab'), 'ba')
        eq(self, R.reverse('abc'), 'cba')


if __name__ == '__main__':
    unittest.main()
