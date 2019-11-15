# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_isNil(unittest.TestCase):
    def test_tests_a_value_for_None_or_None(self):
        eq(self, R.isNil(None), True)
        eq(self, R.isNil(None), True)
        eq(self, R.isNil([]), False)
        eq(self, R.isNil({}), False)
        eq(self, R.isNil(0), False)
        eq(self, R.isNil(''), False)


if __name__ == '__main__':
    unittest.main()
