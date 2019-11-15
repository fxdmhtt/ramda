# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_unfold(unittest.TestCase):
    def test_unfolds_simple_functions_with_a_starting_point_to_create_a_list(self):
        self.assertSequenceEqual(list(R.unfold(lambda n: [n, n - 1] if n > 0 else None, 10)), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_is_cool(self):
        def fib(n):
            count = 0
            def function(pair):
                nonlocal count
                count += 1
                if count <= n:
                    return [pair[0], [pair[1], pair[0] + pair[1]]]
            return function
        self.assertSequenceEqual(list(R.unfold(fib(10), [0, 1])), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == '__main__':
    unittest.main()
