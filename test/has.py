# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_has(unittest.TestCase):
    def setUp(self):
        self.fred = {'name': 'Fred', 'age': 23}
        self.anon = {'age': 99}

    def test_returns_True_if_the_specified_property_is_present(self):
        eq(self, R.has('name', self.fred), True)

    def test_returns_False_if_the_specified_property_is_absent(self):
        eq(self, R.has('name', self.anon), False)

    # def test_does_not_check_properties_from_the_prototype_chain(self):
    #     Person = function() {}
    #     Person.prototype.age = function() {}

    #     bob = Person()
    #     eq(self, R.has('age', bob), False)

    def test_returns_False_for_non_objects(self):
        eq(self, R.has('a', None), False)
        eq(self, R.has('a', None), False)
        eq(self, R.has('a', True), False)
        eq(self, R.has('a', ''), False)
        # eq(self, R.has('a', /a/), False)

    def test_tests_currying(self):
        eq(self, R.has('a')({ 'a': { 'b': 1 } }), True)


if __name__ == '__main__':
    unittest.main()
