# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_forEach(unittest.TestCase):
    def setUp(self):
        self.list = [{'x': 1, 'y': 2}, {'x': 100, 'y': 200}, {'x': 300, 'y': 400}, {'x': 234, 'y': 345}]

    def test_performs_the_passed_in_function_on_each_element_of_the_list(self):
        sideEffect = {}
        def function(elem):
            sideEffect[elem['x']] = elem['y']
        R.forEach(function, self.list)
        eq(self, sideEffect, {1: 2, 100: 200, 300: 400, 234: 345})

    def test_returns_the_original_list(self):
        s = ''
        def function(obj):
            nonlocal s
            s += str(obj['x'])
        eq(self, R.forEach(function, self.list), self.list)
        eq(self, '1100300234', s)

    def test_handles_empty_list(self):
        eq(self, R.forEach(lambda x: x * x, []), [])

    def test_dispatches_to_forEach_method(self):
        dispatched = False
        fn = lambda *_: None
        class DummyList:
            def forEach(self, callback):
                nonlocal dispatched
                dispatched = True
                assert callback is fn
        R.forEach(fn, DummyList())
        eq(self, dispatched, True)


if __name__ == '__main__':
    unittest.main()
