# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_descend(unittest.TestCase):
    def test_builds_a_descending_comparator_function_out_of_the_identity_function(self):
        from functools import cmp_to_key
        eq(self, sorted([3, 1, 8, 1, 2, 5], key=cmp_to_key(R.descend(R.identity))), [8, 5, 3, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()
