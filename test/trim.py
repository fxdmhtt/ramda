# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_trim(unittest.TestCase):
    def setUp(self):
        self.test = '\x09\x0A\x0B\x0C\x0D\x20\xA0\u1680\u180E\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000\u2028\u2029\uFEFFHello, World!\x09\x0A\x0B\x0C\x0D\x20\xA0\u1680\u180E\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u202F\u205F\u3000\u2028\u2029\uFEFF'

    def test_trims_a_string(self):
        eq(self, R.trim('     xyz    '), 'xyz')

    # def test_trims_all_ES5_whitespace(self):
    #     eq(self, R.trim(self.test), 'Hello, World!')
    #     eq(self, len(R.trim(self.test)), 13)

    def test_does_not_trim_the_zero_width_space(self):
        eq(self, R.trim('\u200b'), '\u200b')
        eq(self, len(R.trim('\u200b')), 1)

    # if (typeof String.prototype.trim != 'function') {
    #     def test_falls_back_to_a_shim_if_String.prototype.trim_is_not_present(self):
    #         eq(self, R.trim('     xyz    '), 'xyz')
    #         eq(self, R.trim(self.test), 'Hello, World!')
    #         eq(self, len(R.trim(self.test)), 13)
    #         eq(self, R.trim('\u200b'), '\u200b')
    #         eq(self, len(R.trim('\u200b')), 1)
    #     })


if __name__ == '__main__':
    unittest.main()
