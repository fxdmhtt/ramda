# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def sortWith(fns, list):
    def function(a, b):
        result = 0
        i = 0
        while result == 0 and i < len(fns):
            result = fns[i](a, b)
            i += 1
        return result
    from functools import cmp_to_key
    return sorted(list[0:], key=cmp_to_key(function))
