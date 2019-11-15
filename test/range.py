# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_range(unittest.TestCase):
    def test_returns_list_of_numbers(self):
        eq(self, R.range(0, 5), [0, 1, 2, 3, 4])
        eq(self, R.range(4, 7), [4, 5, 6])

    def test_returns_the_empty_list_if_the_first_parameter_is_not_larger_than_the_second(self):
        eq(self, R.range(7, 3), [])
        eq(self, R.range(5, 5), [])

    def test_returns_an_empty_array_if_from_to(self):
        result = R.range(10, 5)
        eq(self, result, [])
        result.append(5)
        eq(self, R.range(10, 5), [])

    def test_terminates_given_bad_input(self):
        with self.assertRaises(TypeError):
            R.range('a', 'z')


if __name__ == '__main__':
    unittest.main()
