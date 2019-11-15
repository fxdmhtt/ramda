# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_lastIndexOf(unittest.TestCase):
    def test_returns_a_number_indicating_an_objects_last_position_in_a_list(self):
        list = [0, 10, 20, 30, 0, 10, 20, 30, 0, 10]
        eq(self, R.lastIndexOf(30, list), 7)

    def test_returns__1_if_the_object_is_not_in_the_list(self):
        list = [0, 10, 20, 30]
        eq(self, R.lastIndexOf(40, list), -1)

    def test_returns_the_last_index_of_the_first_item(self):
        input = [1, 2, 3, 4, 5, 1]
        eq(self, R.lastIndexOf(1, input), 5)

    def test_returns_the_index_of_the_last_item(self):
        input = [1, 2, 3, 4, 5, 1]
        eq(self, R.lastIndexOf(5, input), 4)

    def test_finds_a(self):
        list = ['a', 1, 'a']
        eq(self, R.lastIndexOf('a', list), 2)

    def test_does_not_find_c(self):
        list = ['a', 1, 'a']
        eq(self, R.lastIndexOf('c', list), -1)

    def test_does_not_consider_1_equal_to_1(self):
        list = ['a', 1, 'a']
        eq(self, R.lastIndexOf('1', list), -1)

    def test_returns__1_for_an_empty_array(self):
        eq(self, R.lastIndexOf('x', []), -1)


    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.lastIndexOf(0, [-0]), -1)
    #     eq(self, R.lastIndexOf(-0, [0]), -1)
    #     eq(self, R.lastIndexOf(NaN, [NaN]), 0)
    #     eq(self, R.lastIndexOf(Just([42]), [Just([42])]), 0)


    def test_dispatches_to_lastIndexOf_method(self):
        class Empty:
            def lastIndexOf(self, *_):
                return R.always(-1)()

        class List:
            def __init__(self, head, tail):
                self.head = head
                self.tail = tail

            def lastIndexOf(self, x):
                idx = self.tail.lastIndexOf(x)
                return 1 + idx if idx >= 0 else 0 if self.head == x else -1

        list = List('b',
            List('a',
                List('n',
                    List('a',
                        List('n',
                            List('a',
                                Empty()
                            )
                        )
                    )
                )
            )
        )

        eq(self, R.lastIndexOf('a', 'banana'), 5)
        eq(self, R.lastIndexOf('x', 'banana'), -1)
        eq(self, R.lastIndexOf('a', list), 5)
        eq(self, R.lastIndexOf('x', list), -1)

    def test_finds_function_compared_by_identity(self):
        f = lambda *_: None
        g = lambda *_: None
        list = [g, f, g, f]
        eq(self, R.lastIndexOf(f, list), 3)

    def test_does_not_find_function_compared_by_identity(self):
        f = lambda *_: None
        g = lambda *_: None
        h = lambda *_: None
        list = [g, f]
        eq(self, R.lastIndexOf(h, list), -1)


if __name__ == '__main__':
    unittest.main()
