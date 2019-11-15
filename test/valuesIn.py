# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_valuesIn(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None, 'f': None}
        # function C() { this.a = 100 this.b = 200 }
        # C.prototype.x = lambda :{ 'x' }
        # C.prototype.y = 'y'
        # cobj = C()

    def test_returns_an_array_of_the_given_objects_values(self):
        vs = list(R.valuesIn(self.obj))
        eq(self, len(vs), 6)
        eq(self, R.indexOf(100, vs) >= 0, True)
        eq(self, R.indexOf('D', vs) >= 0, True)
        eq(self, R.indexOf(None, vs) >= 0, True)
        eq(self, R.indexOf(None, vs) >= 0, True)
        eq(self, R.indexOf(self.obj['b'], vs) >= 0, True)
        eq(self, R.indexOf(self.obj['c'], vs) >= 0, True)

    # def test_includes_the_given_objects_prototype_properties(self):
    #     vs = R.valuesIn(cobj)
    #     eq(self, len(vs), 4)
    #     eq(self, R.indexOf(100, vs) >= 0, True)
    #     eq(self, R.indexOf(200, vs) >= 0, True)
    #     eq(self, R.indexOf(cobj.x, vs) >= 0, True)
    #     eq(self, R.indexOf('y', vs) >= 0, True)

    def test_works_for_primitives(self):
        result = R.map(lambda val: \
            list(R.valuesIn(val))
        , [None, None, 55, '', True, False, float('nan'), float('inf'), None, []])
        eq(self, result, list(R.repeat([], 10)))


if __name__ == '__main__':
    unittest.main()
