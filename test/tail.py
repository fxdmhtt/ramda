# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_tail(unittest.TestCase):
    def test_returns_the_tail_of_an_ordered_collection(self):
        eq(self, R.tail([1, 2, 3]), [2, 3])
        eq(self, R.tail([2, 3]), [3])
        eq(self, R.tail([3]), [])
        eq(self, R.tail([]), [])

        eq(self, R.tail('abc'), 'bc')
        eq(self, R.tail('bc'), 'c')
        eq(self, R.tail('c'), '')
        eq(self, R.tail(''), '')

    def test_throws_if_applied_to_None_or_None(self):
        with self.assertRaises(TypeError):
            R.tail(None)


if __name__ == '__main__':
    unittest.main()
