# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_omit(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    def test_copies_an_object_omitting_the_listed_properties(self):
        eq(self, R.omit(['a', 'c', 'f'], self.obj), {'b': 2, 'd': 4, 'e': 5})

    # def test_includes_prototype_properties(self):
    #     F = function(param) {this.x = param}
    #     F.prototype.y = 40 F.prototype.z = 50
    #     self.obj = F(30)
    #     self.obj.v = 10 self.obj.w = 20
    #     eq(self, R.omit(['w', 'x', 'y'], self.obj), {v: 10, z: 50})


if __name__ == '__main__':
    unittest.main()
