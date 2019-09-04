# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_hasIn(unittest.TestCase):
    def setUp(self):
        self.fred = {'name': 'Fred', 'age': 23}
        self.anon = {'age': 99}

    def test_returns_a_function_that_checks_the_appropriate_property(self):
        nm = R.hasIn('name')
        self.assertTrue(callable(nm))
        eq(self, nm(self.fred), True)
        eq(self, nm(self.anon), False)

    # def test_checks_properties_from_the_prototype_chain(self):
    #     Person = function() {}
    #     Person.prototype.age = function() {}

    #     bob = Person()
    #     eq(self, R.hasIn('age', bob), True)

    def test_works_properly_when_called_with_two_arguments(self):
        eq(self, R.hasIn('name', self.fred), True)
        eq(self, R.hasIn('name', self.anon), False)


if __name__ == '__main__':
    unittest.main()
