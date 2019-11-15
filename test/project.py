# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_project(unittest.TestCase):
    def setUp(self):
        self.kids = [
            {'name': 'Abby', 'age': 7, 'hair': 'blond'},
            {'name': 'Fred', 'age': 12, 'hair': 'brown'},
            {'name': 'Rusty', 'age': 10, 'hair': 'brown'},
            {'name': 'Alois', 'age': 15, 'disposition': 'surly'}
        ]

    def test_selects_the_chosen_properties_from_each_element_in_a_list(self):
        eq(self, R.project(['name', 'age'], self.kids), [
            {'name': 'Abby', 'age': 7},
            {'name': 'Fred', 'age': 12},
            {'name': 'Rusty', 'age': 10},
            {'name': 'Alois', 'age': 15}
        ])

    def test_has_an_None_property_on_the_output_tuple_for_any_input_tuple_that_does_not_have_the_property(self):
        eq(self, R.project(['name', 'hair'], self.kids), [
            {'name': 'Abby', 'hair': 'blond'},
            {'name': 'Fred', 'hair': 'brown'},
            {'name': 'Rusty', 'hair': 'brown'},
            {'name': 'Alois', 'hair': None}
        ])


if __name__ == '__main__':
    unittest.main()
