# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_uniqWith(unittest.TestCase):
    def setUp(self):
        self.objs = [
            {'x': R.T, 'i': 0}, {'x': R.F, 'i': 1}, {'x': R.T, 'i': 2}, {'x': R.T, 'i': 3},
            {'x': R.F, 'i': 4}, {'x': R.F, 'i': 5}, {'x': R.T, 'i': 6}, {'x': R.F, 'i': 7}
        ]
        self.objs2 = [
            {'x': R.T, 'i': 0}, {'x': R.F, 'i': 1}, {'x': R.T, 'i': 2}, {'x': R.T, 'i': 3},
            {'x': R.F, 'i': 0}, {'x': R.T, 'i': 1}, {'x': R.F, 'i': 2}, {'x': R.F, 'i': 3}
        ]
        self.eqI = lambda x, accX: x['i'] == accX['i']

    def test_returns_a_set_from_any_array_purges_duplicate_elements_based_on_predicate(self):
        eq(self, R.uniqWith(self.eqI, self.objs), self.objs)
        eq(self, R.uniqWith(self.eqI, self.objs2), [{'x': R.T, 'i': 0}, {'x': R.F, 'i': 1}, {'x': R.T, 'i': 2}, {'x': R.T, 'i': 3}])

    def test_keeps_elements_from_the_left(self):
        eq(self, R.uniqWith(self.eqI, [{'i': 1}, {'i': 2}, {'i': 3}, {'i': 4}, {'i': 1}]), [{'i': 1}, {'i': 2}, {'i': 3}, {'i': 4}])

    def test_returns_an_empty_array_for_an_empty_array(self):
        eq(self, R.uniqWith(self.eqI, []), [])


if __name__ == '__main__':
    unittest.main()
