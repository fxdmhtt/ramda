# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_drop(unittest.TestCase):
    def test_skips_the_first_n_elements_from_a_list_returning_the_remainder(self):
        eq(self, R.drop(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g']), ['d', 'e', 'f', 'g'])

    def test_returns_an_empty_array_if_n_is_too_large(self):
        eq(self, R.drop(20, ['a', 'b', 'c', 'd', 'e', 'f', 'g']), [])

    def test_returns_an_equivalent_list_if_n_is_0(self):
        eq(self, R.drop(0, [1, 2, 3]), [1, 2, 3])
        eq(self, R.drop(-1, [1, 2, 3]), [1, 2, 3])
        import sys
        eq(self, R.drop(-sys.maxsize, [1, 2, 3]), [1, 2, 3])

    def test_never_returns_the_input_array(self):
        xs = [1, 2, 3]

        self.assertIsNot(R.drop(0, xs), xs)
        self.assertIsNot(R.drop(-1, xs), xs)

    def test_can_operate_on_strings(self):
        eq(self, R.drop(3, 'Ramda'), 'da')
        eq(self, R.drop(4, 'Ramda'), 'a')
        eq(self, R.drop(5, 'Ramda'), '')
        eq(self, R.drop(6, 'Ramda'), '')


if __name__ == '__main__':
    unittest.main()
