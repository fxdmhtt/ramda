# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_reduce(unittest.TestCase):
    def setUp(self):
        self.add = lambda a, b: a + b
        self.mult = lambda a, b: a * b

    def test_folds_simple_functions_over_arrays_with_the_supplied_accumulator(self):
        eq(self, R.reduce(self.add, 0, [1, 2, 3, 4]), 10)
        eq(self, R.reduce(self.mult, 1, [1, 2, 3, 4]), 24)

    def test_dispatches_to_objects_that_implement_reduce(self):
        obj = {'x': [1, 2, 3], 'reduce': lambda *_: 'override'}
        eq(self, R.reduce(self.add, 0, obj), 'override')
        eq(self, R.reduce(self.add, 10, obj), 'override')

    def test_returns_the_accumulator_for_an_empty_array(self):
        eq(self, R.reduce(self.add, 0, []), 0)
        eq(self, R.reduce(self.mult, 1, []), 1)
        eq(self, R.reduce(R.concat, [], []), [])

    # def test_Prefers_the_use_of_the_iterator_of_an_object_over_reduce_and_handles_short_circuits(self):
    #     symIterator = (typeof Symbol != 'None') ? Symbol.iterator : '@@iterator'

    #     function Reducible(arr) {
    #         this.arr = arr
    #     }

    #     Reducible.prototype.reduce = function(f, init) {
    #         acc = init
    #         for (i = 0 i < this.arr.length i += 1) {
    #             acc = f(acc, this.arr[i])
    #         }
    #         return acc
    #     }

    #     Reducible.prototype[symIterator] = function() {
    #         a = this.arr
    #         return {
    #             _pos: 0,

    #             next: function() {
    #                 if (this._pos < a.length) {
    #                     v = a[this._pos]
    #                     this._pos += 1
    #                     return {
    #                         value: v,
    #                         done: False
    #                     }
    #                 } else {
    #                     return {
    #                         done: True
    #                     }
    #                 }
    #             }
    #         }
    #     }

    #     xf = R.take(2)
    #     apendingT = { }
    #     apendingT['@@transducer/result'] = R.identity
    #     apendingT['@@transducer/step'] = R.flip(R.append)

    #     rfn = xf(apendingT)
    #     list = Reducible([1, 2, 3, 4, 5, 6])

    #     eq(self, R.reduce(rfn, [], list), [1, 2])

    # def test_short_circuits_with_reduced(self):
    #     addWithMaxOf10 = lambda acc, val:{ acc + val > 10 ? R.reduced(acc) : acc + val}
    #     eq(self, R.reduce(addWithMaxOf10, 0, [1, 2, 3, 4]), 10)
    #     eq(self, R.reduce(addWithMaxOf10, 0, [2, 4, 6, 8]), 6)


if __name__ == '__main__':
    unittest.main()
