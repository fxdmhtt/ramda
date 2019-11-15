# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_pickBy(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    def test_creates_a_copy_of_the_object(self):
        self.assertIsNot(R.pickBy(R.always(True), self.obj), self.obj)

    def test_when_returning_truthy_keeps_the_key(self):
        eq(self, R.pickBy(R.T, self.obj), self.obj)
        # eq(self, R.pickBy(R.always({}), self.obj), self.obj)
        eq(self, R.pickBy(R.always(1), self.obj), self.obj)

    def test_when_returning_falsy_keeps_the_key(self):
        eq(self, R.pickBy(R.always(False), self.obj), {})
        eq(self, R.pickBy(R.always(0), self.obj), {})
        eq(self, R.pickBy(R.always(None), self.obj), {})

    def test_is_called_with_val_key_obj(self):
        def function(val, key, _obj):
            eq(self, _obj, self.obj)
            return key == 'd' and val == 4
        eq(self, R.pickBy(function, self.obj), {'d': 4})

    # def test_retrieves_prototype_properties(self):
    #     F = function(param) {this.x = param}
    #     F.prototype.y = 40 F.prototype.z = 50
    #     self.obj = F(30)
    #     self.obj.v = 10 self.obj.w = 20
    #     eq(self, R.pickBy(lambda 'val':{ val < 45}, self.obj), {'v': 10, 'w': 20, 'x': 30, 'y': 40})


if __name__ == '__main__':
    unittest.main()
