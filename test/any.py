# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_any(unittest.TestCase):
    def setUp(self):
        self.odd = lambda n: n % 2 == 1
        self.T = lambda: True
        # self.intoArray = R.into([])

    def test_returns_True_if_any_element_satisfies_the_predicate(self):
        eq(self, R.any(self.odd, [2, 4, 6, 8, 10, 11, 12]), True)

    def test_returns_False_if_all_elements_fails_to_satisfy_the_predicate(self):
        eq(self, R.any(self.odd, [2, 4, 6, 8, 10, 12]), False)

    # def test_returns_True_into_array_if_any_element_satisfies_the_predicate(self):
    #     eq(self, self.intoArray(R.any(self.odd), [2, 4, 6, 8, 10, 11, 12]), [True])

    # def test_returns_False_if_all_elements_fails_to_satisfy_the_predicate(self):
    #     eq(self, self.intoArray(R.any(self.odd), [2, 4, 6, 8, 10, 12]), [False])

    def test_works_with_more_complex_objects(self):
        people = [{'first': 'Paul', 'last': 'Grenier'}, {'first':'Mike', 'last': 'Hurley'}, {'first': 'Will', 'last': 'Klein'}]
        alliterative = lambda person: person['first'][0] == person['last'][0]
        eq(self, R.any(alliterative, people), False)
        people.append({'first': 'Scott', 'last': 'Sauyet'})
        eq(self, R.any(alliterative, people), True)

    def test_can_use_a_configurable_function(self):
        teens = [{'name': 'Alice', 'age': 14}, {'name': 'Betty', 'age': 18}, {'name': 'Cindy', 'age': 17}]
        atLeast = lambda age: lambda person: person['age'] >= age
        eq(self, R.any(atLeast(16), teens), True)
        eq(self, R.any(atLeast(21), teens), False)

    def test_returns_False_for_an_empty_list(self):
        eq(self, R.any(self.T, []), False)

    # def test_returns_False_into_array_for_an_empty_list(self):
    #     eq(self, self.intoArray(R.any(self.T), []), [False])

    # def test_dispatches_when_given_a_transformer_in_list_position(self):
    #     eq(self, R.any(self.odd, listXf), {
    #         any: False,
    #         f: self.odd,
    #         xf: listXf
    #     })


if __name__ == '__main__':
    unittest.main()
