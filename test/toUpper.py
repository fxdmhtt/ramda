# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_toUpper(unittest.TestCase):
    def test_returns_the_upper_case_equivalent_of_the_input_string(self):
        eq(self, R.toUpper('abc'), 'ABC')


if __name__ == '__main__':
    unittest.main()
