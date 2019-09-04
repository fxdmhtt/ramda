# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_dropLast(unittest.TestCase):
    def test_skips_the_last_n_elements_from_a_list_returning_the_remainder(self):
        eq(self, R.dropLast(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g']), ['a', 'b', 'c', 'd'])

    def test_returns_an_empty_array_if_n_is_too_large(self):
        eq(self, R.dropLast(20, ['a', 'b', 'c', 'd', 'e', 'f', 'g']), [])

    def test_returns_an_equivalent_list_if_n_is_0(self):
        eq(self, R.dropLast(0, [1, 2, 3]), [1, 2, 3])
        eq(self, R.dropLast(-1, [1, 2, 3]), [1, 2, 3])
        import sys
        eq(self, R.dropLast(-sys.maxsize, [1, 2, 3]), [1, 2, 3])

    def test_never_returns_the_input_array(self):
        xs = [1, 2, 3]

        self.assertIsNot(R.dropLast(0, xs), xs)
        self.assertIsNot(R.dropLast(-1, xs), xs)

    def test_can_operate_on_strings(self):
        eq(self, R.dropLast(3, 'Ramda'), 'Ra')

    # def test_can_act_as_a_transducer(self):
    #     dropLast2 = R.dropLast(2)
    #     assert.deepEqual(R.into([], dropLast2, [1, 3, 5, 7, 9, 1, 2]), [1, 3, 5, 7, 9])
    #     assert.deepEqual(R.into([], dropLast2, [1]), [])


if __name__ == '__main__':
    unittest.main()
