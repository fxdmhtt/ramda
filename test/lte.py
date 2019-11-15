# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_lte(unittest.TestCase):
    def test_reports_whether_one_item_is_less_than_or_equal_to_another(self):
        eq(self, R.lte(3, 5), True)
        eq(self, R.lte(6, 4), False)
        eq(self, R.lte(7.0, 7.0), True)
        eq(self, R.lte('abc', 'xyz'), True)
        eq(self, R.lte('abcd', 'abc'), False)


if __name__ == '__main__':
    unittest.main()
