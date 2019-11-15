# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest
import datetime

class Test_min(unittest.TestCase):
    def test_returns_the_smaller_of_its_two_arguments(self):
        eq(self, R.min(-7, 7), -7)
        eq(self, R.min(7, -7), -7)

    def test_works_for_any_orderable_type(self):
        d1 = datetime.date(2001, 1, 1)
        d2 = datetime.date(2002, 2, 2)

        eq(self, R.min(d1, d2), d1)
        eq(self, R.min(d2, d1), d1)
        eq(self, R.min('a', 'b'), 'a')
        eq(self, R.min('b', 'a'), 'a')


if __name__ == '__main__':
    unittest.main()
