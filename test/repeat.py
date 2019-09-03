# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_repeat(unittest.TestCase):
    def test_returns_a_lazy_list_of_identical_values(self):
        eq(self, R.repeat(0, 5), [0, 0, 0, 0, 0])

    def test_can_accept_any_value_including_None(self):
        eq(self, R.repeat(None, 3), [None, None, None])


if __name__ == '__main__':
    unittest.main()
