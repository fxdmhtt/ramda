# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_propOr(unittest.TestCase):
    def setUp(self):
        self.fred = {'name': 'Fred', 'age': 23}
        self.anon = {'age': 99}

        self.nm = R.propOr('Unknown', 'name')

    def test_returns_a_function_that_fetches_the_appropriate_property(self):
        self.assertTrue(callable(self.nm))
        eq(self, self.nm(self.fred), 'Fred')

    def test_returns_the_default_value_when_the_property_does_not_exist(self):
        eq(self, self.nm(self.anon), 'Unknown')

    def test_returns_the_default_value_when_the_object_is_nil(self):
        eq(self, self.nm(None), 'Unknown')

    def test_uses_the_default_when_supplied_an_object_with_a_nil_value(self):
        eq(self, R.propOr('foo', 'x', {'x': None}), 'foo')
        eq(self, R.propOr('foo', 'x', {'x': None}), 'foo')


if __name__ == '__main__':
    unittest.main()
