# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_prepend(unittest.TestCase):
    def test_adds_the_element_to_the_beginning_of_the_list(self):
        eq(self, R.prepend('x', ['y', 'z']), ['x', 'y', 'z'])
        eq(self, R.prepend(['a', 'z'], ['x', 'y']), [['a', 'z'], 'x', 'y'])

    def test_works_on_empty_list(self):
        eq(self, R.prepend(1, []), [1])


if __name__ == '__main__':
    unittest.main()
