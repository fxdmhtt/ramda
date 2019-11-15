# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from functools import cmp_to_key

@_curry2
def sortWith(fns, list):
    def function(a, b):
        for i in range(len(fns)):
            result = fns[i](a, b)
            if result != 0:
                return result
        return 0
    return sorted(list, key=cmp_to_key(function))
