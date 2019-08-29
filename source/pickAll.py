# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pickAll(names, obj):
    result = {}
    idx = 0
    len = len(names)
    while idx < len:
        name = names[idx]
        result[name] = obj[name]
        idx += 1
    return result
