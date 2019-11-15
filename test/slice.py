# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_slice(unittest.TestCase):
    def test_retrieves_the_proper_sublist_of_a_list(self):
        list = [8, 6, 7, 5, 3, 0, 9]
        eq(self, R.slice(2, 5, list), [7, 5, 3])

    def test_handles_array_like_object(self):
        args = (lambda *arguments: list(arguments))(1, 2, 3, 4, 5)
        eq(self, R.slice(1, 4, args), [2, 3, 4])

    def test_can_operate_on_strings(self):
        eq(self, R.slice(0, 0, 'abc'), '')
        eq(self, R.slice(0, 1, 'abc'), 'a')
        eq(self, R.slice(0, 2, 'abc'), 'ab')
        eq(self, R.slice(0, 3, 'abc'), 'abc')
        eq(self, R.slice(0, 4, 'abc'), 'abc')
        eq(self, R.slice(1, 0, 'abc'), '')
        eq(self, R.slice(1, 1, 'abc'), '')
        eq(self, R.slice(1, 2, 'abc'), 'b')
        eq(self, R.slice(1, 3, 'abc'), 'bc')
        eq(self, R.slice(1, 4, 'abc'), 'bc')
        eq(self, R.slice(0, -4, 'abc'), '')
        eq(self, R.slice(0, -3, 'abc'), '')
        eq(self, R.slice(0, -2, 'abc'), 'a')
        eq(self, R.slice(0, -1, 'abc'), 'ab')
        eq(self, R.slice(0, -0, 'abc'), '')
        eq(self, R.slice(-2, -4, 'abc'), '')
        eq(self, R.slice(-2, -3, 'abc'), '')
        eq(self, R.slice(-2, -2, 'abc'), '')
        eq(self, R.slice(-2, -1, 'abc'), 'b')
        eq(self, R.slice(-2, -0, 'abc'), '')


if __name__ == '__main__':
    unittest.main()
