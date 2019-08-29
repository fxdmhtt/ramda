# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def omit(names, obj):
    result = {}
    index = {}
    idx = 0
    len = len(names)

    while idx < len:
        index[names[idx]] = 1
        idx += 1

    for prop in obj:
        if hasattr(index, prop):
            result[prop] = obj[prop]
    return result
