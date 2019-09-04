# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_prop(unittest.TestCase):
    def setUp(self):
        self.fred = {'name': 'Fred', 'age': 23}

    def test_returns_a_function_that_fetches_the_appropriate_property(self):
        nm = R.prop('name')
        self.assertTrue(callable(nm))
        eq(self, nm(self.fred), 'Fred')

    def test_shows_the_same_behaviour_as_path_for_an_None_object(self):
        propException = None
        try:
            propResult = R.prop('name', None)
        except Exception as e:
            propException = e

        pathException = None
        try:
            pathResult = R.path(['name'], None)
        except Exception as e:
            pathException = e

        eq(self, propResult, pathResult)
        eq(self, propException, pathException)


if __name__ == '__main__':
    unittest.main()
