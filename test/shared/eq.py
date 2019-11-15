# -*- coding: utf-8 -*-

import ramda as R

def eq(self, actual, expected):
    self.assertEqual(R.toString(actual), R.toString(expected))
