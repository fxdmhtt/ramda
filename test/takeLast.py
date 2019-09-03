# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_takeLast(unittest.TestCase):
    def test_takes_only_the_last_n_elements_from_a_list(self):
        eq(self, R.takeLast(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g']), ['e', 'f', 'g'])

    def test_returns_only_as_many_as_the_array_can_provide(self):
        eq(self, R.takeLast(3, [1, 2]), [1, 2])
        eq(self, R.takeLast(3, []), [])

    def test_returns_an_equivalent_list_if_n_is_lt_0(self):
        eq(self, R.takeLast(-1, [1, 2, 3]), [1, 2, 3])
        import sys
        eq(self, R.takeLast(-sys.maxsize, [1, 2, 3]), [1, 2, 3])

    def test_never_returns_the_input_array(self):
        xs = [1, 2, 3]

        self.assertEqual(R.takeLast(3, xs), xs)
        import sys
        self.assertEqual(R.takeLast(sys.maxsize, xs), xs)
        self.assertEqual(R.takeLast(-1, xs), xs)

    def test_can_operate_on_strings(self):
        eq(self, R.takeLast(3, 'Ramda'), 'mda')

    def test_handles_zero_correctly_1224(self):
        eq(self, R.takeLast(0, [1, 2, 3]), [])


if __name__ == '__main__':
    unittest.main()
