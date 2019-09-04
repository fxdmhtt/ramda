# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

testObj = {
    'a': 1,
    'b': 2,
    'c': 3
}

class Test_lensProp(unittest.TestCase):
    class Test_view(unittest.TestCase):
        def test_focuses_object_the_specified_object_property(self):
            eq(self, R.view(R.lensProp('a'), testObj), 1)
    
        def test_returns_None_if_the_specified_property_does_not_exist(self):
            eq(self, R.view(R.lensProp('X'), testObj), None)
    

    class Test_set(unittest.TestCase):
        def test_sets_the_value_of_the_object_property_specified(self):
            eq(self, R.set(R.lensProp('a'), 0, testObj), {a:0, b:2, c:3})
    
        def test_adds_the_property_to_the_object_if_it_doesn_'t_exist(self):
            eq(self, R.set(R.lensProp('d'), 4, testObj), {a:1, b:2, c:3, d:4})
    

    class Test_over(unittest.TestCase):
        def test_applies_function_to_the_value_of_the_specified_object_property(self):
            eq(self, R.over(R.lensProp('a'), R.inc, testObj), {a:2, b:2, c:3})
    
        def test_applies_function_to_None_and_adds_the_property_if_it_doesn_'t_exist(self):
            eq(self, R.over(R.lensProp('X'), R.identity, testObj), {a:1, b:2, c:3, X:None})
    

    class Test_composability(unittest.TestCase):
        def test_can_be_composed(self):
            nestedObj = {a: {b: 1}, c:2}
            composedLens = R.compose(R.lensProp('a'), R.lensProp('b'))

            eq(self, R.view(composedLens, nestedObj), 1)
    

    class Test_well behaved lens(unittest.TestCase):
        def test_set_s_(get_s)_==_s(self):
            eq(self, R.set(R.lensProp('a'), R.view(R.lensProp('a'), testObj), testObj), testObj)
    
        def test_get_(set_s_v)_==_v(self):
            eq(self, R.view(R.lensProp('a'), R.set(R.lensProp('a'), 0, testObj)), 0)
    
        def test_get_(set(set_s_v1)_v2)_==_v2(self):
            eq(self, 
                R.view(R.lensProp('a'), R.set(R.lensProp('a'), 11, R.set(R.lensProp('a'), 10, testObj))),
                11
            )


if __name__ == '__main__':
    unittest.main()
