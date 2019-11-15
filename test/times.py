# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_times(unittest.TestCase):
    def test_takes_a_map_func(self):
        self.assertSequenceEqual(list(R.times(R.identity, 5)), [0, 1, 2, 3, 4])
        self.assertSequenceEqual(list(R.times(lambda x: \
            x * 2
        , 5)), [0, 2, 4, 6, 8])

    def test_throws_if_second_argument_is_not_a_valid_array_length(self):
        with self.assertRaises(ValueError):
            list(R.times(3)('cheers!'))
            list(R.times(R.identity, -1))


if __name__ == '__main__':
    unittest.main()
