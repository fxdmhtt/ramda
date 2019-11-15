# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_not(unittest.TestCase):
    def test_reverses_argument(self):
        eq(self, R.not_(False), True)
        eq(self, R.not_(1), False)
        eq(self, R.not_(''), True)


if __name__ == '__main__':
    unittest.main()
