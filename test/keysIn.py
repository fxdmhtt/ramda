# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_keysIn(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None, 'f': None}
        # function C() { this.a = 100 this.b = 200 }
        # C.prototype.x = lambda :{ 'x' }
        # C.prototype.y = 'y'
        # cobj = C()

    def test_returns_an_array_of_the_given_objects_keys(self):
        eq(self, sorted(R.keysIn(self.obj)), ['a', 'b', 'c', 'd', 'e', 'f'])

    # def test_includes_the_given_objects_prototype_properties(self):
    #     eq(self, sorted(R.keysIn(cobj)), ['a', 'b', 'x', 'y'])

    def test_works_for_primitives(self):
        result = R.map(lambda val: \
            R.keys(val)
        , [None, None, 55, '', True, False, float('nan'), float('inf'), None, []])
        eq(self, result, R.repeat([], 10))


if __name__ == '__main__':
    unittest.main()
