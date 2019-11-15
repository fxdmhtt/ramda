# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
from datetime import timedelta

class Test_add(unittest.TestCase):
    def test_adds_together_two_numbers(self):
        eq(self, R.add(3, 7), 10)

    def test_coerces_its_arguments_to_numbers(self):
        eq(self, R.add('1', '2'), '12')
        # eq(self, R.add(1, '2'), 3)
        eq(self, R.add(True, False), 1)
        eq(self, R.add(float('nan'), float('nan')), float('nan'))
        eq(self, R.add(timedelta(1), timedelta(2)), timedelta(3))


if __name__ == '__main__':
    unittest.main()
