# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_last(unittest.TestCase):
    def test_returns_the_last_element_of_an_ordered_collection(self):
        eq(self, R.last([1, 2, 3]), 3)
        eq(self, R.last([1, 2]), 2)
        eq(self, R.last([1]), 1)
        eq(self, R.last([]), None)

        eq(self, R.last('abc'), 'c')
        eq(self, R.last('ab'), 'b')
        eq(self, R.last('a'), 'a')
        eq(self, R.last(''), '')

    def test_throws_if_applied_to_None_or_None(self):
        with self.assertRaises(TypeError):
            R.last(None)


if __name__ == '__main__':
    unittest.main()
