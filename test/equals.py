# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import datetime

class Test_equals(unittest.TestCase):
    def setUp(self):
        self.a = []
        self.b = self.a

    def test_tests_for_deep_equality_of_its_operands(self):
        eq(self, R.equals(100, 100), True)
        eq(self, R.equals(100, '100'), False)
        eq(self, R.equals([], []), True)
        eq(self, R.equals(self.a, self.b), True)

    def test_considers_equal_Boolean_primitives_equal(self):
        eq(self, R.equals(True, True), True)
        eq(self, R.equals(False, False), True)
        eq(self, R.equals(True, False), False)
        eq(self, R.equals(False, True), False)

    def test_considers_equivalent_Boolean_objects_equal(self):
        eq(self, R.equals(bool(True), bool(True)), True)
        eq(self, R.equals(bool(False), bool(False)), True)
        eq(self, R.equals(bool(True), bool(False)), False)
        eq(self, R.equals(bool(False), bool(True)), False)

    # def test_never_considers_Boolean_primitive_equal_to_Boolean_object(self):
        # eq(self, R.equals(True, bool(True)), False)
        # eq(self, R.equals(bool(True), True), False)
        # eq(self, R.equals(False, bool(False)), False)
        # eq(self, R.equals(bool(False), False), False)

    def test_considers_equal_number_primitives_equal(self):
        eq(self, R.equals(0, 0), True)
        eq(self, R.equals(0, 1), False)
        eq(self, R.equals(1, 0), False)

    def test_considers_equivalent_Number_objects_equal(self):
        eq(self, R.equals(float(0), float(0)), True)
        eq(self, R.equals(float(0), float(1)), False)
        eq(self, R.equals(float(1), float(0)), False)

    def test_never_considers_number_primitive_equal_to_Number_object(self):
        eq(self, R.equals(0, float(0)), False)
        eq(self, R.equals(float(0), 0), False)

    def test_considers_equal_string_primitives_equal(self):
        eq(self, R.equals('', ''), True)
        eq(self, R.equals('', 'x'), False)
        eq(self, R.equals('x', ''), False)
        eq(self, R.equals('foo', 'foo'), True)
        eq(self, R.equals('foo', 'bar'), False)
        eq(self, R.equals('bar', 'foo'), False)

    def test_considers_equivalent_String_objects_equal(self):
        eq(self, R.equals(str(''), str('')), True)
        eq(self, R.equals(str(''), str('x')), False)
        eq(self, R.equals(str('x'), str('')), False)
        eq(self, R.equals(str('foo'), str('foo')), True)
        eq(self, R.equals(str('foo'), str('bar')), False)
        eq(self, R.equals(str('bar'), str('foo')), False)

    # def test_never_considers_string_primitive_equal_to_String_object(self):
    #     eq(self, R.equals('', str('')), False)
    #     eq(self, R.equals(str(''), ''), False)
    #     eq(self, R.equals('x', str('x')), False)
    #     eq(self, R.equals(str('x'), 'x'), False)

    def test_handles_objects(self):
        eq(self, R.equals({}, {}), True)
        eq(self, R.equals({'a':1, 'b':2}, {'a':1, 'b':2}), True)
        eq(self, R.equals({'a':2, 'b':3}, {'b':3, 'a':2}), True)
        eq(self, R.equals({'a':2, 'b':3}, {'a':3, 'b':3}), False)
        eq(self, R.equals({'a':2, 'b':3, 'c':1}, {'a':2, 'b':3}), False)

    def test_considers_equivalent_Arguments_objects_equal(self):
        a = (lambda *arguments: list(arguments))()
        b = (lambda *arguments: list(arguments))()
        c = (lambda *arguments: list(arguments))(1, 2, 3)
        d = (lambda *arguments: list(arguments))(1, 2, 3)

        eq(self, R.equals(a, b), True)
        eq(self, R.equals(b, a), True)
        eq(self, R.equals(c, d), True)
        eq(self, R.equals(d, c), True)
        eq(self, R.equals(a, c), False)
        eq(self, R.equals(c, a), False)

    def test_considers_equivalent_Error_objects_equal(self):
        # eq(self, R.equals(Exception('XXX'), Exception('XXX')), True)
        eq(self, R.equals(Exception('XXX'), Exception('YYY')), False)
        eq(self, R.equals(Exception('XXX'), TypeError('XXX')), False)
        eq(self, R.equals(Exception('XXX'), TypeError('YYY')), False)

    # supportsSticky = False
    # try { RegExp('', 'y') supportsSticky = True } catch (e) {}

    # supportsUnicode = False
    # try { RegExp('', 'u') supportsUnicode = True } catch (e) {}

    # def test_handles_regex(self):
    #     eq(self, R.equals(/\s/, /\s/), True)
    #     eq(self, R.equals(/\s/, /\d/), False)
    #     eq(self, R.equals(/self.a/gi, /self.a/ig), True)
    #     eq(self, R.equals(/self.a/mgi, /self.a/img), True)
    #     eq(self, R.equals(/self.a/gi, /self.a/i), False)

    #     if (supportsSticky) {
    #         # eq(self, R.equals(/\s/y, /\s/y), True)
    #         # eq(self, R.equals(/self.a/mygi, /self.a/imgy), True)
    #     }

    #     if (supportsUnicode) {
    #         # eq(self, R.equals(/\s/u, /\s/u), True)
    #         # eq(self, R.equals(/self.a/mugi, /self.a/imgu), True)
    #     }

    def test_handles_lists(self):
        listA = [1, 2, 3]
        listB = [1, 3, 2]
        eq(self, R.equals([], {}), False)
        eq(self, R.equals(listA, listB), False)

    def test_handles_recursive_data_structures(self):
        c = {};c['v'] = c
        d = {};d['v'] = d
        e = [];e.append(e)
        f = [];f.append(f)
        nestA = {'a':[1, 2, {'c':1}], 'b':1}
        nestB = {'a':[1, 2, {'c':1}], 'b':1}
        nestC = {'a':[1, 2, {'c':2}], 'b':1}
        # eq(self, R.equals(c, d), True)
        # eq(self, R.equals(e, f), True)
        eq(self, R.equals(nestA, nestB), True)
        eq(self, R.equals(nestA, nestC), False)

    def test_handles_dates(self):
        eq(self, R.equals(datetime.timedelta(0), datetime.timedelta(0)), True)
        eq(self, R.equals(datetime.timedelta(1), datetime.timedelta(1)), True)
        eq(self, R.equals(datetime.timedelta(0), datetime.timedelta(1)), False)
        eq(self, R.equals(datetime.timedelta(1), datetime.timedelta(0)), False)

    # def test_requires_that_both_objects_have_the_same_enumerable_properties_with_the_same_values(self):
    #     a1 = []
    #     a2 = []
    #     a2.x = 0

    #     b1 = bool(False)
    #     b2 = bool(False)
    #     b2.x = 0

    #     d1 = datetime.timedelta(0)
    #     d2 = datetime.timedelta(0)
    #     d2.x = 0

    #     n1 = float(0)
    #     n2 = float(0)
    #     n2.x = 0

    #     r1 = /(?:)/
    #     r2 = /(?:)/
    #     r2.x = 0

    #     s1 = str('')
    #     s2 = str('')
    #     s2.x = 0

    #     eq(self, R.equals(a1, a2), False)
    #     eq(self, R.equals(b1, b2), False)
    #     eq(self, R.equals(d1, d2), False)
    #     eq(self, R.equals(n1, n2), False)
    #     eq(self, R.equals(r1, r2), False)
    #     eq(self, R.equals(s1, s2), False)


    # if (typeof ArrayBuffer != 'None' && typeof Int8Array != 'None') {
    #     typArr1 = ArrayBuffer(10)
    #     typArr1[0] = 1
    #     typArr2 = ArrayBuffer(10)
    #     typArr2[0] = 1
    #     typArr3 = ArrayBuffer(10)
    #     intTypArr = Int8Array(typArr1)
    #     typArr3[0] = 0
    #     def test_handles_typed_arrays(self):
    #         eq(self, R.equals(typArr1, typArr2), True)
    #         eq(self, R.equals(typArr1, typArr3), False)
    #         eq(self, R.equals(typArr1, intTypArr), False)
    
    # }

    # if (typeof Promise != 'None') {
    #     def test_compares_Promise_objects_by_identity(self):
    #         p = Promise.resolve(42)
    #         q = Promise.resolve(42)
    #         eq(self, R.equals(p, p), True)
    #         eq(self, R.equals(p, q), False)
    
    # }

    # if (typeof Map != 'None') {
    #     def test_compares_Map_objects_by_value(self):
    #         eq(self, R.equals(Map([]), Map([])), True)
    #         eq(self, R.equals(Map([]), Map([[1, 'self.a']])), False)
    #         eq(self, R.equals(Map([[1, 'self.a']]), Map([])), False)
    #         eq(self, R.equals(Map([[1, 'self.a']]), Map([[1, 'self.a']])), True)
    #         eq(self, R.equals(Map([[1, 'self.a'], [2, 'self.b']]), Map([[2, 'self.b'], [1, 'self.a']])), True)
    #         eq(self, R.equals(Map([[1, 'self.a']]), Map([[2, 'self.a']])), False)
    #         eq(self, R.equals(Map([[1, 'self.a']]), Map([[1, 'self.b']])), False)
    #         eq(self, R.equals(Map([[1, 'self.a'], [2, Map([[3, 'c']])]]), Map([[1, 'self.a'], [2, Map([[3, 'c']])]])), True)
    #         eq(self, R.equals(Map([[1, 'self.a'], [2, Map([[3, 'c']])]]), Map([[1, 'self.a'], [2, Map([[3, 'd']])]])), False)
    #         eq(self, R.equals(Map([[[1, 2, 3], [4, 5, 6]]]), Map([[[1, 2, 3], [4, 5, 6]]])), True)
    #         eq(self, R.equals(Map([[[1, 2, 3], [4, 5, 6]]]), Map([[[1, 2, 3], [7, 8, 9]]])), False)
    
    #     def test_dispatches_to_`equals`_method_recursively_in_Set(self):
    #         self.a = Map()
    #         self.b = Map()
    #         self.a.set(self.a, self.a)
    #         eq(self, R.equals(self.a, self.b), False)
    #         self.a.set(self.b, self.b)
    #         self.b.set(self.b, self.b)
    #         self.b.set(self.a, self.a)
    #         eq(self, R.equals(self.a, self.b), True)
    
    # }

    # if (typeof Set != 'None') {
    #     def test_compares_Set_objects_by_value(self):
    #         eq(self, R.equals(Set([]), Set([])), True)
    #         eq(self, R.equals(Set([]), Set([1])), False)
    #         eq(self, R.equals(Set([1]), Set([])), False)
    #         eq(self, R.equals(Set([1, 2]), Set([2, 1])), True)
    #         eq(self, R.equals(Set([1, Set([2, Set([3])])]), Set([1, Set([2, Set([3])])])), True)
    #         eq(self, R.equals(Set([1, Set([2, Set([3])])]), Set([1, Set([2, Set([4])])])), False)
    #         eq(self, R.equals(Set([[1, 2, 3], [4, 5, 6]]), Set([[1, 2, 3], [4, 5, 6]])), True)
    #         eq(self, R.equals(Set([[1, 2, 3], [4, 5, 6]]), Set([[1, 2, 3], [7, 8, 9]])), False)
    
    #     def test_dispatches_to_`equals`_method_recursively_in_Set(self):
    #         self.a = Set()
    #         self.b = Set()
    #         self.a.add(self.a)
    #         eq(self, R.equals(self.a, self.b), False)
    #         self.a.add(self.b)
    #         self.b.add(self.b)
    #         self.b.add(self.a)
    #         eq(self, R.equals(self.a, self.b), True)
    
    # }

    # if (typeof WeakMap != 'None') {
    #     def test_compares_WeakMap_objects_by_identity(self):
    #         m = WeakMap([])
    #         eq(self, R.equals(m, m), True)
    #         eq(self, R.equals(m, WeakMap([])), False)
    
    # }

    # if (typeof WeakSet != 'None') {
    #     def test_compares_WeakSet_objects_by_identity(self):
    #         s = WeakSet([])
    #         eq(self, R.equals(s, s), True)
    #         eq(self, R.equals(s, WeakSet([])), False)
    
    # }

    # def test_dispatches_to_`equals`_method_recursively(self):
    #     function Left(x) { this.value = x }
    #     Left.prototype.equals = function(x) {
    #         return x instanceof Left && R.equals(x.value, this.value)
    #     }

    #     function Right(x) { this.value = x }
    #     Right.prototype.equals = function(x) {
    #         return x instanceof Right && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.equals(Left([42]), Left([42])), True)
    #     eq(self, R.equals(Left([42]), Left([43])), False)
    #     eq(self, R.equals(Left(42), {value: 42}), False)
    #     eq(self, R.equals({value: 42}, Left(42)), False)
    #     eq(self, R.equals(Left(42), Right(42)), False)
    #     eq(self, R.equals(Right(42), Left(42)), False)

    #     eq(self, R.equals([Left(42)], [Left(42)]), True)
    #     eq(self, R.equals([Left(42)], [Right(42)]), False)
    #     eq(self, R.equals([Right(42)], [Left(42)]), False)
    #     eq(self, R.equals([Right(42)], [Right(42)]), True)


    # def test_is_commutative(self):
    #     function Point(x, y) {
    #         this.x = x
    #         this.y = y
    #     }
    #     Point.prototype.equals = function(point) {
    #         return point instanceof Point &&
    #                      this.x == point.x && this.y == point.y
    #     }

    #     function ColorPoint(x, y, color) {
    #         this.x = x
    #         this.y = y
    #         this.color = color
    #     }
    #     ColorPoint.prototype = Point(0, 0)
    #     ColorPoint.prototype.equals = function(point) {
    #         return point instanceof ColorPoint &&
    #                      this.x == point.x && this.y == point.y &&
    #                      this.color == point.color
    #     }

    #     eq(self, R.equals(Point(2, 2), ColorPoint(2, 2, 'red')), False)
    #     eq(self, R.equals(ColorPoint(2, 2, 'red'), Point(2, 2)), False)


if __name__ == '__main__':
    unittest.main()
