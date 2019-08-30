# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_adjust(unittest.TestCase):
    def test_applies_the_given_function_to_the_value_at_the_given_index_of_the_supplied_array(self):
        eq(self, R.adjust(2, R.add(1), [0, 1, 2, 3]), [0, 1, 3, 3])
    
    def test_offsets_negative_indexes_from_the_end_of_the_array(self):
        eq(self, R.adjust(-3, R.add(1), [0, 1, 2, 3]), [0, 2, 2, 3])
    
    def test_returns_the_original_array_if_the_supplied_index_is_out_of_bounds(self):
        list = [0, 1, 2, 3]
        eq(self, R.adjust(4, R.add(1), list), list)
        eq(self, R.adjust(-5, R.add(1), list), list)

    def test_does_not_mutate_the_original_array(self):
        list = [0, 1, 2, 3]
        eq(self, R.adjust(2, R.add(1), list), [0, 1, 3, 3])
        eq(self, list, [0, 1, 2, 3])
    
    def test_accepts_an_array_like_object(self):
        def args(*arguments):
            return arguments
        eq(self, R.adjust(2, R.add(1), args(0, 1, 2, 3)), [0, 1, 3, 3])


if __name__ == '__main__':
        unittest.main()
