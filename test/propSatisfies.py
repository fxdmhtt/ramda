# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_propSatisfies(unittest.TestCase):
    def setUp(self):
        self.isPositive = lambda n: n > 0

    def test_returns_True_if_the_specified_object_property_satisfies_the_given_predicate(self):
        eq(self, R.propSatisfies(self.isPositive, 'x', {'x': 1, 'y': 0}), True)

    def test_returns_False_otherwise(self):
        eq(self, R.propSatisfies(self.isPositive, 'y', {'x': 1, 'y': 0}), False)

    # def test_returns_False_if_given_a_None_or_None_object(self):
    #     eq(self, R.propSatisfies(self.isPositive, 'y', None), False)


if __name__ == '__main__':
    unittest.main()
