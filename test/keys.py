# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_keys(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 100, 'b': [1, 2, 3], 'c': {'x': 200, 'y': 300}, 'd': 'D', 'e': None, 'f': None}
        # function C() { this.a = 100 this.b = 200 }
        # C.prototype.x = lambda :{ 'x' }
        # C.prototype.y = 'y'
        # cobj = C()

    def test_returns_an_array_of_the_given_objects_own_keys(self):
        self.assertSequenceEqual(sorted(R.keys(self.obj)), ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_works_with_hasOwnProperty_override(self):
        self.assertSequenceEqual(R.keys({
            'hasOwnProperty': False
        }), ['hasOwnProperty'])

    def test_works_for_primitives(self):
        result = R.map(lambda val: \
            R.keys(val)
        , [None, None, 55, '', True, False, float('nan'), float('inf'), None, []])
        self.assertSequenceEqual(result, list(R.repeat([], 10)))

    # def test_does_not_include_the_given_objects_prototype_properties(self):
    #     self.assertSequenceEqual(R.keys(self.cobj).sort(), ['a', 'b'])


if __name__ == '__main__':
    unittest.main()
