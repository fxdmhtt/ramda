# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_insertAll(unittest.TestCase):
    def test_inserts_a_list_of_elements_into_the_given_list(self):
        list = ['a', 'b', 'c', 'd', 'e']
        eq(self, R.insertAll(2, ['x', 'y', 'z'], list), ['a', 'b', 'x', 'y', 'z', 'c', 'd', 'e'])

    def test_appends_to_the_end_of_the_list_if_the_index_is_too_large(self):
        list = ['a', 'b', 'c', 'd', 'e']
        eq(self, R.insertAll(8, ['p', 'q', 'r'], list), ['a', 'b', 'c', 'd', 'e', 'p', 'q', 'r'])


if __name__ == '__main__':
    unittest.main()
