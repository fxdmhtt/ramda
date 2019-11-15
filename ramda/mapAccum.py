# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def mapAccum(fn, acc, list):
    idx = 0
    len_ = len(list)
    result = []
    tuple = [acc]
    while idx < len_:
        tuple = fn(tuple[0], list[idx])
        result.append(tuple[1])
        idx += 1
    return [tuple[0], result]
