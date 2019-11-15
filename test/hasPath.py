# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_hasPath(unittest.TestCase):
    def setUp(self):
        self.obj = {
            'objVal': {'b': {'c': 'c'}},
            'FalseVal': False,
            'NoneVal': None,
            'arrayVal': ['arr']
        }

    def test_returns_True_for_existing_path(self):
        eq(self, R.hasPath(['objVal'], self.obj), True)
        eq(self, R.hasPath(['objVal', 'b'], self.obj), True)
        eq(self, R.hasPath(['objVal', 'b', 'c'], self.obj), True)
        eq(self, R.hasPath(['arrayVal'], self.obj), True)

    def test_returns_True_for_existing_path_to_falsy_values(self):
        eq(self, R.hasPath(['FalseVal'], self.obj), True)
        eq(self, R.hasPath(['NoneVal'], self.obj), True)
        eq(self, R.hasPath(['NoneVal'], self.obj), True)

    def test_return_False_for_a_test_for_a_child_to_a_non_object(self):
        eq(self, R.hasPath(['NoneVal', 'child', 'grandchild'], self.obj), False)
        eq(self, R.hasPath(['FalseVal', 'child', 'grandchild'], self.obj), False)
        eq(self, R.hasPath(['NoneVal', 'child', 'grandchild'], self.obj), False)
        eq(self, R.hasPath(['arrayVal', 0, 'child', 'grandchild'], self.obj), False)

    def test_returns_True_for_existing_path_with_indexes(self):
        eq(self, R.hasPath(['arrayVal', 0], self.obj), True)

    def test_returns_False_for_non_existing_path_with_indexes(self):
        eq(self, R.hasPath(['arrayVal', 1], self.obj), False)

    def test_tests_for_paths_in_arrays(self):
        eq(self, R.hasPath([0], [1, 2]), True)
        eq(self, R.hasPath([2], [1, 2]), False)

        # eq(self, R.hasPath(['0'], [1, 2]), True)
        # eq(self, R.hasPath(['2'], [1, 2]), False)

    def test_returns_False_for_non_existent_path(self):
        eq(self, R.hasPath(['Unknown'], self.obj), False)
        eq(self, R.hasPath(['objVal', 'Unknown'], self.obj), False)

    # def test_does_not_check_properties_from_the_prototype_chain(self):
    #     Person = function() {}
    #     Person.prototype.age = {x: 1}
    #     bob = Person()

    #     eq(self, R.hasPath(['age'], bob), False)
    #     eq(self, R.hasPath(['age', 'x'], bob), False)
    #     eq(self, R.hasPath(['toString'], bob), False)

    def test_returns_False_for_non_objects(self):
        eq(self, R.hasPath([], self.obj), False)

    def test_tests_paths_on_non_objects(self):
        eq(self, R.hasPath(['a', 'b'], None), False)
        eq(self, R.hasPath(['a', 'b'], None), False)
        eq(self, R.hasPath('a', True), False)
        eq(self, R.hasPath('a', ''), False)
        # eq(self, R.hasPath('a', /a/), False)

    def test_tests_currying(self):
        eq(self, R.hasPath(['a', 'b'])({ 'a': { 'b': 1 } }), True)


if __name__ == '__main__':
    unittest.main()
