# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_sort(unittest.TestCase):
    def test_sorts_the_elements_of_a_list(self):
        eq(self, R.sort(lambda a, b: a - b, [3, 1, 8, 1, 2, 5]), [1, 1, 2, 3, 5, 8])

    def test_does_not_affect_the_list_passed_supplied(self):
        list = [3, 1, 8, 1, 2, 5]
        eq(self, R.sort(lambda a, b: a - b, list), [1, 1, 2, 3, 5, 8])
        eq(self, list, [3, 1, 8, 1, 2, 5])


if __name__ == '__main__':
    unittest.main()
