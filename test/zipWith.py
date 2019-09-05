# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_zipWith(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 3]
        self.b = [100, 200, 300]
        self.c = [10, 20, 30, 40, 50, 60]
        self.add = lambda a, b: a + b
        self.x = lambda a, b: a * b
        self.s = lambda a, b: str(a) + ' cow ' + str(b)

    def test_returns_an_array_created_by_applying_its_passed_in_function_pair_wise_on_its_passed_in_arrays(self):
        self.assertSequenceEqual(list(R.zipWith(self.add, self.a, self.b)), [101, 202, 303])
        self.assertSequenceEqual(list(R.zipWith(self.x, self.a, self.b)), [100, 400, 900])
        self.assertSequenceEqual(list(R.zipWith(self.s, self.a, self.b)), ['1 cow 100', '2 cow 200', '3 cow 300'])

    def test_returns_an_array_whose_length_is_equal_to_the_shorter_of_its_input_arrays(self):
        self.assertEqual(len(list(R.zipWith(self.add, self.a, self.c))), len(self.a))


if __name__ == '__main__':
    unittest.main()
