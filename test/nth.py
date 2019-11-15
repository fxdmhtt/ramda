# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_nth(unittest.TestCase):
    def setUp(self):
        self.list = ['foo', 'bar', 'baz', 'quux']

    def test_accepts_positive_offsets(self):
        eq(self, R.nth(0, self.list), 'foo')
        eq(self, R.nth(1, self.list), 'bar')
        eq(self, R.nth(2, self.list), 'baz')
        eq(self, R.nth(3, self.list), 'quux')
        eq(self, R.nth(4, self.list), None)

        eq(self, R.nth(0, 'abc'), 'a')
        eq(self, R.nth(1, 'abc'), 'b')
        eq(self, R.nth(2, 'abc'), 'c')
        eq(self, R.nth(3, 'abc'), '')

    def test_accepts_negative_offsets(self):
        eq(self, R.nth(-1, self.list), 'quux')
        eq(self, R.nth(-2, self.list), 'baz')
        eq(self, R.nth(-3, self.list), 'bar')
        eq(self, R.nth(-4, self.list), 'foo')
        eq(self, R.nth(-5, self.list), None)

        eq(self, R.nth(-1, 'abc'), 'c')
        eq(self, R.nth(-2, 'abc'), 'b')
        eq(self, R.nth(-3, 'abc'), 'a')
        eq(self, R.nth(-4, 'abc'), '')

    def test_throws_if_applied_to_None_or_None(self):
        with self.assertRaises(TypeError):
            R.nth(0, None)


if __name__ == '__main__':
    unittest.main()
