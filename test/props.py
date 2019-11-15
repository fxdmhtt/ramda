# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_props(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    def test_returns_empty_array_if_no_properties_requested(self):
        eq(self, R.props([], self.obj), [])

    def test_returns_values_for_requested_properties(self):
        eq(self, R.props(['a', 'e'], self.obj), [1, 5])

    def test_preserves_order(self):
        eq(self, R.props(['f', 'c', 'e'], self.obj), [6, 3, 5])

    def test_returns_None_for_nonexistent_properties(self):
        ps = R.props(['a', 'nonexistent'], self.obj)
        eq(self, len(ps), 2)
        eq(self, ps[0], 1)
        eq(self, ps[1], None)


if __name__ == '__main__':
    unittest.main()
