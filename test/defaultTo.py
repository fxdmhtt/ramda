# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_defaultTo(unittest.TestCase):
    def setUp(self):
        self.defaultTo42 = R.defaultTo(42)

    def test_returns_the_default_value_if_input_is_None_None_or_NaN(self):
        eq(self, 42, self.defaultTo42(None))
        eq(self, 42, self.defaultTo42(float('nan')))

    def test_returns_the_input_value_if_it_is_not_None_None(self):
        eq(self, 'a real value', self.defaultTo42('a real value'))

    def test_returns_the_input_value_even_if_it_is_considered_falsy(self):
        eq(self, '', self.defaultTo42(''))
        eq(self, 0, self.defaultTo42(0))
        eq(self, False, self.defaultTo42(False))
        eq(self, [], self.defaultTo42([]))

    def test_can_be_called_with_both_arguments_directly(self):
        eq(self, 42, R.defaultTo(42, None))
        eq(self, 'a real value', R.defaultTo(42, 'a real value'))


if __name__ == '__main__':
    unittest.main()
