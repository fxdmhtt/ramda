# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_indexOf(unittest.TestCase):
    def test_returns_a_number_indicating_an_objects_position_in_a_list(self):
        list = [0, 10, 20, 30]
        eq(self, R.indexOf(30, list), 3)

    def test_returns__1_if_the_object_is_not_in_the_list(self):
        list = [0, 10, 20, 30]
        eq(self, R.indexOf(40, list), -1)

    def test_returns_the_index_of_the_first_item(self):
        input = [1, 2, 3, 4, 5]
        eq(self, R.indexOf(1, input), 0)

    def test_returns_the_index_of_the_last_item(self):
        input = [1, 2, 3, 4, 5]
        eq(self, R.indexOf(5, input), 4)

    def test_finds_1(self):
        list = [1, 2, 3]
        eq(self, R.indexOf(1, list), 0)

    def test_finds_1_and_is_result_strictly_it(self):
        list = [1, 2, 3]
        eq(self, R.indexOf(1, list), 0)

    def test_does_not_find_4(self):
        list = [1, 2, 3]
        eq(self, R.indexOf(4, list), -1)

    def test_does_not_consider_1_equal_to_1(self):
        list = [1, 2, 3]
        eq(self, R.indexOf('1', list), -1)

    def test_returns__1_for_an_empty_array(self):
        eq(self, R.indexOf('x', []), -1)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.indexOf(0, [-0]), -1)
    #     eq(self, R.indexOf(-0, [0]), -1)
    #     eq(self, R.indexOf(NaN, [NaN]), 0)
    #     eq(self, R.indexOf(Just([42]), [Just([42])]), 0)

    def test_dispatches_to_indexOf_method(self):
        class Empty:
            def indexOf(self, *_):
                return R.always(-1)()

        class List:
            def __init__(self, head, tail):
                self.head = head
                self.tail = tail

            def indexOf(self, x):
                idx = self.tail.indexOf(x)
                return 0 if self.head == x else 1 + idx if idx >= 0 else -1

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

        eq(self, R.indexOf('a', 'banana'), 1)
        eq(self, R.indexOf('x', 'banana'), -1)
        eq(self, R.indexOf('a', list), 1)
        eq(self, R.indexOf('x', list), -1)

    def test_finds_function_compared_by_identity(self):
        f = lambda *_: None
        g = lambda *_: None
        list = [g, f, g, f]
        eq(self, R.indexOf(f, list), 1)

    def test_does_not_find_function_compared_by_identity(self):
        f = lambda *_: None
        g = lambda *_: None
        h = lambda *_: None
        list = [g, f]
        eq(self, R.indexOf(h, list), -1)


if __name__ == '__main__':
    unittest.main()
