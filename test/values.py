# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_values(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None, 'f': None}
        # function C() { this.a = 100 this.b = 200 }
        # C.prototype.x = 'lambda':{ 'x' }
        # C.prototype.y = 'y'
        # cobj = C()

    # def test_returns_an_array_of_the_given_objects_values(self):
    #     vs = sorted(R.values(self.obj))
    #     ts = [[1, 2, 3], 100, 'D', {'x': 200, 'y': 300}, None, None]
    #     eq(self, vs.length, ts.length)
    #     eq(self, vs[0], ts[0])
    #     eq(self, vs[1], ts[1])
    #     eq(self, vs[2], ts[2])
    #     eq(self, vs[3], ts[3])
    #     eq(self, vs[4], ts[4])
    #     eq(self, vs[5], ts[5])

    #     eq(self, R.values({
    #         'hasOwnProperty': False
    #     }), [False])

    # def test_does_not_include_the_given_objects_prototype_properties(self):
    #     eq(self, R.values(cobj), [100, 200])

    def test_returns_an_empty_object_for_primitives(self):
        result = R.map(lambda val: \
            R.keys(val)
        , [None, None, 55, '', True, False, float('nan'), float('inf'), None, []])
        eq(self, result, R.repeat([], 10))


if __name__ == '__main__':
    unittest.main()
