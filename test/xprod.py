# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_xprod(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2]
        self.b = ['a', 'b', 'c']

    def test_returns_an_empty_list_if_either_input_list_is_empty(self):
        eq(self, list(R.xprod([], [1, 2, 3])), [])
        eq(self, list(R.xprod([1, 2, 3], [])), [])

    def test_creates_the_collection_of_all_cross_product_pairs_of_its_parameters(self):
        eq(self, list(R.xprod(self.a, self.b)), [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')])


if __name__ == '__main__':
    unittest.main()
