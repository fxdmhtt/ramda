# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_take(unittest.TestCase):
    def test_takes_only_the_first_n_elements_from_a_list(self):
        eq(self, R.take(3, ['a', 'b', 'c', 'd', 'e', 'f', 'g']), ['a', 'b', 'c'])

    def test_returns_only_as_many_as_the_array_can_provide(self):
        eq(self, R.take(3, [1, 2]), [1, 2])
        eq(self, R.take(3, []), [])

    def test_returns_an_equivalent_list_if_n_is_lt_0(self):
        eq(self, R.take(-1, [1, 2, 3]), [1, 2, 3])
        import sys
        eq(self, R.take(-sys.maxsize, [1, 2, 3]), [1, 2, 3])

    def test_never_returns_the_input_array(self):
        xs = [1, 2, 3]

        self.assertIsNot(R.take(3, xs), xs)
        import sys
        self.assertIsNot(R.take(sys.maxsize, xs), xs)
        self.assertIsNot(R.take(-1, xs), xs)

    def test_can_operate_on_strings(self):
        eq(self, R.take(3, 'Ramda'), 'Ram')
        eq(self, R.take(2, 'Ramda'), 'Ra')
        eq(self, R.take(1, 'Ramda'), 'R')
        eq(self, R.take(0, 'Ramda'), '')

    # def test_handles_zero_correctly_1224(self):
    #     eq(self, R.into([], R.take(0), [1, 2, 3]), [])

    # def test_steps_correct_number_of_times(self):
    #     spy = sinon.spy()
    #     R.into([], R.compose(R.map(spy), R.take(2)), [1, 2, 3])
    #     sinon.assert.calledTwice(spy)

    # def test_transducer_called_for_every_member_of_list_if_n_is_lt_0(self):
    #     spy = sinon.spy()
    #     R.into([], R.compose(R.map(spy), R.take(-1)), [1, 2, 3])
    #     sinon.assert.calledThrice(spy)


if __name__ == '__main__':
    unittest.main()
