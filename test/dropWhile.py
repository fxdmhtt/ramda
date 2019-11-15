# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_dropWhile(unittest.TestCase):
    def test_skips_elements_while_the_function_reports_True(self):
        eq(self, R.dropWhile(lambda x: x < 5, [1, 3, 5, 7, 9]), [5, 7, 9])

    def test_returns_an_empty_list_for_an_empty_list(self):
        eq(self, R.dropWhile(lambda : False, []), [])
        eq(self, R.dropWhile(lambda : True, []), [])

    def test_starts_at_the_right_arg_and_acknowledges_None(self):
        sublist = R.dropWhile(lambda x: bool(x), [1, 3, None, 5, 7])
        eq(self, len(sublist), 3)
        eq(self, sublist[0], None)
        eq(self, sublist[1], 5)
        eq(self, sublist[2], 7)

    def test_can_operate_on_strings(self):
        eq(self, R.dropWhile(lambda x: x != 'd', 'Ramda'), 'da')


if __name__ == '__main__':
    unittest.main()
