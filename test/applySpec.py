# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_applySpec(unittest.TestCase):
    def test_works_with_empty_spec(self):
        eq(self, R.applySpec({})(), {})

    def test_works_with_unary_functions(self):
        eq(self, R.applySpec({ 'v': R.inc, 'u': R.dec })(1), { 'v': 2, 'u': 0 })

    def test_works_with_binary_functions(self):
        eq(self, R.applySpec({ 'sum': R.add })(1, 2), { 'sum': 3 })

    def test_works_with_nested_specs(self):
        eq(self, R.applySpec({ 'unnested': R.always(0), 'nested': { 'sum': R.add } })(1, 2),
            { 'unnested': 0, 'nested': { 'sum': 3 } }
        )

    def test_works_with_arrays_of_nested_specs(self):
        eq(self, R.applySpec({ 'unnested': R.always(0), 'nested':[{ 'sum': R.add }] })(1, 2),
            { 'unnested': 0, 'nested': [{ 'sum': 3 }] }
        )

    def test_works_with_arrays_of_spec_objects(self):
        eq(self, R.applySpec([{ 'sum': R.add }])(1, 2),
            [{ 'sum': 3 }]
        )

    def test_works_with_arrays_of_functions(self):
        eq(self, R.applySpec([R.map(R.prop('a')), R.map(R.prop('b'))])([
            {'a': 'a1', 'b': 'b1'}, {'a': 'a2', 'b': 'b2'}
        ]),
        [['a1', 'a2'], ['b1', 'b2']])

    def test_works_with_a_spec_defining_a_map_key(self):
        eq(self, R.applySpec({'map': R.prop('a')})({'a': 1}), {'map': 1})

    def test_retains_the_highest_arity(self):
        f = R.applySpec({ 'f1': R.nAry(2, R.T), 'f2': R.nAry(5, R.T) })
        eq(self, f.length, 5)

    def test_returns_a_curried_function(self):
        eq(self, R.applySpec({ 'sum': R.add })(1)(2), { 'sum': 3 })


if __name__ == '__main__':
    unittest.main()
