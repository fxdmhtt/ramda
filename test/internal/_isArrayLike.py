# -*- coding: utf-8 -*-

from ramda.internal._isArrayLike import _isArrayLike

import unittest

class Test_isArrayLike(unittest.TestCase):
    def test_is_true_for_Arrays(self):
        self.assertEqual(_isArrayLike([]), True)
        self.assertEqual(_isArrayLike([1, 2, 3, 4]), True)
        self.assertEqual(_isArrayLike([None]), True)

    def test_is_true_for_arguments(self):
        def test(*arguments):
            return _isArrayLike(arguments)
        self.assertEqual(test(), True)
        self.assertEqual(test(1, 2, 3), True)
        self.assertEqual(test(None), True)

    def test_is_false_for_Strings(self):
        self.assertEqual(_isArrayLike(''), False)
        self.assertEqual(_isArrayLike('abcdefg'), False)

    def test_is_true_for_arbitrary_objects_with_numeric_length(self):
        obj1 = {'length': 0}
        obj2 = {0: 'something', 'length': 0}
        obj3 = {0: 0, 'length': 0}
        obj4 = {0: 'zero', 1: 'one', 'length': 2}
        obj5 = {0: 'zero', 'length': 2}
        obj6 = {1: 'one', 'length': 2}
        self.assertEqual(_isArrayLike(obj1), True)
        self.assertEqual(_isArrayLike(obj2), True)
        self.assertEqual(_isArrayLike(obj3), True)
        self.assertEqual(_isArrayLike(obj4), True)
        self.assertEqual(_isArrayLike(obj5), False)
        self.assertEqual(_isArrayLike(obj6), False)

    def test_is_false_for_everything_else(self):
        self.assertEqual(_isArrayLike(None), False)
        self.assertEqual(_isArrayLike(1), False)
        self.assertEqual(_isArrayLike({}), False)
        self.assertEqual(_isArrayLike(False), False)
        self.assertEqual(_isArrayLike(lambda: {}), False)


if __name__ == '__main__':
    unittest.main()
