# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
from numbers import Number

class Test_propIs(unittest.TestCase):
    def test_returns_True_if_the_specified_object_property_is_of_the_given_type(self):
        eq(self, R.propIs(Number, 'value', {'value': 1}), True)

    def test_returns_False_otherwise(self):
        eq(self, R.propIs(str, 'value', {'value': 1}), False)
        eq(self, R.propIs(str, 'value', {}), False)


if __name__ == '__main__':
    unittest.main()
