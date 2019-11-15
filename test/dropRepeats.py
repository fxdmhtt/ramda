# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_dropRepeats(unittest.TestCase):
    def setUp(self):
        self.objs = [1, 2, 3, 4, 5, 3, 2]
        self.objs2 = [1, 2, 2, 2, 3, 4, 4, 5, 5, 3, 2, 2]

    def test_removes_repeated_elements(self):
        eq(self, R.dropRepeats(self.objs2), self.objs)
        eq(self, R.dropRepeats(self.objs), self.objs)

    def test_returns_an_empty_array_for_an_empty_array(self):
        eq(self, R.dropRepeats([]), [])

    # def test_can_act_as_a_transducer(self):
    #     eq(self, R.into([], R.dropRepeats, self.objs2), self.objs)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.dropRepeats([0, -0]).length, 2)
    #     eq(self, R.dropRepeats([-0, 0]).length, 2)
    #     eq(self, R.dropRepeats([NaN, NaN]).length, 1)
    #     eq(self, R.dropRepeats([Just([42]), Just([42])]).length, 1)


if __name__ == '__main__':
    unittest.main()
