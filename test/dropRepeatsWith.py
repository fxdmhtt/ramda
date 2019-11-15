# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_dropRepeatsWith(unittest.TestCase):
    def setUp(self):
        self.objs = [
            {'i': 1}, {'i': 2}, {'i': 3}, {'i': 4}, {'i': 5}, {'i': 3}
        ]
        self.objs2 = [
            {'i': 1}, {'i': 1}, {'i': 1}, {'i': 2}, {'i': 3},
            {'i': 3}, {'i': 4}, {'i': 4}, {'i': 5}, {'i': 3}
        ]
        self.eqI = R.eqProps('i')

    def test_removes_repeated_elements_based_on_predicate(self):
        eq(self, R.dropRepeatsWith(self.eqI, self.objs2), self.objs)
        eq(self, R.dropRepeatsWith(self.eqI, self.objs), self.objs)

    def test_keeps_elements_from_the_left(self):
        eq(self, 
            R.dropRepeatsWith(self.eqI, [{'i': 1, 'n': 1}, {'i': 1, 'n': 2}, {'i': 1, 'n': 3}, {'i': 4, 'n': 1}, {'i': 4, 'n': 2}]),
            [{'i': 1, 'n': 1}, {'i': 4, 'n': 1}]
        )

    def test_returns_an_empty_array_for_an_empty_array(self):
        eq(self, R.dropRepeatsWith(self.eqI, []), [])

    # def test_can_act_as_a_transducer(self):
    #     eq(self, R.into([], R.dropRepeatsWith(self.eqI), self.objs2), self.objs)


if __name__ == '__main__':
    unittest.main()
