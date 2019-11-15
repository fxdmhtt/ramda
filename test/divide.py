# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_divide(unittest.TestCase):
    def test_divides_two_numbers(self):
        eq(self, R.divide(28, 7), 4.0)


if __name__ == '__main__':
    unittest.main()
