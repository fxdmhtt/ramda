# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import datetime

class Test_max(unittest.TestCase):
    def test_returns_the_larger_of_its_two_arguments(self):
        eq(self, R.max(-7, 7), 7)
        eq(self, R.max(7, -7), 7)

    def test_works_for_any_orderable_type(self):
        d1 = datetime.date(2001, 1, 1)
        d2 = datetime.date(2002, 2, 2)

        eq(self, R.max(d1, d2), d2)
        eq(self, R.max(d2, d1), d2)
        eq(self, R.max('a', 'b'), 'b')
        eq(self, R.max('b', 'a'), 'b')


if __name__ == '__main__':
    unittest.main()
