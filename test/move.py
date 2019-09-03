# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

list = ['a', 'b', 'c', 'd', 'e', 'f']

class Test_move(unittest.TestCase):
    def test_moves_an_element_from_an_index_to_another(self):
        eq(self, R.move(0, 1, list), ['b', 'a', 'c', 'd', 'e', 'f'])
        eq(self, R.move(2, 1, list), ['a', 'c', 'b', 'd', 'e', 'f'])
        eq(self, R.move(-1, 0, list), ['f', 'a', 'b', 'c', 'd', 'e'])
        eq(self, R.move(0, -1, list), ['b', 'c', 'd', 'e', 'f', 'a'])

    def test_does_nothing_when_indexes_are_outside_the_list_outbounds(self):
        eq(self, R.move(-20, 2, list), list)
        eq(self, R.move(20, 2, list), list)
        eq(self, R.move(2, 20, list), list)
        eq(self, R.move(2, -20, list), list)
        eq(self, R.move(20, 20, list), list)
        eq(self, R.move(-20, -20, list), list)


if __name__ == '__main__':
    unittest.main()
