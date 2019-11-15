# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
from datetime import date

class Test_always(unittest.TestCase):
    def test_returns_a_function_that_returns_the_object_initially_supplied(self):
        theMeaning = R.always(42)
        eq(self, theMeaning(), 42)
        eq(self, theMeaning(10), 42)
        eq(self, theMeaning(False), 42)

    def test_works_with_various_types(self):
        eq(self, R.always(False)(), False)
        eq(self, R.always('abc')(), 'abc')
        eq(self, R.always({'a': 1, 'b': 2})(), {'a': 1, 'b': 2})
        obj = {'a': 1, 'b': 2}
        eq(self, R.always(obj)(), obj)
        now = date(1776, 6, 4)
        eq(self, R.always(now)(), date(1776, 6, 4))
        eq(self, R.always(None)(), None)


if __name__ == '__main__':
    unittest.main()
