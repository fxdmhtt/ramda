# -*- coding: utf-8 -*-

__package__ = 'ramda.test.internal'

from ..shared.eq import eq
from ...source.internal._isArrayLike import _isArrayLike

import unittest

class Test_isArrayLike(unittest.TestCase):
    def test_is_true_for_Arrays(self):
        eq(self, _isArrayLike([]), True)
        eq(self, _isArrayLike([1, 2, 3, 4]), True)
        eq(self, _isArrayLike([None]), True)

    def test_is_true_for_arguments(self):
        def test(*arguments):
            return _isArrayLike(arguments)
        eq(self, test(), True)
        eq(self, test(1, 2, 3), True)
        eq(self, test(None), True)

    def test_is_false_for_Strings(self):
        eq(self, _isArrayLike(''), False)
        eq(self, _isArrayLike('abcdefg'), False)

    def test_is_true_for_arbitrary_objects_with_numeric_length(self):
        obj1 = {'length': 0}
        obj2 = {0: 'something', 'length': 0}
        obj3 = {0: 0, 'length': 0}
        obj4 = {0: 'zero', 1: 'one', 'length': 2}
        obj5 = {0: 'zero', 'length': 2}
        obj6 = {1: 'one', 'length': 2}
        eq(self, _isArrayLike(obj1), True)
        eq(self, _isArrayLike(obj2), True)
        eq(self, _isArrayLike(obj3), True)
        eq(self, _isArrayLike(obj4), True)
        eq(self, _isArrayLike(obj5), False)
        eq(self, _isArrayLike(obj6), False)

    def test_is_false_for_everything_else(self):
        eq(self, _isArrayLike(None), False)
        eq(self, _isArrayLike(1), False)
        eq(self, _isArrayLike({}), False)
        eq(self, _isArrayLike(False), False)
        eq(self, _isArrayLike(lambda: {}), False)


if __name__ == '__main__':
    unittest.main()
