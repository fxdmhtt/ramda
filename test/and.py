# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_and(unittest.TestCase):
    def test_compares_two_values_with_and(self):
        eq(self, R.and_(True, True), True)
        eq(self, R.and_(True, False), False)
        eq(self, R.and_(False, True), False)
        eq(self, R.and_(False, False), False)


if __name__ == '__main__':
    unittest.main()
