# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pickAll(names, obj):
    result = {}
    idx = 0
    len_ = len(names)
    while idx < len_:
        name = names[idx]
        result[name] = obj.get(name)
        idx += 1
    return result
