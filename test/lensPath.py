# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

testObj = {
    'a': [{
        'b': 1
    }, {
        'b': 2
    }],
    'd': 3
}

class Test_lensPath(unittest.TestCase):
    class Test_view(unittest.TestCase):
        def test_focuses_the_specified_object_property(self):
            eq(self, R.view(R.lensPath(['d']), testObj), 3)
            eq(self, R.view(R.lensPath(['a', 1, 'b']), testObj), 2)
            eq(self, R.view(R.lensPath([]), testObj), testObj)
    

    class Test_set(unittest.TestCase):
        def test_sets_the_value_of_the_object_property_specified(self):
            eq(self, R.set(R.lensPath(['d']), 0, testObj), {a: [{b: 1}, {b: 2}], d: 0})
            eq(self, R.set(R.lensPath(['a', 0, 'b']), 0, testObj), {a: [{b: 0}, {b: 2}], d: 3})
            eq(self, R.set(R.lensPath([]), 0, testObj), 0)
    
        def test_adds_the_property_to_the_object_if_it_doesn_'t_exist(self):
            eq(self, R.set(R.lensPath(['X']), 0, testObj), {a: [{b: 1}, {b: 2}], d: 3, X: 0})
            eq(self, R.set(R.lensPath(['a', 0, 'X']), 0, testObj), {a: [{b: 1, X: 0}, {b: 2}], d: 3})
    

    class Test_over(unittest.TestCase):
        def test_applies_function_to_the_value_of_the_specified_object_property(self):
            eq(self, R.over(R.lensPath(['d']), R.inc, testObj), {a: [{b: 1}, {b: 2}], d: 4})
            eq(self, R.over(R.lensPath(['a', 1, 'b']), R.inc, testObj), {a: [{b: 1}, {b: 3}], d: 3})
            eq(self, R.over(R.lensPath([]), R.toPairs, testObj), [['a', [{b: 1}, {b: 2}]], ['d', 3]])
    
        def test_applies_function_to_None_and_adds_the_property_if_it_doesn_'t_exist(self):
            eq(self, R.over(R.lensPath(['X']), R.identity, testObj), {a: [{b: 1}, {b: 2}], d: 3, X: None})
            eq(self, R.over(R.lensPath(['a', 0, 'X']), R.identity, testObj), {a: [{b: 1, X: None}, {b: 2}], d: 3})
    

    class Test_composability(unittest.TestCase):
        def test_can_be_composed(self):
            composedLens = R.compose(R.lensPath(['a']), R.lensPath([1, 'b']))
            eq(self, R.view(composedLens, testObj), 2)
    

    class Test_well behaved lens(unittest.TestCase):
        def test_set_s_(get_s)_==_s(self):
            eq(self, R.set(R.lensPath(['d']), R.view(R.lensPath(['d']), testObj), testObj), testObj)
            eq(self, R.set(R.lensPath(['a', 0, 'b']), R.view(R.lensPath(['a', 0, 'b']), testObj), testObj), testObj)
    
        def test_get_(set_s_v)_==_v(self):
            eq(self, R.view(R.lensPath(['d']), R.set(R.lensPath(['d']), 0, testObj)), 0)
            eq(self, R.view(R.lensPath(['a', 0, 'b']), R.set(R.lensPath(['a', 0, 'b']), 0, testObj)), 0)
    
        def test_get_(set(set_s_v1)_v2)_==_v2(self):
            p = ['d']
            q = ['a', 0, 'b']
            eq(self, R.view(R.lensPath(p), R.set(R.lensPath(p), 11, R.set(R.lensPath(p), 10, testObj))), 11)
            eq(self, R.view(R.lensPath(q), R.set(R.lensPath(q), 11, R.set(R.lensPath(q), 10, testObj))), 11)


if __name__ == '__main__':
    unittest.main()
