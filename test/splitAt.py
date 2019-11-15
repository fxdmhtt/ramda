# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_splitAt(unittest.TestCase):
    def test_splits_an_array_at_a_given_index(self):
        eq(self, R.splitAt(1, [1, 2, 3]), [[1], [2, 3]])

    def test_splits_a_string_at_a_given_index(self):
        eq(self, R.splitAt(5, 'hello world'), ['hello', ' world'])

    def test_can_handle_index_greater_than_array_length(self):
        eq(self, R.splitAt(4, [1, 2]), [[1, 2], []])

    def test_can_support_negative_index(self):
        eq(self, R.splitAt(-1, 'foobar'), ['fooba', 'r'])


if __name__ == '__main__':
    unittest.main()
