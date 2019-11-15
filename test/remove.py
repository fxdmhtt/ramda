# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_remove(unittest.TestCase):
    def test_splices_out_a_sub_list_of_the_given_list(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        eq(self, R.remove(2, 5, list), ['a', 'b', 'h', 'i', 'j'])

    def test_returns_the_appropriate_sublist_when_start_eq_0(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        eq(self, R.remove(0, 5, list), ['f', 'g', 'h', 'i', 'j'])
        eq(self, R.remove(0, 1, list), ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
        eq(self, R.remove(0, len(list), list), [])

    def test_removes_the_end_of_the_list_if_the_count_is_too_large(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        eq(self, R.remove(2, 20, list), ['a', 'b'])

    def test_retains_the_entire_list_if_the_start_is_too_large(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        eq(self, R.remove(13, 3, list), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


if __name__ == '__main__':
    unittest.main()
