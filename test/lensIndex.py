# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

testList = [{'a': 1}, {'b': 2}, {'c': 3}]

class Test_lensIndex(unittest.TestCase):
    class Test_view(unittest.TestCase):
        def test_focuses_list_element_at_the_specified_index(self):
            eq(self, R.view(R.lensIndex(0), testList), {a: 1})
    
        def test_returns_None_if_the_specified_index_does_not_exist(self):
            eq(self, R.view(R.lensIndex(10), testList), None)
    

    class Test_set(unittest.TestCase):
        def test_sets_the_list_value_at_the_specified_index(self):
            eq(self, R.set(R.lensIndex(0), 0, testList), [0, {b: 2}, {c: 3}])
    

    class Test_over(unittest.TestCase):
        def test_applies_function_to_the_value_at_the_specified_list_index(self):
            eq(self, R.over(R.lensIndex(2), R.keys, testList), [{a: 1}, {b: 2}, ['c']])
    

    class Test_composability(unittest.TestCase):
        def test_can_be_composed(self):
            nestedList = [0, [10, 11, 12], 1, 2]
            composedLens = R.compose(R.lensIndex(1), R.lensIndex(0))

            eq(self, R.view(composedLens, nestedList), 10)
    

    class Test_well behaved lens(unittest.TestCase):
        def test_set_s_(get_s)_==_s(self):
            eq(self, R.set(R.lensIndex(0), R.view(R.lensIndex(0), testList), testList), testList)
    
        def test_get_(set_s_v)_==_v(self):
            eq(self, R.view(R.lensIndex(0), R.set(R.lensIndex(0), 0, testList)), 0)
    
        def test_get_(set(set_s_v1)_v2)_==_v2(self):
            eq(self, 
                R.view(R.lensIndex(0), R.set(R.lensIndex(0), 11, R.set(R.lensIndex(0), 10, testList))),
                11
            )


if __name__ == '__main__':
    unittest.main()
