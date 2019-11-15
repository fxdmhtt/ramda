# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def mapAccumRight(fn, acc, list):
    idx = len(list) - 1
    result = [None] * len(list)
    tuple = [acc]
    while idx >= 0:
        tuple = fn(tuple[0], list[idx])
        result[idx] = tuple[1]
        idx -= 1
    return [tuple[0], result]
