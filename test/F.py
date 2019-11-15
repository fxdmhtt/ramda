# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_F(unittest.TestCase):
    def test_always_returns_False(self):
        eq(self, R.F(), False)
        eq(self, R.F(10), False)
        eq(self, R.F(True), False)


if __name__ == '__main__':
    unittest.main()
