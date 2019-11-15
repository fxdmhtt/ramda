# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_insert(unittest.TestCase):
    def test_inserts_an_element_into_the_given_list(self):
        list = ['a', 'b', 'c', 'd', 'e']
        eq(self, R.insert(2, 'x', list), ['a', 'b', 'x', 'c', 'd', 'e'])

    def test_inserts_another_list_as_an_element(self):
        list = ['a', 'b', 'c', 'd', 'e']
        eq(self, R.insert(2, ['s', 't'], list), ['a', 'b', ['s', 't'], 'c', 'd', 'e'])

    def test_appends_to_the_end_of_the_list_if_the_index_is_too_large(self):
        list = ['a', 'b', 'c', 'd', 'e']
        eq(self, R.insert(8, 'z', list), ['a', 'b', 'c', 'd', 'e', 'z'])


if __name__ == '__main__':
    unittest.main()
