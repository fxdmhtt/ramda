# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_call(unittest.TestCase):
    def test_returns_the_result_of_calling_its_first_argument_with_the_remaining_arguments(self):
        eq(self, R.call(max, 1, 2, 3, -99, 42, 6, 7), 42)

    def test_accepts_one_or_more_arguments(self):
        fn = lambda *arguments: len(arguments)
        eq(self, R.call(fn), 0)
        eq(self, R.call(fn, 'x'), 1)
        eq(self, R.call(fn, 'x', 'y'), 2)
        eq(self, R.call(fn, 'x', 'y', 'z'), 3)

    # def test_provides_no_way_to_specify_context(self):
    #     obj = {'method': lambda self: self == obj}
    #     eq(self, R.call(obj['method']), False)
    #     eq(self, R.call(R.bind(obj['method'], obj)), True)


if __name__ == '__main__':
    unittest.main()
