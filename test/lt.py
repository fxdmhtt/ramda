# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_lt(unittest.TestCase):
    def test_reports_whether_one_item_is_less_than_another(self):
        eq(self, R.lt(3, 5), True)
        eq(self, R.lt(6, 4), False)
        eq(self, R.lt(7.0, 7.0), False)
        eq(self, R.lt('abc', 'xyz'), True)
        eq(self, R.lt('abcd', 'abc'), False)


if __name__ == '__main__':
    unittest.main()
