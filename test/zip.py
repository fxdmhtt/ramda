# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_zip(unittest.TestCase):
    def test_returns_an_array_of_tuples(self):
        a = [1, 2, 3]
        b = [100, 200, 300]

        self.assertSequenceEqual(list(R.zip(a, b)), [(1, 100), (2, 200), (3, 300)])

    def test_returns_a_list_as_long_as_the_shorter_of_the_lists_input(self):
        a = [1, 2, 3]
        b = [100, 200, 300, 400]
        c = [10, 20]

        self.assertSequenceEqual(list(R.zip(a, b)), [(1, 100), (2, 200), (3, 300)])
        self.assertSequenceEqual(list(R.zip(a, c)), [(1, 10), (2, 20)])


if __name__ == '__main__':
    unittest.main()
