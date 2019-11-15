# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_apply(unittest.TestCase):
    def test_applies_function_to_argument_list(self):
        eq(self, R.apply(max, [1, 2, 3, -99, 42, 6, 7]), 42)

    # def test_provides_no_way_to_specify_context(self):
    #     obj = {'method': lambda *, this=None: this == obj}
    #     eq(self, R.apply(obj['method'], []), False)
    #     eq(self, R.apply(R.bind(obj['method'], obj), []), True)


if __name__ == '__main__':
    unittest.main()
