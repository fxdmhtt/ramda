# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def fromPairs(pairs):
    result = {}
    idx = 0
    while idx < len(pairs):
        result[pairs[idx][0]] = pairs[idx][1]
        idx += 1
    return result
