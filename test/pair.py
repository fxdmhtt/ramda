# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_pair(unittest.TestCase):
    def test_creates_a_two_element_array(self):
        eq(self, R.pair('foo', 'bar'), ['foo', 'bar'])
        eq(self, R.pair('foo')('bar'), ['foo', 'bar'])


if __name__ == '__main__':
    unittest.main()
