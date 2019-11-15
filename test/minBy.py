# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_minBy(unittest.TestCase):
    def test_returns_the_smaller_value_as_determined_by_the_function(self):
        eq(self, R.minBy(lambda n: n * n, -3, 2), 2)
        eq(self, R.minBy(R.prop('x'), {'x': 3, 'y': 1}, {'x': 5, 'y': 10}), {'x': 3, 'y': 1})


if __name__ == '__main__':
    unittest.main()
