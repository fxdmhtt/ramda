# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_gt(unittest.TestCase):
    def test_reports_whether_one_item_is_greater_than_another(self):
        eq(self, R.gt(3, 5), False)
        eq(self, R.gt(6, 4), True)
        eq(self, R.gt(7.0, 7.0), False)
        eq(self, R.gt('abc', 'xyz'), False)
        eq(self, R.gt('abcd', 'abc'), True)


if __name__ == '__main__':
    unittest.main()
