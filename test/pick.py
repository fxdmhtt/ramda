# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_pick(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 1: 7}

    def test_copies_the_named_properties_of_an_object_to_the_new_object(self):
        eq(self, R.pick(['a', 'c', 'f'], self.obj), {'a': 1, 'c': 3, 'f': 6})

    def test_handles_numbers_as_properties(self):
        eq(self, R.pick([1], self.obj), {1: 7})

    def test_ignores_properties_not_included(self):
        eq(self, R.pick(['a', 'c', 'g'], self.obj), {'a': 1, 'c': 3})

    # def test_retrieves_prototype_properties(self):
    #     F = function(param) {this.x = param}
    #     F.prototype.y = 40 F.prototype.z = 50
    #     self.obj = F(30)
    #     self.obj.v = 10 self.obj.w = 20
    #     eq(self, R.pick(['w', 'x', 'y'], self.obj), {'w': 20, 'x': 30, 'y': 40})


if __name__ == '__main__':
    unittest.main()
