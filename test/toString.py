# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_toString(unittest.TestCase):
    def test_returns_the_string_representation_of_None(self):
        self.assertEqual(R.toString(None), 'None')

    def test_returns_the_string_representation_of_None(self):
        self.assertEqual(R.toString(None), 'None')

    def test_returns_the_string_representation_of_a_Boolean_primitive(self):
        self.assertEqual(R.toString(True), 'True')
        self.assertEqual(R.toString(False), 'False')

    def test_returns_the_string_representation_of_a_number_primitive(self):
        self.assertEqual(R.toString(0), '0')
        # self.assertEqual(R.toString(-0), '-0')
        self.assertEqual(R.toString(1.23), '1.23')
        self.assertEqual(R.toString(-1.23), '-1.23')
        self.assertEqual(R.toString(1e+23), '1e+23')
        self.assertEqual(R.toString(-1e+23), '-1e+23')
        self.assertEqual(R.toString(1e-23), '1e-23')
        self.assertEqual(R.toString(-1e-23), '-1e-23')
        self.assertEqual(R.toString(float('inf')), 'inf')
        self.assertEqual(R.toString(-float('inf')), '-inf')
        self.assertEqual(R.toString(float('nan')), 'nan')

    # def test_returns_the_string_representation_of_a_string_primitive(self):
    #     self.assertEqual(R.toString('abc'), "'abc'")
    #     self.assertEqual(R.toString('x "y" z'), '"x \\"y\\" z"')
    #     self.assertEqual(R.toString("' '"), '"\' \'"')
    #     self.assertEqual(R.toString('" "'), '"\\" \\""')
    #     self.assertEqual(R.toString('\b \b'), '"\\b \\b"')
    #     self.assertEqual(R.toString('\f \f'), '"\\f \\f"')
    #     self.assertEqual(R.toString('\n \n'), '"\\n \\n"')
    #     self.assertEqual(R.toString('\r \r'), '"\\r \\r"')
    #     self.assertEqual(R.toString('\t \t'), '"\\t \\t"')
    #     self.assertEqual(R.toString('\v \v'), '"\\v \\v"')
    #     self.assertEqual(R.toString('\0 \0'), '"\\0 \\0"')
    #     self.assertEqual(R.toString('\\ \\'), '"\\\\ \\\\"')

    def test_returns_the_string_representation_of_a_Boolean_object(self):
        self.assertEqual(R.toString(bool(True)), 'True')
        self.assertEqual(R.toString(bool(False)), 'False')

    def test_returns_the_string_representation_of_a_Number_object(self):
        self.assertEqual(R.toString(0), '0')
        # self.assertEqual(R.toString(-0), '-0')

    # def test_returns_the_string_representation_of_a_String_object(self):
    #     self.assertEqual(R.toString(String('abc')), 'String("abc")')
    #     self.assertEqual(R.toString(String('x "y" z')), 'String("x \\"y\\" z")')
    #     self.assertEqual(R.toString(String("' '")), 'String("\' \'")')
    #     self.assertEqual(R.toString(String('" "')), 'String("\\" \\"")')
    #     self.assertEqual(R.toString(String('\b \b')), 'String("\\b \\b")')
    #     self.assertEqual(R.toString(String('\f \f')), 'String("\\f \\f")')
    #     self.assertEqual(R.toString(String('\n \n')), 'String("\\n \\n")')
    #     self.assertEqual(R.toString(String('\r \r')), 'String("\\r \\r")')
    #     self.assertEqual(R.toString(String('\t \t')), 'String("\\t \\t")')
    #     self.assertEqual(R.toString(String('\v \v')), 'String("\\v \\v")')
    #     self.assertEqual(R.toString(String('\0 \0')), 'String("\\0 \\0")')
    #     self.assertEqual(R.toString(String('\\ \\')), 'String("\\\\ \\\\")')

    # def test_returns_the_string_representation_of_a_Date_object(self):
    #     self.assertEqual(R.toString(Date('2001-02-03T04:05:06.000Z')), 'Date("2001-02-03T04:05:06.000Z")')
    #     self.assertEqual(R.toString(Date('XXX')), 'Date(NaN)')

    # def test_returns_the_string_representation_of_a_RegExp_object(self):
    #     self.assertEqual(R.toString(/(?:)/), '/(?:)/')
    #     self.assertEqual(R.toString(/\#g), '/\\#g')

    # def test_returns_the_string_representation_of_a_function(self):
    #     add = lambda a, b: a + b
    #     self.assertEqual(R.toString(add), add.toString())

    def test_returns_the_string_representation_of_an_array(self):
        self.assertEqual(R.toString([]), '[]')
        self.assertEqual(R.toString([1, 2, 3]), '[1, 2, 3]')
        self.assertEqual(R.toString([1, [2, [3]]]), '[1, [2, [3]]]')
        self.assertEqual(R.toString(['x', 'y']), "['x', 'y']")

    # def test_returns_the_string_representation_of_an_array_with_non_numeric_property_names(self):
    #     xs = [1, 2, 3]
    #     xs.foo = 0
    #     xs.bar = 0
    #     xs.baz = 0

    #     self.assertEqual(R.toString(xs), '[1, 2, 3, "bar": 0, "baz": 0, "foo": 0]')

    # def test_returns_the_string_representation_of_an_arguments_object(self):
    #     self.assertEqual(R.toString((lambda ) { return arguments })()), '(function(:{ arguments }())')
    #     self.assertEqual(R.toString((lambda ) { return arguments })(1, 2, 3)), '(function(:{ arguments }(1, 2, 3))')
    #     self.assertEqual(R.toString((lambda ) { return arguments })(['x', 'y'])), '(function(:{ arguments }(["x", "y"]))')

    def test_returns_the_string_representation_of_a_plain_object(self):
        self.assertEqual(R.toString({}), '{}')
        self.assertEqual(R.toString({'foo': 1, 'bar': 2, 'baz': 3}), "{'foo': 1, 'bar': 2, 'baz': 3}")
        # self.assertEqual(R.toString({'"quoted"': True}), '{"\\"quoted\\"": True}')
        self.assertEqual(R.toString({'a': {'b': {'c': {}}}}), "{'a': {'b': {'c': {}}}}")

    # def test_treats_instance_without_custom_toString_method_as_plain_object(self):
    #     function Point(x, y) {
    #         this.x = x
    #         this.y = y
    #     }
    #     self.assertEqual(R.toString(Point(1, 2)), '{"x": 1, "y": 2}')

    # def test_dispatches_to_custom_toString_method(self):
    #     function Point(x, y) {
    #         this.x = x
    #         this.y = y
    #     }
    #     Point.prototype.toString = function() {
    #         return 'Point(' + this.x + ', ' + this.y + ')'
    #     }
    #     self.assertEqual(R.toString(Point(1, 2)), 'Point(1, 2)')

    #     function Just(x) {
    #         if (!(this instanceof Just)) {
    #             return Just(x)
    #         }
    #         this.value = x
    #     }
    #     Just.prototype.toString = function() {
    #         return 'Just(' + R.toString(this.value) + ')'
    #     }
    #     self.assertEqual(R.toString(Just(42)), 'Just(42)')
    #     self.assertEqual(R.toString(Just([1, 2, 3])), 'Just([1, 2, 3])')
    #     self.assertEqual(R.toString(Just(Just(Just('')))), 'Just(Just(Just("")))')

    #     self.assertEqual(R.toString({toString: R.always('x')}), 'x')

    # def test_handles_object_with_no_toString_method(self):
    #     if (typeof Object.create == 'function') {
    #         a = Object.create(None)
    #         b = Object.create(None) b.x = 1 b.y = 2
    #         self.assertEqual(R.toString(a), '{}')
    #         self.assertEqual(R.toString(b), '{"x": 1, "y": 2}')
    #     }

    def test_handles_circular_references(self):
        a = [None]
        a[0] = a
        self.assertEqual(R.toString(a), '[[...]]')

        o = {}
        o['o'] = o
        self.assertEqual(R.toString(o), "{'o': {...}}")

        b = ['bee', None]
        c = ['see', None]
        b[1] = c
        c[1] = b
        self.assertEqual(R.toString(b), "['bee', ['see', [...]]]")
        self.assertEqual(R.toString(c), "['see', ['bee', [...]]]")

        p = {}
        q = {}
        p['q'] = q
        q['p'] = p
        self.assertEqual(R.toString(p), "{'q': {'p': {...}}}")
        self.assertEqual(R.toString(q), "{'p': {'q': {...}}}")

        x = [None]
        y = {}
        x[0] = y
        y['x'] = x
        self.assertEqual(R.toString(x), "[{'x': [...]}]")
        self.assertEqual(R.toString(y), "{'x': [{...}]}")


if __name__ == '__main__':
    unittest.main()
