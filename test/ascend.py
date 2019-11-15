# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_ascend(unittest.TestCase):
    def test_builds_an_ascending_comparator_function_out_of_the_identity_function(self):
        from functools import cmp_to_key
        eq(self, sorted([3, 1, 8, 1, 2, 5], key=cmp_to_key(R.ascend(R.identity))), [1, 1, 2, 3, 5, 8])


if __name__ == '__main__':
    unittest.main()
