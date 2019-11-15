# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_update(unittest.TestCase):
    def test_updates_the_value_at_the_given_index_of_the_supplied_array(self):
        eq(self, R.update(2, 4, [0, 1, 2, 3]), [0, 1, 4, 3])

    def test_offsets_negative_indexes_from_the_end_of_the_array(self):
        eq(self, R.update(-3, 4, [0, 1, 2, 3]), [0, 4, 2, 3])

    def test_returns_the_original_array_if_the_supplied_index_is_out_of_bounds(self):
        list = [0, 1, 2, 3]
        eq(self, R.update(4, 4, list), list)
        eq(self, R.update(-5, 4, list), list)

    def test_does_not_mutate_the_original_array(self):
        list = [0, 1, 2, 3]
        eq(self, R.update(2, 4, list), [0, 1, 4, 3])
        eq(self, list, [0, 1, 2, 3])

    def test_curries_the_arguments(self):
        eq(self, R.update(2)(4)([0, 1, 2, 3]), [0, 1, 4, 3])

    def test_accepts_an_array_like_object(self):
        def args(*arguments):
            return list(arguments)
        eq(self, R.update(2, 4, args(0, 1, 2, 3)), [0, 1, 4, 3])


if __name__ == '__main__':
    unittest.main()
