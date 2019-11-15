# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_gte(unittest.TestCase):
    def test_reports_whether_one_item_is_greater_than_or_equal_to_another(self):
        eq(self, R.gte(3, 5), False)
        eq(self, R.gte(6, 4), True)
        eq(self, R.gte(7.0, 7.0), True)
        eq(self, R.gte('abc', 'xyz'), False)
        eq(self, R.gte('abcd', 'abc'), True)


if __name__ == '__main__':
    unittest.main()
