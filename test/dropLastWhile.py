# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_dropLastWhile(unittest.TestCase):
    def test_skips_elements_while_the_function_reports_True(self):
        eq(self, R.dropLastWhile(lambda x: x >= 5, [1, 3, 5, 7, 9]), [1, 3])

    def test_returns_an_empty_list_for_an_empty_list(self):
        eq(self, R.dropLastWhile(lambda: False, []), [])
        eq(self, R.dropLastWhile(lambda: True, []), [])

    def test_starts_at_the_right_arg_and_acknowledges_None(self):
        sublist = R.dropLastWhile(lambda x: bool(x), [1, 3, None, 5, 7])
        eq(self, len(sublist), 3)
        eq(self, sublist[0], 1)
        eq(self, sublist[1], 3)
        eq(self, sublist[2], None)

    def test_can_operate_on_strings(self):
        eq(self, R.dropLastWhile(lambda x: x != 'd', 'Ramda'), 'Ramd')

    # def test_can_act_as_a_transducer(self):
    #     dropLt7 = R.dropLastWhile(lambda x:{ x < 7})
    #     eq(self, R.into([], dropLt7, [1, 3, 5, 7, 9, 1, 2]), [1, 3, 5, 7, 9])
    #     eq(self, R.into([], dropLt7, [1, 3, 5]), [])


if __name__ == '__main__':
    unittest.main()
