# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_mergeAll(unittest.TestCase):
    def test_merges_a_list_of_objects_together_into_one_object(self):
        eq(self, R.mergeAll([{'foo':1}, {'bar':2}, {'baz':3}]), {'foo':1, 'bar':2, 'baz':3})

    def test_gives_precedence_to_later_objects_in_the_list(self):
        eq(self, R.mergeAll([{'foo':1}, {'foo':2}, {'bar':2}]), {'foo':2, 'bar':2})

    # def test_ignores_inherited_properties(self):
    #     function Foo() {}
    #     Foo.prototype.bar = 42
    #     foo = Foo()
    #     res = R.mergeAll([foo, {fizz: 'buzz'}])
    #     eq(res, {fizz: 'buzz'})


if __name__ == '__main__':
    unittest.main()
