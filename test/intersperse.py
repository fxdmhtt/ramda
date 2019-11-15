# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_intersperse(unittest.TestCase):
    def test_interposes_a_separator_between_list_items(self):
        eq(self, R.intersperse('n', ['ba', 'a', 'a']), ['ba', 'n', 'a', 'n', 'a'])
        eq(self, R.intersperse('bar', ['foo']), ['foo'])
        eq(self, R.intersperse('bar', []), [])

    def test_dispatches(self):
        obj = {'intersperse': lambda x: 'override ' + str(x)}
        eq(self, R.intersperse('x', obj), 'override x')


if __name__ == '__main__':
    unittest.main()
