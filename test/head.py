# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_head(unittest.TestCase):
    def test_returns_the_first_element_of_an_ordered_collection(self):
        eq(self, R.head([1, 2, 3]), 1)
        eq(self, R.head([2, 3]), 2)
        eq(self, R.head([3]), 3)
        eq(self, R.head([]), None)

        eq(self, R.head('abc'), 'a')
        eq(self, R.head('bc'), 'b')
        eq(self, R.head('c'), 'c')
        eq(self, R.head(''), '')

    def test_throws_if_applied_to_None_or_None(self):
        with self.assertRaises(TypeError):
            R.head(None)


if __name__ == '__main__':
    unittest.main()
