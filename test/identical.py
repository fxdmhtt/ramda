# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_identical(unittest.TestCase):
    def setUp(self):
        self.a = []
        self.b = self.a

    def test_has_Object_is_semantics(self):
        eq(self, R.identical(100, 100), True)
        eq(self, R.identical(100, '100'), False)
        eq(self, R.identical('string', 'string'), True)
        eq(self, R.identical([], []), False)
        eq(self, R.identical(self.a, self.b), True)
        eq(self, R.identical(None, None), True)

        eq(self, R.identical(-0, 0), True)
        eq(self, R.identical(0, -0), True)
        eq(self, R.identical(float('nan'), float('nan')), True)

        eq(self, R.identical(float('nan'), 42), False)
        eq(self, R.identical(42, float('nan')), False)

        eq(self, R.identical(0, 0.0), False)
        eq(self, R.identical(0.0, 0), False)


if __name__ == '__main__':
    unittest.main()
