# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_map(unittest.TestCase):
    def setUp(self):
        self.times2 = lambda x: x * 2
        self.add1 = lambda x: x + 1
        self.dec = lambda x: x - 1
        # self.intoArray = R.into([])

    def test_maps_simple_functions_over_arrays(self):
        eq(self, R.map(self.times2, [1, 2, 3, 4]), [2, 4, 6, 8])

    # def test_maps_simple_functions_into_arrays(self):
    #     eq(self, self.intoArray(R.map(self.times2), [1, 2, 3, 4]), [2, 4, 6, 8])

    def test_maps_over_objects(self):
        eq(self, R.map(self.dec, {}), {})
        eq(self, R.map(self.dec, {'x': 4, 'y': 5, 'z': 6}), {'x': 3, 'y': 4, 'z': 5})

    def test_interprets_r_as_a_functor(self):
        f = lambda a: a - 1
        g = lambda b: b * 2
        h = R.map(f, g)
        eq(self, h(10), (10 * 2) - 1)

    def test_dispatches_to_objects_that_implement_map(self):
        obj = {'x': 100, 'map': lambda f: f(100)}
        eq(self, R.map(self.add1, obj), 101)

    # def test_dispatches_to_transformer_objects(self):
    #     eq(self, R.map(self.add1, listXf), {
    #         f: self.add1,
    #         xf: listXf
    #     })

    def test_throws_a_TypeError_on_None_and_None(self):
        with self.assertRaises(TypeError):
            R.map(self.times2, None)

    def test_composes(self):
        mdouble = R.map(self.times2)
        mdec = R.map(self.dec)
        eq(self, mdec(mdouble([10, 20, 30])), [19, 39, 59])

    # def test_can_compose_transducer_style(self):
    #     mdouble = R.map(self.times2)
    #     mdec = R.map(self.dec)
    #     xcomp = mdec(mdouble(listXf))
    #     eq(self, xcomp.xf, {xf: listXf, f: self.times2})
    #     eq(self, xcomp.f, self.dec)

    # def test_correctly_uses_fantasy_land_implementations(self):
    #     m1 = Id(1)
    #     m2 = R.map(R.add(1), m1)

    #     eq(self, m1.value + 1, m2.value)


if __name__ == '__main__':
    unittest.main()
