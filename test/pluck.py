# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_pluck(unittest.TestCase):
    def setUp(self):
        self.people = [
            {'name': 'Fred', 'age': 23},
            {'name': 'Wilma', 'age': 21},
            {'name': 'Pebbles', 'age': 2}
        ]

    def test_returns_a_function_that_maps_the_appropriate_property_over_an_array(self):
        nm = R.pluck('name')
        self.assertTrue(callable(nm))
        eq(self, nm(self.people), ['Fred', 'Wilma', 'Pebbles'])

    # def test_behaves_as_a_transducer_when_given_a_transducer_in_list_position(self):
    #     numbers = [{a: 1}, {a: 2}, {a: 3}, {a: 4}]
    #     transducer = R.compose(R.pluck('a'), R.map(R.add(1)), R.take(2))
    #     eq(self, R.transduce(transducer, R.flip(R.append), [], numbers), [2, 3])


if __name__ == '__main__':
    unittest.main()
