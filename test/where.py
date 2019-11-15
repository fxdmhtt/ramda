# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_where(unittest.TestCase):
    def test_returns_True_if_the_test_object_satisfies_the_spec(self):
        spec = {'x': R.equals(1), 'y': R.equals(2)}
        test1 = {'x': 0, 'y': 200}
        test2 = {'x': 0, 'y': 10}
        test3 = {'x': 1, 'y': 101}
        test4 = {'x': 1, 'y': 2}
        eq(self, R.where(spec, test1), False)
        eq(self, R.where(spec, test2), False)
        eq(self, R.where(spec, test3), False)
        eq(self, R.where(spec, test4), True)

    def test_does_not_need_the_spec_and_the_test_object_to_have_the_same_interface_the_test_object_will_have_a_superset_of_the_specs_properties(self):
        spec = {'x': R.equals(100)}
        test1 = {'x': 20, 'y': 100, 'z': 100}
        test2 = {'w': 1, 'x': 100, 'y': 100, 'z': 100}

        eq(self, R.where(spec, test1), False)
        eq(self, R.where(spec, test2), True)

    def test_matches_specs_that_have_None_properties(self):
        spec = {'x': R.equals(None)}
        test1 = {}
        # test2 = {'x': None}
        test3 = {'x': None}
        test4 = {'x': 1}
        eq(self, R.where(spec, test1), True)
        # eq(self, R.where(spec, test2), False)
        eq(self, R.where(spec, test3), True)
        eq(self, R.where(spec, test4), False)

    def test_is_True_for_an_empty_spec(self):
        eq(self, R.where({}, {'a': 1}), True)

    # def test_matches_inherited_properties(self):
    #     spec = {
    #         'toString': R.equals(Object.prototype.toString),
    #         'valueOf': R.equals(Object.prototype.valueOf)
    #     }
    #     eq(self, R.where(spec, {}), True)

    # def test_does_not_match_inherited_spec(self):
    #     function Spec() { this.y = R.equals(6) }
    #     Spec.prototype.x = R.equals(5)
    #     spec = Spec()

    #     eq(self, R.where(spec, {'y': 6}), True)
    #     eq(self, R.where(spec, {'x': 5}), False)


if __name__ == '__main__':
    unittest.main()
