# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_identity(unittest.TestCase):
    def test_returns_its_first_argument(self):
        eq(self, R.identity(None), None)
        eq(self, R.identity('foo'), 'foo')
        eq(self, R.identity('foo', 'bar'), 'foo')

    def test_has_length_1(self):
        eq(self, R.identity.length, 1)


if __name__ == '__main__':
    unittest.main()
